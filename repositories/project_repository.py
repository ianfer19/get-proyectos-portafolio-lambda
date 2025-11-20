# repositories/project_repository.py

from boto3.dynamodb.conditions import Key
from config.database.dynamo import table

class ProjectRepository:

    @staticmethod
    def scan_all():
        return table.scan().get("Items", [])

    @staticmethod
    def query_by_skill(skill_id: str):
        return table.query(
            IndexName="GSI1",
            KeyConditionExpression=Key("GSI1PK").eq(skill_id)
        ).get("Items", [])

    @staticmethod
    def get_by_id(project_id: str):
        return table.get_item(Key={"projectId": project_id}).get("Item")
