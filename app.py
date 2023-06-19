import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

os.environ["OPENAI_API_KEY"] = "Open_API_Key"

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    return llm_chain
