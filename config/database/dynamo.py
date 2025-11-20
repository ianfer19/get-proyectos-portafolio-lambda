import boto3
from botocore.config import Config

DYNAMO_TABLE_NAME = "iam-portafolio-projects-pdn"

_config = Config(
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
)

dynamodb = boto3.resource("dynamodb", config=_config)
table = dynamodb.Table(DYNAMO_TABLE_NAME)
