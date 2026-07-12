from pydantic import BaseModel

class FileSpec(BaseModel):

    path: str

    file_name: str

    description: str