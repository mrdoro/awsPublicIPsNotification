import boto3
import json
import os

sns = boto3.client('sns')

SNS_TOPIC = os.environ['SNS_TOPIC']

def send_notification(payload):
    for pld in payload:
        payload = json.loads(pld)
        print("Payload received by send_notification: ", pld)
        description = f"New public ip is allocated: {payload['eip']}\nAccount id: {payload['account_id']}\nRegion: {payload['region']}\nDate: {payload['time']}"
        eventName = payload['event_name']
        message = {
                "version": "1.0",
                "source": "custom",
                "id": "c-weihfjdsf",
                "content": {
                    "textType": "client-markdown",
                    "title": ":warning: New Public IP is allocated!",
                    "description": description,
                    "keywords": [
                        "PublicIP",
                        "Critical",
                        "SRE"
                    ]
                },
                "metadata": {
                    "summary": "Public IP allocated",
                    "eventType": eventName,
                    "relatedResources": [
                        payload['eip']
                    ],
                    "additionalContext": {
                        "priority": "critical"
                    }
                }
        }

        response = sns.publish(
                TopicArn= SNS_TOPIC,
                Message=json.dumps(message)
        )

        print("Notification sent successfully: " + json.dumps(response))