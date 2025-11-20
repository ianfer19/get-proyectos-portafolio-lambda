from repositories.project_repository import ProjectRepository

class ProjectService:

    @staticmethod
    def get_all_projects():
        return ProjectRepository.scan_all()

    @staticmethod
    def get_projects_by_skill(skill_id: str):
        return ProjectRepository.find_by_skill(skill_id)

    @staticmethod
    def get_projects_by_skills(skills: list[str]):
        results = []
        seen = set()

        for skill in skills:
            items = ProjectRepository.find_by_skill(skill)
            for it in items:
                if it["projectId"] not in seen:
                    seen.add(it["projectId"])
                    results.append(it)

        return results
