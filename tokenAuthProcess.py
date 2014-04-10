"""
	This code is from Skype Developer Site. 
	It's a example of how authorize your application.
"""
# coding:utf-8
import dropbox
import os
import webbrowser

# Get your app key and secret from the Dropbox developer website
app_key = os.getenv('DROPBOX_APP_KEY', "Dropbox App Key Here")
app_secret = os.getenv('DROPBOX_APP_SECRET', "Dropbox App secret Here")

# token Validation Flow
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()

webbrowser.open_new_tab(authorize_url)
print ('1. Click "Allow" (you might have to log in first)')
print ('2. Copy the authorization code.')
code = input("Enter the authorization code here: ").strip()

access_token, user_id = flow.finish(code)

print ('Returned Token:', access_token, '\nReturned UserId:', user_id)
print ('OBS: If you save your Token you do not have to pass through it again')

# Simply get your account information
client = dropbox.client.DropboxClient(access_token)
print ('Linked Account Information:', client.account_info())