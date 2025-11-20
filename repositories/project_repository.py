# repositories/project_repository.py

from boto3.dynamodb.conditions import Key
from config.database.dynamo import table

class ProjectRepository:
    
    @staticmethod
    def scan_all():
        response = table.scan()
        return response.get("Items", [])

    @staticmethod
    def query_by_skill(skill_id: str):
        # 1. Obtener items del índice
        gsi_items = ProjectRepository.query_by_skill(skill_id)

        projects = []

        for gsi_item in gsi_items:
            pid = gsi_item["projectId"]

            # 2. Obtener el item completo del proyecto
            full_project = ProjectRepository.get_by_id(pid)

            if full_project:
                projects.append(full_project)

        return projects

    @staticmethod
    def get_by_id(project_id: str):
        response = table.get_item(Key={"projectId": project_id})
        return response.get("Item")
