# services/project_service.py

from repositories.project_repository import ProjectRepository

class ProjectService:
    
    @staticmethod
    def get_all_projects():
        return ProjectRepository.scan_all()

    @staticmethod
    def get_projects_by_skill(skill_id: str):
        # Items del índice GSI
        gsi_items = ProjectRepository.query_by_skill(skill_id)

        projects = []
        
        for gsi_item in gsi_items:
            project_id = gsi_item["projectId"]
            full_project = ProjectRepository.get_by_id(project_id)
            if full_project:
                projects.append(full_project)

        return projects

    @staticmethod
    def get_project_by_id(project_id: str):
        return ProjectRepository.get_by_id(project_id)