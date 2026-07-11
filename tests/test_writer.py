from app.agents.writing_agent import (
    WritingAgent
)

agent = WritingAgent()

result = agent.run(
    file_name="Book.java",
    description="""
    Represents a library book
    """
)

print(result)

