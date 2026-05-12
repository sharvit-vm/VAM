from typing import Dict, Any
from andromeda.core.workflow import WorkflowBuilder, task, conditional, parallel

def fetch_articles(state: Dict[str, Any]) -> Dict[str, Any]:
    return {"articles": [f"Article about {state['query']} - A", f"Article about {state['query']} - B"]}

def filter_relevant(state: Dict[str, Any]) -> Dict[str, Any]:
    articles = state["articles"]
    return [a for a in articles if "Article" in a]

def summarize_list(state: Dict[str, Any]) -> Dict[str, Any]:
    articles = state["articles"]
    return {"summary": " | ".join(articles)}

flow = (
    fetch_articles
    >> filter_relevant
    >> conditional(
        true_branch=summarize_list,
        false_branch=lambda state: {"summary": "No articles found."},
        condition=lambda state: len(state["articles"]) > 0,
    )
)

builder = WorkflowBuilder.from_expression(flow, name="ArticlePipeline")
summary = builder.execute(state={"query": "Andromeda workflows"})
print(summary)