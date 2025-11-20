from config.database.dynamo import table
from boto3.dynamodb.conditions import Attr

class ProjectRepository:

    @staticmethod
    def scan_all():
        res = table.scan()
        return res.get("Items", [])

    @staticmethod
    def find_by_skill(skill_id: str):
        res = table.scan(
            FilterExpression=Attr("skillsIds").contains(skill_id)
        )
        return res.get("Items", [])
