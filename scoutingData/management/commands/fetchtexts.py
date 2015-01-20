import re
import argparse
import pprint

import httplib2
from apiclient.discovery import build
from oauth2client import tools
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from scoutingData.models import Message, PerMatchTeamData, Match, Team

class Command(BaseCommand):
    help = 'Updates the database with scouting data from text messages'
    output_transaction = True # I think I want this set to true

    def parse_email_then_save_data(self, message_body, gmail_id):
        # expecting "Match:<match_number> Team:<team_number> Alliance:<alliance_color> Kills:<kills> Deaths:<deaths> Assists:<assists>"
        tokens = re.search(r'Match:([\d]*) Team:([\d]*) Alliance:([\w]*) Kills:([\d]*) Deaths:([\d]*) Assists:([\d]*)', message_body)
        if tokens:
            """
            self.stdout.write(tokens.group(1))
            self.stdout.write(tokens.group(2))
            self.stdout.write(tokens.group(3))
            self.stdout.write(tokens.group(4))
            self.stdout.write(tokens.group(5))
            self.stdout.write(tokens.group(6))
            """
            try:
                preexisting_match = Match.objects.get(match_number__exact=tokens.group(1))
            except ObjectDoesNotExist:
                m = Match(match_number=tokens.group(1))
                m.save()
                self.stdout.write("Created a new match:\n    %s" % (m))
        else:
            self.stdout.write("Could not parse info from text")
            return

        if tokens.group(6):
            self.stdout.write("Submission format appears to be correct.")
        else:
            self.stdout.write("Submission was not formatted correctly.")
            return

        if preexisting_match:
            pmtd = PerMatchTeamData(match_fk=preexisting_match, team=tokens.group(2))
            match_data = PerMatchTeamData.objects.filter(team=tokens.group(2)).filter(match_fk_id=tokens.group(1))
            if match_data:
                self.stdout.write("PerMatchTeamData for this submission already exists!")
                return
        else:
            pmtd = PerMatchTeamData(match_fk= m, team= tokens.group(2))
        if tokens.group(3) == 'red':
            pmtd.alliance_color = 'red'
        else:
            pmtd.alliance_color = 'blue'
        pmtd.kills = tokens.group(4)
        pmtd.deaths = tokens.group(5)
        pmtd.assists = tokens.group(6)
        pmtd.source_mail_id = gmail_id
        pmtd.save()
        
        """
        I will need to take the match object and manually look through and populate
        the alliance members.
        """
        # TODO make sure this works




    def handle(self, *args, **options):
        
        # Path to the client_secret.json file downloaded from the Developer Console
        CLIENT_SECRET_FILE = 'client_secret.json'

        # Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
        OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

        # Location of the credentials storage file
        STORAGE = Storage('gmail.storage')


        # Start the OAuth flow to retrieve credentials
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
        parser = argparse.ArgumentParser(parents=[tools.argparser])
        
        flags = tools.argparser.parse_args(args=[])
        http = httplib2.Http()

        # Try to retrieve credentials from storage or run the flow to generate them
        credentials = STORAGE.get()
        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, STORAGE, flags, http=http)

        # Authorize the httplib2.Http object with our credentials
        http = credentials.authorize(http)

        # Build the Gmail service from discovery
        gmail_service = build('gmail', 'v1', http=http)

        # Retrieve a page of messages
        messages = gmail_service.users().messages().list(userId='me').execute()

        # match_data_list


        if messages['messages']:
            for message in messages['messages']:
                #self.stdout.write('Message ID: %s' % (message['id']))
                messageObject = gmail_service.users().messages().get(id=message['id'], userId='me').execute()
                """ Trying to see what's inside the gmail message
                self.stdout.write("\n\n\n")
                pp = pprint.PrettyPrinter(indent=2)
                if pp.isrecursive(messageObject):
                    pp.pprint(messageObject)
                else:
                    stringy = pp.pformat(messageObject)
                    self.stdout.write(stringy)
                #self.stdout.write(message)
                self.stdout.write("\n\n\n")
                """
                self.stdout.write("\n\n")
                #headers = messageObject['payload']['headers']
                for dicts in messageObject['payload']['headers']:
                    if dicts['name']=='Subject':
                        phone_num_raw = dicts['value']

                p = re.compile('\d+')
                phone_token = p.findall(phone_num_raw)
                if phone_token:
                    #self.stdout.write("My re.findall() results: %s" % (phone_token))
                    phone_num = "%s%s%s" % (phone_token[0], phone_token[1], phone_token[2])
                    #self.stdout.write(phone_num)

                else:
                    self.stdout.write("oops I can't regex")
                # this will store some info about the gmail message just in case
                
                gmailMessage = Message(
                    gmail_message_id=message['id'],
                    sender_phone_number=phone_num,
                    message_body=messageObject['snippet']
                )
                gmailMessage.save()
                
                self.stdout.write(gmailMessage.gmail_message_id)
                self.stdout.write(gmailMessage.sender_phone_number)
                self.stdout.write(gmailMessage.message_body)
                # message_string = messageObject['snippet']
                self.parse_email_then_save_data(gmailMessage.message_body, message['id'])
                
        
        #self.stdout.write('My first django command!')




