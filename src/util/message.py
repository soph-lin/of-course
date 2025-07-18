import requests
import os
from dotenv import load_dotenv
import pync

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def notify_slack(message):
    if not SLACK_WEBHOOK_URL:
        print("❌ SLACK_WEBHOOK_URL not set.")
        return
    payload = { "text": message }
    r = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if r.status_code == 200:
        print("✅ Slack notification sent.")
    else:
        print("❌ Slack error:", r.text)

def notify_mac(message):
    pync.notify(message)