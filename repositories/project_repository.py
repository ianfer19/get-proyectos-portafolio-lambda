from boto3.dynamodb.conditions import Key
from config.database.dynamo import table

class ProjectRepository:
    
    @staticmethod
    def scan_all():
        response = table.scan()
        return response.get("Items", [])

    @staticmethod
    def query_by_skill(skill_id: str):
        response = table.query(
            IndexName="GSI1",
            KeyConditionExpression=Key("GSI1PK").eq(skill_id)
        )
        return response.get("Items", [])

    @staticmethod
    def get_by_keys(project_id: str, name: str):
        response = table.get_item(
            Key={
                "projectId": project_id,
                "name": name
            }
        )
        return response.get("Item")

    @staticmethod
    def get_by_project_id(project_id: str):
        # Query basado en PK (retorna el item principal)
        response = table.query(
            KeyConditionExpression=Key("projectId").eq(project_id)
        )
        items = response.get("Items", [])
        return items[0] if items else None
