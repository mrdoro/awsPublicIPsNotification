import json
import logging
from src.common.check_instances import check_public_ip
from src.common.data_extractor import prepare_payload
from src.common.send_notification import send_notification

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Payload received the the lambda function:" + json.dumps(event))
    body = event['Records'][0]['body']
    logger.info("Extracted body from the event: " + body)
    record = json.loads(body)
    logger.info("Preparing payload for the notification...")
    message = prepare_payload(record)
    logger.info("Sending notification...")
    send_notification(message)
    
    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully'
    }
