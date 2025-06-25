# 🚀 LangGraph Exercises

A collection of exercises and implementations from the [FreeCodeCamp LangGraph course](https://www.youtube.com/watch?v=jGg_1h0qzaM) taught by Vaibhav Mehra.


## 📚 About the Course

This repository contains exercises and solutions from the FreeCodeCamp course on LangGraph. LangGraph is a library for building stateful, multi-actor applications with LLMs using graphs. It extends the LangChain framework to allow for more complex agent workflows and conversations.

- **Course Link**: [LangGraph - Build Multi-Agent Systems (FreeCodeCamp)](https://www.youtube.com/watch?v=jGg_1h0qzaM)
- **Original Course Repo**: [LangGraph-Course-freeCodeCamp by Vaibhav Mehra](https://github.com/iamvaibhavmehra/LangGraph-Course-freeCodeCamp)

## 🗂️ Repository Structure

- **Lessons/**: Contains the code examples from the course lessons
  - Basic graph concepts & visualization
  - Node implementation
  - Conditional flows
  - Looping structures

- **exercises/**: My solutions to the practice exercises
  - Exercise 1: Basic node creation and message passing
  - Exercise 2: Mathematical operations within nodes
  - Exercise 3: Sequential node execution and string formatting
  - Exercise 4: Conditional routing with multiple operations
  - Exercise 5: Interactive number guessing game with state management

- **Agents/**: Implementation of various LLM-powered agents
  - Agent1: Simple conversational agent
  - Agent2: Conversational agent with memory
  - Agent3: ReAct agent with math and currency tools
  - Agent4: Document editing assistant
  - Agent5: RAG-based agent for querying financial documents

## 💻 Key Technologies Used

- **LangGraph**: For building stateful agent workflows
- **LangChain**: Core framework for LLM applications
- **Groq**: Fast LLM API for inference
- **ChromaDB**: Vector database for retrieval-augmented generation
- **HuggingFace Embeddings**: For text embeddings
- **PyPDF**: For PDF document processing

## 🛠️ Setup and Usage

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/Langraph-excercises.git
   cd Langraph-excercises
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   # or
   pip install -r requirements.txt
   ```

3. **Setup your API keys**
   - Create a `.env` file in the root directory
   - Add your API keys (Groq API key for LLM access)
   ```
   GROQ_API_KEY=your-api-key-here
   ```

4. **Run the examples**
   ```bash
   python Lessons/lesson.py
   python excercises/excercise1.py
   python Agents/Agent1.py
   ```

## 🌟 What I've Learned

- Building stateful conversation flows using graph structures
- Managing complex agent interactions and state
- Implementing ReAct agents with tool utilization
- Creating RAG systems with document retrieval
- Using conditional and loop patterns in LLM applications
- Handling various types of user inputs and agent responses

## 📝 License

This project is based on the materials from the FreeCodeCamp course by Vaibhav Mehra, used for educational purposes.

## 🙏 Acknowledgements

- [FreeCodeCamp](https://www.freecodecamp.org) for the free educational content
- [Vaibhav Mehra](https://github.com/iamvaibhavmehra) for creating the excellent tutorial
- [LangChain](https://github.com/langchain-ai) team for the fantastic libraries
