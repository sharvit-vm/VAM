from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser

from config import get_llm
from prompts.rag_prompt import get_rag_prompt
from schemas.response_schema import AnswerSchema


def format_docs(docs):
    context = ""

    for i, doc in enumerate(docs):
        source = doc.metadata.get("source", "unknown")

        context += (
            f"[Source {i+1} | {source}]\n"
            f"{doc.page_content}\n\n"
        )

    return context


def create_rag_chain(retriever):
    llm = get_llm()
    prompt = get_rag_prompt()

    parser = PydanticOutputParser(pydantic_object=AnswerSchema)

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
            "format_instructions": lambda _: parser.get_format_instructions()
        }| prompt | llm | parser
    )

    return chain