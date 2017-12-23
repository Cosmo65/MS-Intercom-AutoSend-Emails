# Instructions

### Obtain client_secret.json
1. Go to [Google APIs Manager](https://console.developers.google.com/).
2. Create a new project with any Project name (Suggested Name: Intercom-AutoReply). Add Google Sheets API from the library to the project by enabling the API. 
3. Go to Credentials and add credentials to the project.

*Find out what kind of credentials you need*
- Which API are you using? Google Sheets API
- Where will you be calling the API from? Web server (e.g. node.js, Tomcat)
- What data will you be accessing? Application data
- Are you using Google App Enginer or Google Compute Engine? No, I'm not using them.

*Create a service account*
- Service account name: (any name; Suggested name: Intercom-AutoReply)
- Role: Project > Editor
- Key type: JSON

4. Click "continue" and a JSON file is downloaded. 
5. Rename the downloaded JSON file as **client_secret.json** and put it in the MS-Intercom-Autoreply/src folder.

### Run the server

1. Run the `main.py` in the MS-Intercom-AutoReply folder and open https://127.0.0.1:8080 in your browser.

2. Enter the name of the Google Sheet you are accessing.

3. Enter the name of the worksheet of the Google Sheet you are accessing.

Check out the GIF file that shows how the script works.

![How The Script Works](https://github.com/yongzx/MS-Intercom-AutoReply/blob/master/docs/Intercom-Automate-Email.gif)

Voila!
