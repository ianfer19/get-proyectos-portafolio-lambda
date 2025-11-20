from services.project_service import ProjectService
from utils.responses import success, error

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}

    # Filtro por skill
    if "skill" in params:
        skill_id = params["skill"]
        data = ProjectService.get_projects_by_skill(skill_id)
        return success(data)

    # Obtener todos
    data = ProjectService.get_all_projects()
    return success(data)
