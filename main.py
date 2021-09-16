import json
import requests
import csv

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'john-roe'
# You have to create a Github Token here https://github.com/settings/tokens and your user must have permissions to the repository you will execute this program
PASSWORD = 'ghp_aaaaaaaaaaaaaaaaa'

# The repository to add this issue to
REPO_OWNER = 'john-roe'
REPO_NAME = 'myrepo'


def make_github_issue(title, body=None, assignees=None, labels=None, milestone=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'assignees': [assignees],
             'labels': [labels],
             'milestone': [milestone]
             }
    
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', r.content)
        print(r)


with open('issues.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        make_github_issue(row['title'], row['body'])
