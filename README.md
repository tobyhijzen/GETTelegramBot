# GET telegram bot

## Setup

```bash
sudo pip3 install python-telegram-bot web3 datetime
```

The GET telegram bot communicates with a public ethereum node run by infura. To run these nodes you need to create an account on `infura.io`. Then you will need to create a project and export the project ID and SECRET for use by the monitor. Add the following to your `.bashrc`:

```bash
export WEB3_INFURA_PROJECT_ID= <your-id>
export WEB3_INFURE_PROJECT_SECRET= <your-secret>
export TELEGRAM_GET_COMMUNITY_TOKEN= <telegram-bot-token>
```
