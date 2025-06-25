from langgraph.graph import StateGraph
import math
from typing import TypedDict,List

class AgentState(TypedDict):
    name:str
    value:List[int] 
    operation:str
    result:str

def process_result(state):
    if state["operation"] == "*":
        answer = math.prod(state["value"])
    else:
        answer = sum(state["value"])
    state["result"] = f"Hii {state["name"]}, your answer is {answer}"
    return state

graph = StateGraph(AgentState)

graph.add_node("Processor",process_result)

graph.set_entry_point("Processor")
graph.set_finish_point("Processor")

app = graph.compile()

res = app.invoke({
    "name": "Jack Sparrow",
    "value":[1,2,3,4],
    "operation":"+"
})
print(res)