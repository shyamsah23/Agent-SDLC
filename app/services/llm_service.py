import os

from dotenv import load_dotenv

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

load_dotenv()


class LLMService:

    def __init__(self):

        self.llm = (
            ChatGoogleGenerativeAI(
                model="gemini-2.5-flash-lite",
                temperature=0
            )
        )

    def get_llm(self):

        return self.llm