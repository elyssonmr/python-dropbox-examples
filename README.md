#Python Dropbox API Examples


These are some examples of how you can use Python's Dropbox API in your projects.

Before we get started is necessary to do a few steps to configure dropbox and your environment.

First of all we need to create a new APP in your dropbox account [https://www.dropbox.com/developers/apps](https://www.dropbox.com/developers/apps). If you don't have an account you can [register here](https://db.tt/8aGace0).

Then you must install Dropbox Package in your environment. It can be done using [pip](http://www.pip-installer.org/en/latest/) command:
```
pip install dropbox
```
This command will install Dropbox API and all its dependency needed to get started.

Add your Dropbox information into your system variables to be more easy and quickly run the examples. Into a Linux the *export* command can handle it
```
export DROPBOX_APP_KEY=<your_app_key>
export DROPBOX_APP_SECRET=<your_app_secret>
export DROPBOX_APP_TOKEN=<your_app_token>
```

More information about environment variables in Linux systems can be found [here](http://www.cyberciti.biz/faq/set-environment-variable-linux/).

**These examples where run using Python 3.3**

#How to Contribute
You can contribute by creating more examples and finding any bugs or improvements for the examples already done. Also you can help sharing to your friends.