from aws_lambda_powertools.utilities.typing import LambdaContext
import requests
from requests.models import Response
import os


def notify_to_slack() -> Response:
    try:
        res = requests.post(
            url=os.environ["SLACK_URL"],
            json={"text": "AWS lambda からの通知です"},
            headers={"Content-Type": "application/json"},
        )
        print(res)
        res.raise_for_status()
    except Exception as e:
        print(f"Slack 通知に失敗しました: {e}")

    return res


def lambda_handler(event: dict, context: LambdaContext):
    print(event)
    print(context)

    res = notify_to_slack()

    print("Slack 通知に成功しました")
    return res.json()
