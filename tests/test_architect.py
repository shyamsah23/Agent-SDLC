from app.agents.architect_agent import (
    ArchitectAgent
)

agent = ArchitectAgent()

result = agent.run(
    "Build Library Management System"
)

print(result)