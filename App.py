from tavily import TavilyClient
import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class AgentState(TypedDict):
    query: str
    decision: str
    final_result: str

llm = ChatOpenAI(model="gpt-4o-mini")
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_tool(state):
    print("Running web search...")
    try:
        result = tavily.search(query=state["query"], max_results=3)
        content = ""
        for r in result["results"]:
            content += f"{r['content']}\n\n"
        if "weather" in state["query"]:
            prompt = f"""
                Extract weather details and format like this:
                🌍 Location:
                🌡️ Temperature:
                ☁️ Condition:
                💧 Humidity:
                💨 Wind:

                Data:{content}
                Donot give back the data that I'm passing.
            """
        else:
            prompt = f"""
                Convert this into a clean and readable answer
                {content}
            """
        formatted = llm.invoke(prompt)
        return {
            "final_result": formatted.content
        }
    except:
        return {
            "final_result": "⚠️ Search Failed, Try again lated"
        }

def calculator_tool(state):
    try:
        result = eval(state["query"])
        return {
            "final_result": result
        }
    except:
        return {
            "final_result": "Invalid Calculation"
        }

def summarize_tool(state):
    prompt = f"""
        Summarize this in 3 concise lines:
        {state['query']}
    """
    response = llm.invoke(prompt)
    return {
        "final_result": response.content
    }

def direct_answer(state):
    response = llm.invoke(state["query"])
    return {
        "final_result": response.content
    }

def decision_tool(state):
    prompt = f"""
        Decide the best tool:
        Query: {state['query']}
        options: 
        - "search" ---> current events / factual / latest info
        - "calculator" ---> math
        - "summarizer" ---> summarizing text
        - "answer" ---> general knowledge
        Return ONLY one word.
        Also if I give you the calculation in the textual formal then calculate it and then give me the result in one word.
    """
    response = llm.invoke(prompt)
    str = response.content.strip().lower()
    if "search" in str:
        return {
            "decision": "search"
        }
    elif "calculator" in str:
        return {
            "decision": "calculator"
        }
    elif "summarizer" in str:
        return {
            "decision": "summarizer"
        }
    else:
        return {
            "decision": "answer"
        }

def route(state):
    return state["decision"]

builder = StateGraph(AgentState)

builder.add_node("search", search_tool)
builder.add_node("calculator", calculator_tool)
builder.add_node("answer", direct_answer)
builder.add_node("summarizer", summarize_tool)
builder.add_node("decide", decision_tool)


builder.add_edge(START, "decide")
builder.add_conditional_edges(
    "decide",
    route,
    {
        "summarizer": "summarizer",
        "answer": "answer",
        "search": "search",
        "calculator": "calculator"
    }
)
builder.add_edge("summarizer", END)
builder.add_edge("answer", END)
builder.add_edge("search", END)
builder.add_edge("calculator", END)

graph = builder.compile()

st.set_page_config(page_title="Info-Pilot", layout="centered")

st.title("🤖 Info Pilot (Multi-Tool Web Search)")
st.write("Ask anything : math, summaries, or real-time info 🌏")

query = st.text_area("Enter your query : ")
if st.button("Run Agent"):
    if not query.strip():
        st.warning("please enter a query")
    else:
        with st.spinner("Thinking..."):
            result = graph.invoke(
                {
                    "query": query,
                    "decision": "",
                    "final_result": ""
                }
            )
        st.success("Done!")

        st.subheader("🧠 Final Answer : ")
        st.write(result["final_result"])
