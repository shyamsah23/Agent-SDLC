from langchain_core.prompts import (
    PromptTemplate
)

writer_prompt = PromptTemplate(
    input_variables=[
        "file_name",
        "description"
    ],
    template="""
You are a senior Java developer.

Generate production-quality Java code.

File Name:
{file_name}

Description:
{description}

Requirements:

1. Return ONLY code
2. No markdown
3. No explanations
4. Generate complete compilable code
"""
)