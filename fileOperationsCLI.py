# coding: utf-8
import dropbox
import os
import sys

allowed_operations = ['send', 'list', 'delete', 'about',]

# validate arguments
if len(sys.argv) < 3:
	print ('Usage: python', sys.argv[0], '<operation> <file_path>')
	sys.exit(0)
	

if sys.argv[1] not in allowed_operations:
	print ('Operation:', sys.argv[1], 'is not suported')
	sys.exit(0)

# token aquired through Token Auth Process
access_token = os.getenv('DROPBOX_APP_TOKEN', 'Your Token Here')

# Client that we are using to execute the operations
client = dropbox.client.DropboxClient(access_token)

print('Welcome', client.account_info()['display_name'])

print('Executing:', sys.argv[1], 'operation')
operation = sys.argv[1]

if operation == 'list':
	total_space = 0
	# depending of your app permission this should show files from your dropbox root or app folder
	root_folder = client.metadata(sys.argv[2])
	print('Files in Folder: "%s"' % (sys.argv[2]))
	for arq in root_folder['contents']:
		if arq['is_dir']:
			print('Folder: "%s"' % (arq['path'],))
		else:
			total_space = total_space + arq['bytes']
			print('File: "%s", Mime: "%s", Size: "%s Bytes"' % (arq['path'], arq['mime_type'], arq['size'],))
	print('Total Space: %.1f KBytes' % (total_space/1024,))
elif operation == 'send': #create or update file into Dropbox
	print('Sending File:', sys.argv[2], 'to Dropbox')
	f = open(sys.argv[2], 'rb')
	response = client.put_file('/' + f.name, f, overwrite=True)
	# your installed Dropbox Client should warn you about this upload
	print('Uploaded:', response['path'], 'Size:', response['size'], 'Revision:', response['revision'])
elif operation == 'delete': #remove a remote File or folder
	print('Deleting file:', sys.argv[2], 'From Dropbox')
	response = client.file_delete(sys.argv[2])
elif operation == 'about': #List some information about remote file or folder
	print('About file:', sys.argv[2], 'From Dropbox')
	response = client.metadata(sys.argv[2])
	print('Path:', response['path'], 'Size:', response['size'], 'Root:', response['root'])
print('Done!')
