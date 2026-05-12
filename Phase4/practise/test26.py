from typing import Dict, Any
from andromeda.core.workflow import WorkflowBuilder
from andromeda import HumanMessage, BaseMessage
from andromeda.core import Agent
from andromeda.config import AgentConfig, ModelConfig
from typing import TypedDict
from dotenv import load_dotenv 
load_dotenv()

class StateModel(TypedDict):
    messages: list[BaseMessage] # is mandatory field for agents
    query: str
    raw: list[str]
    summary: str

def ingest(state: Dict[str, Any]) -> Dict[str, Any]:
    query = state.get("query", "")
    return {"raw": [f"Result for {query} from web", f"Result for {query} from docs"]}

def summarize(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = Agent(AgentConfig(
        name="summarizer",
        model=ModelConfig(name="gpt-4o-mini", provider="openai"),
        prompt="Summarize the following text:",
    ))
    messages = [HumanMessage(content="\n".join(state["raw"]))]
    result = agent.invoke(messages)
    text = result[-1].content
    return {"summary": text, "messages": result}

workflow = WorkflowBuilder(name="SimpleLinearWorkflow", state_schema=StateModel)
(
    workflow
    .start("ingest").run(ingest)
    .finish("summarize").run(summarize)
)

result = workflow.execute(state={"query": "Andromeda features"})
print("Summary:", result["summary"])