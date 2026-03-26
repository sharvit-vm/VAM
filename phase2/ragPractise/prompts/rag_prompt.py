from langchain_core.prompts import ChatPromptTemplate

def get_rag_prompt():

    template = """
You are a helpful assistant.

Answer the question using ONLY the provided context.

If the answer is not in the context, say:
"I don't know based on the document."

Return your response in the following JSON format:
{format_instructions}

Context:
{context}

Question:
{question}
"""

    return ChatPromptTemplate.from_template(template)