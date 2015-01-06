import re

import httplib2
from apiclient.discovery import build
from oauth2client import tools
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

from django.core.management.base import BaseCommand, CommandError
from scoutingData.models import PerMatchTeamData, Match

class Command(BaseCommand):
    help = 'Updates the database with scouting data from text messages'

    def parse_email(message_body):
        # expecting "Match:<match_number> Team:<team_number> Alliance:<alliance_color> Kills:<kills> Deaths:<deaths> Assists:<assists>"
        tokens = re.search(r'Match:(\I+) Team:(\I+) Alliance:(\w+) Kills:(\I+) Deaths:(\I+) Assists:(\I+)', message_body)
        orgs = Match.objects.get(match_number__exact=tokens.group(1))
        pmtd = PerMatchTeamData(team= tokens.group(2))
        if orgs:
            pmtd.match_fk = orgs
        else:
            m = Match(match_number=tokens.group(1))
            m.save()
        pmtd = PerMatchTeamData(match_fk= m, team= tokens.group(2))
        if tokens.group(3) == 'red':
            pmtd.alliance_color = 'red'
        else:
            pmtd.alliance_color = 'blue'
        pmtd.kills = tokens.group(4)
        pmtd.deaths = tokens.group(5)
        pmtd.assists = tokens.group(6)




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

        match_data_list = new list
        

        if messages['messages']:
            for message in messages['messages']:
                #self.stdout.write('Message ID: %s' % (message['id']))
                self.stdout.write('Message ID: %s' % (message['id']))
                messageObject = gmail_service.users().messages().get(id=message['id'], userId='me').execute()
                self.stdout.write(messageObject['snippet'])
        
        #self.stdout.write('My first django command!')




