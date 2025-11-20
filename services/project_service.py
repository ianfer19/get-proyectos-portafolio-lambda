# services/project_service.py

from models.project import Project
from repositories.project_repository import ProjectRepository

class ProjectService:

    @staticmethod
    def get_all_projects():
        items = ProjectRepository.scan_all()
        return [Project(**item).dict() for item in items]

    @staticmethod
    def get_projects_by_skill(skill_id: str):
        items = ProjectRepository.query_by_skill(skill_id)
        return [Project(**item).dict() for item in items]

    @staticmethod
    def get_project_by_id(project_id: str):
        item = ProjectRepository.get_by_id(project_id)
        return Project(**item).dict() if item else None
