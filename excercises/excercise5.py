from langgraph.graph import StateGraph,START,END
from typing import TypedDict,List
import random

class AgentState(TypedDict):
    name: "str"
    target_number: int
    guesses: List[int]
    attempts: int
    hint : str
    lower_bound:int
    upper_bound:int

def setup_node(state):
    """Initialize the game with a random target number"""
    state["name"] = f"Welcome, {state['name']}!"
    state["lower_bound"] = 1 
    state["upper_bound"] = 20 
    state["target_number"] = random.randint(state['lower_bound'],state['upper_bound'])
    state['guesses'] = []
    state["attempts"] = 0
    state["hint"] = "Game started! Try to guess the number."
    
    print(f"{state['name']} The game has begun. I'm thinking of a number between 1 and 20.")
    return state

def guess_node(state):
    possible_numbers = [i for i in range(state['lower_bound'],state['upper_bound']+1) if i not in state["guesses"]]
    if possible_numbers:
        guess = random.choice(possible_numbers)
    else:
        guess = random.randint(state["lower_bound"], state["upper_bound"])
    state["guesses"].append(guess)
    state['attempts'] += 1
    print(f"Attempt {state['attempts']}: Guessing {guess} (Current range: {state['lower_bound']}-{state['upper_bound']})")
    return state

def hint_node(state):
    """Here we provide a hint based on the last guess and update the bounds"""
    latest_guess = state["guesses"][-1]
    target = state["target_number"]
    
    if latest_guess < target:
        state["hint"] = f"The number {latest_guess} is too low. Try higher!"
        
        state["lower_bound"] = max(state["lower_bound"], latest_guess + 1)
        print(f"Hint: {state['hint']}")
        
    elif latest_guess > target:
        state["hint"] = f"The number {latest_guess} is too high. Try lower!"
      
        state["upper_bound"] = min(state["upper_bound"], latest_guess - 1)
        print(f"Hint: {state['hint']}")
    else:
        state["hint"] = f"Correct! You found the number {target} in {state['attempts']} attempts."
        print(f"Success! {state['hint']}")
    
    return state

def should_continue(state):
    guess = state["guesses"][-1]
    target = state['target_number']
    if guess == target:
        print(f"GAME OVER: Number found!")
        return "end"
    elif state["attempts"] >= 7:
        print(f"GAME OVER: Maximum attempts reached! The number was {state['target_number']}")
        return "end"
    else:
        print(f"CONTINUING: {state['attempts']}/7 attempts used")
        return "continue"

graph = StateGraph(AgentState)

graph.add_node("setup",setup_node)
graph.add_node("guess",guess_node)
graph.add_node("hint_node",hint_node)

graph.add_edge("setup","guess")
graph.add_edge("guess","hint_node")
graph.add_conditional_edges(
    "hint_node",
    should_continue,
    {
        "end":END,
        "continue":"guess"
    }

)
graph.set_entry_point("setup")


app = graph.compile()

result = app.invoke({"name": "Student", "guesses": [], "attempts": 0, "lower_bound": 1, "upper_bound": 20})
print(result)