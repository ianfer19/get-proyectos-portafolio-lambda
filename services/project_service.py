# services/project_service.py

from repositories.project_repository import ProjectRepository

class ProjectService:
    
    @staticmethod
    def get_all_projects():
        return ProjectRepository.scan_all()

    @staticmethod
    def get_projects_by_skill(skill_id: str):
        return ProjectRepository.query_by_skill(skill_id)

    @staticmethod
    def get_project_by_id(project_id: str):
        return ProjectRepository.get_by_id(project_id)