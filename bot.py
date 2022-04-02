import os
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

breach_report = open('breach_report.csv', 'r').read()

breaches_to_process = [b for b in breach_report if "Breach Submission Date" > (latest_breach)"Breach Submission Date"]

for b in breaches_to_process
      try:
         response = client.chat_postMessage(
            channel="slack-bots",
            text=f"New breach submission: {submission date} + {Name of Covered Entity}"
         )
except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
  assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'

latest_breach = open('breach_report', 'w')
