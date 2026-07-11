from app.models.architecture_response import (
    ArchitectureResponse
)

from app.prompts.architect_prompt import (
    architect_prompt
)

from app.services.llm_service import (
    LLMService
)


class ArchitectAgent:

    def __init__(self):

        llm = (
            LLMService()
            .get_llm()
        )

        self.llm = (
            llm.with_structured_output(
                ArchitectureResponse
            )
        )

    def run(
        self,
        requirement: str
    ):

        prompt = architect_prompt.format(
            requirement=requirement
        )

        return self.llm.invoke(prompt)