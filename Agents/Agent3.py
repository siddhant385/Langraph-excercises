#This is the react Agent that can do math operations and currency conversion

from dotenv import load_dotenv  
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage,ToolMessage,SystemMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
import re
import requests

load_dotenv()


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]


@tool
def currency_converter_tool(query: str) -> str:
    """This is a currency converter tool that converts an amount from one currency to another."""
    pattern1 = r"convert\s+([\d.]+)\s*(\w{3})\s+to\s+(\w{3})"
    pattern2 = r"([\d.]+)\s*(\w{3})\s+to\s+(\w{3})"
    match = re.search(pattern1, query.lower()) or re.search(pattern2, query.lower())

    if not match:
        return "Please use format like: convert 100 INR to USD"
    amount, from_currency, to_currency = match.groups()
    amount = float(amount)
    try:
        response = requests.get(f"https://open.er-api.com/v6/latest/{from_currency.upper()}")
        data = response.json()
        if "rates" not in data or to_currency.upper() not in data["rates"]:
            return f"Currency {to_currency.upper()} not supported."
        rate = data["rates"][to_currency.upper()]
        converted = round(amount * rate, 4)
        return f"{amount} {from_currency.upper()} = {converted} {to_currency.upper()}"
    except Exception as e:
        return f"Error during conversion: {str(e)}"

@tool
def add(a: int, b:int):
    """This is an addition function that adds 2 numbers together"""

    return a + b 

@tool
def subtract(a: int, b: int):
    """Subtraction function"""
    return a - b

@tool
def multiply(a: int, b: int):
    """Multiplication function"""
    return a * b
    

tool = [currency_converter_tool,add,subtract,multiply]

model = ChatGroq(
    model="qwen/qwen3-32b"
).bind_tools(tool)


def model_call(state):
    system_prompt = SystemMessage(
        content="You are my helpful assistant that can answer my query with best of your ability. "
    )
    response= model.invoke([system_prompt]+ state["messages"])
    return{"messages": [response]}

def should_continue(state):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls: 
        return "end"
    else:
        return "continue"
    
graph = StateGraph(AgentState)
graph.add_node("agent",model_call)

tool_node = ToolNode(tools=tool)
graph.add_node("tools",tool_node)

graph.set_entry_point("agent")

graph.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)
graph.add_edge("tools", "agent")

app=graph.compile()

def print_stream(stream):
    for step in stream:
        print("🔁 Step:")
        for msg in step["messages"]:
            print("🔹", type(msg).__name__)
            try:
                msg.pretty_print()
            except:
                print(msg)
        print("-" * 50)

inputs = {"messages": [("user", "Add 4000rs + 12dollars and then multiply the result by 6 and then subtract 340 rupees and give answer in USD . Also tell me a joke please.")]}
print_stream(app.stream(inputs, stream_mode="values"))