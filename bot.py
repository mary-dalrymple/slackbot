import os
import csv
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

breach_report = open('breach_report.csv', 'r').read()
csv_obj = csv.DictReader(breach_report)

for b in csv_obj:
    obj = Summary.objects.create(
        submission_date = b['Breach Submission Date'],
        covered_entity = b['Name of Covered Entity']
    )

breaches_to_process = [b for b in breach_report if b.submission_date <= today]

for b in breaches_to_process:
    try:
        response = client.chat_postMessage(
            channel="slack-bots",
            text=f"New breach submission: {submission_date} by {covered_entity}"
        )

    except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'

# latest_breach = open('breach_report', 'w')
