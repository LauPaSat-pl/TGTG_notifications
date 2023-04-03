# TGTG notifications
[![CodeQL](https://github.com/LauPaSat-pl/TGTG_notifications/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/LauPaSat-pl/TGTG_notifications/actions/workflows/github-code-scanning/codeql)
Program run 100% on Github actions (not counting the set up), to check for your favourite TGTG bags
## How to use
1. Create a new Telegram bot using BotFather [tutorial](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot)
2. Check your Telegram ID [tutorial](https://www.alphr.com/telegram-find-user-id/)
3. Install tgtg library 
```
pip install tgtg
```
4. Run 
``` python
from tgtg import TgtgClient

client = TgtgClient(email="<your_email>")
credentials = client.get_credentials()
```
You should receive an email from tgtg. The client will wait until you validate the login by clicking the link inside the email.

Once you clicked the link, you will get credentials and be able to use them
``` python
print(credentials)
{
    'access_token': '<your_access_token>',
    'refresh_token': '<your_refresh_token>',
    'user_id': '<your_user_id>',
    'cookie': '<cookie>',
}
```
5. Fork this repo
6. In your repo add secrets you got from earlier steps (TGTG and Telegram), you can check how to name them in *notitications.yml* file
7. Make sure it's up and running
