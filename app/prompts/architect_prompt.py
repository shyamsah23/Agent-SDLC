from langchain_core.prompts import PromptTemplate

architect_prompt = PromptTemplate(
    input_variables=[
        "requirement"
    ],
    template="""
You are a senior software architect.

Requirement:

{requirement}

Generate:

1. Project name
2. Required files
3. Description of each file

Return structured response.
"""
)