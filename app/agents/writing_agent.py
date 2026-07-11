from app.services.llm_service import (
    LLMService
)

from app.prompts.writer_prompt import (
    writer_prompt
)


class WritingAgent:

    def __init__(self):

        self.llm = (
            LLMService()
            .get_llm()
        )

    def run(
        self,
        file_name: str,
        description: str
    ):

        prompt = writer_prompt.format(
            file_name=file_name,
            description=description
        )

        response = self.llm.invoke(
            prompt
        )

        return response.content