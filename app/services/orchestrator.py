from app.agents.architect_agent import (
    ArchitectAgent
)

from app.agents.writing_agent import (
    WritingAgent
)

from app.tools.file_tools import (
    FileTools
)


class Orchestrator:

    def __init__(self):

        self.architect = (
            ArchitectAgent()
        )

        self.writer = (
            WritingAgent()
        )

    def run(
        self,
        requirement: str
    ):

        architecture = (
            self.architect.run(
                requirement
            )
        )

        project_name = (
            architecture.project_name
        )

        for file in architecture.files:

            code = self.writer.run(
                file.file_name,
                file.description
            )

            file_path = (
                f"generated_projects/"
                f"{project_name}/"
                f"{file.path}/"
                f"{file.file_name}"
            )

            FileTools.create_file(
                path=file_path,
                content=code
            )

        return architecture