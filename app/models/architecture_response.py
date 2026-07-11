from pydantic import BaseModel
from typing import List
from app.models.file_spec import(FileSpec)

class ArchitectureResponse(BaseModel):
    project_name: str

    files: List[FileSpec]