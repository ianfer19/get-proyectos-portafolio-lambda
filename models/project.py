from pydantic import BaseModel
from typing import List, Optional


class Skill(BaseModel):
    skillId: str
    name: str
    iconUrl: Optional[str] = None
    officialUrl: Optional[str] = None


class Project(BaseModel):
    projectId: str
    name: str
    description: str
    imageUrl: Optional[str] = None

    skills: List[Skill] = []

    repoUrl: Optional[str] = None
    demoUrl: Optional[str] = None

    createdAt: str
    updatedAt: str
