#!/usr/bin/env python

from dotenv import load_dotenv
from flask import Flask
import logging
import os
from pathlib import Path
from slack import WebClient
from slackeventsapi import SlackEventAdapter

# ログ設定
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Slack設定
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = WebClient(token=os.environ["SLACK_TOKEN"])
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'],
    '/slack/events',
    app)
BOT_ID = client.api_call('auth.test')['user_id']


@slack_event_adapter.on("message")
def message(payload):
    logging.debug(payload)
    event = payload.get('event', {})
    if event['user'] != BOT_ID:
        client.chat_postMessage(
            channel=event["channel"],
            text=event["text"]
        )
    return "message"


# Start the server on port 3000
if __name__ == "__main__":
    app.run(port=3000)
