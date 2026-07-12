import json
import os
import boto3
import requests
from datetime import datetime

s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]

API_URL = "https://api.tfl.gov.uk/line/244/arrivals"

def lambda_handler(event, context):

    response = requests.get(API_URL)

    data = response.json()

    file_name = datetime.utcnow().strftime("%Y%m%d_%H%M%S") + ".json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"raw/{file_name}",
        Body=json.dumps(data)
    )

    return {
        "statusCode": 200
    }
