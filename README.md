
## Project

Build a bot that extracts the following from people’s Twitter bio (on public/open accounts), into a Google spreadsheet:

* Twitter profile name
* Number of followers

Target accounts using either of these criteria:
* Based on hashtags used
* Based on number of followers; Between 1,000 - 50,000

The bot is suppose to maintain a session and continously listen to the predefined hashtag

## Development language
* Python 3.6.2

## Getting Started
* You need to set up the following to run the application successfully.

## Twitter Account/App Setup
1. Create a Twitter account in case you don't have one. https://twitter.com/signup
2. Go to apps.twitter.com and click on 'Create New App ' button.
3. Fill out the details of the form correctly.
4. Then click on the ‘Create your Twitter application’ button.
5. Replace the consumer key, consumer secret, access token and access token secret values with the ones you generate.

## Google Spreadsheet
1. Go to the Google API Console
2. Create a new project
3. Click Enable API. Search for and enable the Google Drive API.
4. Create credentials for a service account to access Application data.
5. Obtain OAuth2 credentials from Google Developers Console for google spreadsheet api and drive api
6. Save the file as client_secret.json in same directory as project.
5. Look up this link https://pygsheets.readthedocs.io/en/latest/authorizing.html for more information on Authorizing pygsheets

## Other Information
* Ensure you install all project dependencies
```
pip install -r requirements.txt
```
* Run Test
```
python -m unittest tests.test_bot tests.test_spreadsheets
```

* Run application
```
python bot.py
```
