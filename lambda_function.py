# lambda_function.py

from services.project_service import ProjectService
from utils.response import success, error


def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}

    if "skill" in params:
        return success(ProjectService.get_projects_by_skill(params["skill"]))

    return success(ProjectService.get_all_projects())
