from services.project_service import ProjectService
from utils.response import success, error

def lambda_handler(event, context):
    try:
        params = event.get("queryStringParameters", {}) or {}

        # Filtrar por multiples skills
        if "skills" in params:
            skills = [s.strip() for s in params["skills"].split(",")]
            return success(ProjectService.get_projects_by_skills(skills))

        # Filtrar por 1 skill
        if "skill" in params:
            return success(ProjectService.get_projects_by_skill(params["skill"]))

        return success(ProjectService.get_all_projects())
    except Exception as e:
        return error(str(e))
