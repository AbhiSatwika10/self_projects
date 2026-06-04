from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def coder_agent(plan):
    prompt = f"Generate production-ready Python code for: {plan}"
    response = llm.invoke(prompt)
    return response.content
