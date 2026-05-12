from typing import Dict, Any 
from andromeda.core.workflow import WorkflowBuilder 
from andromeda import BaseMessage
from typing import TypedDict 

class StateModel(TypedDict):
    messages: list[BaseMessage] 
    query: str
    raw: list[str]
    summary: str
    status: str        
    handled: bool      
    should_fail: bool  

def risky_task(state: Dict[str, Any]) -> Dict[str, Any]: 
    if state.get("should_fail"):
        raise RuntimeError("Task failed")
    return {"status":"ok"}

def on_failure(state: Dict[str, Any]) -> Dict[str, Any]: 
    return {"status":"failed","handled": True}

def on_success(state:Dict[str,Any])->Dict[str,Any]:
    return {"status":"completed"}

wf = WorkflowBuilder(name ="RiskyWorkflow",state_schema = StateModel)
(
    wf.start("risky_task").run(risky_task).if_fails().goto("failure_handler").if_succeeds().goto("success_handler").then("failure_handler").run(on_failure).then("success_handler").run(on_success)
)

final_state = wf.execute(state = {"should_fail": True})
print(final_state["status"], final_state.get("handled"))