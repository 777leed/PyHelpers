from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

flow = InstalledAppFlow.from_client_secrets_file(
    r'C:\Users\hp\Downloads\code_secret_client_491064337383-tr0snl8k7uie4iluae1r2p1f0q3i0u0k.apps.googleusercontent.com.json',
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])

flow.run_local_server()
credentials = flow.credentials

service = build('youtube', 'v3', credentials=credentials)
channel_response = service.channels().list(part='snippet', mine=True).execute()

# print the results to the console
for channel in channel_response['items']:
    print(f"Channel title: {channel['snippet']['title']}, ID: {channel['id']}")

# # prompt the user to enter the channel ID
# channel_id = input("Enter the channel ID: ")

# # switch to the specified channel
# service.channels().update(
#     part='snippet',
#     body={
#         'id': channel_id,
#         'snippet': {
#             'defaultLanguage': 'en'
#         }
#     }
# ).execute()
