# 2. 🏗️ Build an Agent from Scratch
Welcome to the second step of our "Zero to Agent" series! The theory is great, but nothing beats writing actual code. Today, we will build a foundational AI agent. It will be simple, but it will contain the core loop that powers even the most complex agentic systems.

### What is an Agent (in simple terms)?
At its heart, an AI agent operates on a simple, continuous loop:

1. Perceive: The agent takes in information about its environment. This could be user input, data from a sensor, or information from a website.

2. Think: The agent processes this information to make a decision. This is the "brain" of the operation, where the Large Language Model (LLM) comes into play.

3. Act: The agent performs an action based on its decision. This could be writing a response, calling an API, or controlling a device.

Our first agent will follow this exact pattern. It will perceive a text prompt from you, think using an LLM to generate a response, and act by printing that response to the console.

**Prerequisites**
For this tutorial, we'll use Python, as it's the most common language for AI development and has excellent library support.

1. Python 3.8+: Make sure you have Python installed.

2. OpenAI API Key: Our agent's "brain" will be an OpenAI model (like GPT-3.5 Turbo).

    - Go to the OpenAI Platform to sign up and get your API key.
    
    - Important: Keep your API key secret! We will use environment variables to handle it securely.
## Step 1: Setting up your project
Let's create a clean workspace for our new agent.
1. Inside your `zero-to-agent` project folder, create a new directory for this lesson:
```bash
mkdir 02-first-agent
cd 02-first-agent
```
2. Install the necessary python libraries: openai to talk to the LLM and python-dotenv to manage our secret API key.
```bash
pip install openai python-dotenv
```
3. Create two files in this directory:
- .env: This file will store our OpenAI API key.
- main.py: This will be our main script where we build the agent.
Your folder should look like this:
```
zero-to-agent/
├── 02-first-agent/
    ├── .env
    ├── main.py
```
### Step 2: Storing your API Key
Open  the `.env` file and add your OpenAI API key like this:
```Ini, TOML
OPENAI_API_KEY=your_openai_api_key_here
```
By using this file, we keep our secret key ouf of our main code.

### Step 3: Writing the Agent Code
Now for the fun part! Open `main.py` and let's write our agent's logic, piece by piece.
```python
# main.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# --- 1. PERCEIVE: Load environment and configuration ---
print("Agent: Loading configuration...")
load_dotenv() # This line loads the .env file

# Check if the API key is set
if "OPENAI_API_KEY" not in os.environ:
    print("Error: OPENAI_API_KEY is not set in the .env file.")
    exit()

# Initialize the OpenAI client
# The client automatically reads the OPENAI_API_KEY from the environment
client = OpenAI()
print("Agent: Configuration loaded.")


# --- 2. THINK: Define the agent's core logic ---
def run_agent_once(user_prompt):
    """
    Runs the agent's thinking process for a single interaction.
    """
    print(f"You: {user_prompt}")
    print("Agent: Thinking...")

    # The system message defines the agent's personality or role.
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant. You keep your answers concise and to the point."
    }

    # The user message is the input from the user.
    user_message = {
        "role": "user",
        "content": user_prompt
    }
    
    try:
        # This is the core call to the LLM
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # You can swap this for "gpt-4" if you have access
            messages=[system_message, user_message]
        )
        
        # Extract the agent's reply from the response
        agent_reply = response.choices[0].message.content
        return agent_reply

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I ran into an error."


# --- 3. ACT: The main interaction loop ---
def main_loop():
    """
    The main loop where the agent perceives input and acts.
    """
    print("\n--- AI Agent is running ---")
    print("Say 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        # Perception: Check for exit condition
        if user_input.lower() == 'exit':
            print("Agent: Goodbye!")
            break
        
        # Think & Act
        agent_response = run_agent_once(user_input)
        print(f"Agent: {agent_response}")

# Entry point of the script
if __name__ == "__main__":
    main_loop()
```
### Step 4: Running Your Agent
You're all set! Go to your terminal, make sure you are in the `02-first-agent` directory, and run the script:
```bash
python main.py
```
You should see the agent load its configuration and then prompt you for input. Try asking it a few questions!
**Example interaction**:
```
$ python main.py
Agent: Loading configuration...
Agent: Configuration loaded.

--- AI Agent is running ---
Say 'exit' to end the conversation.
You: What is the capital of France?
Agent: The capital of France is Paris.
You: Can you tell me a joke?
Agent: Why did the scarecrow win an award? Because he was outstanding in his field!
You: exit
Agent: Goodbye!
```

### Congratulations!
You have  successfully built and run your first AI agent. You implemented the complete Perceive-Think-Act loop:
- **Perceive**: Your `input("You: ")` captures the user's prompt.

- **Think**: The `client.chat.completions.create()` call sends the prompt to the LLM and gets a decision (the response). The "system message" gave the agent its basic instructions.

- **Act**: The `print(f"Agent: {agent_response}")` performs the action of communicating the result.

The simple structure is the foundation we will build upon. In our next session, we'll explore AI Agent Frameworks -- tools that take this basic concept and make it vastly more powerful and flexible. But for now, you've got the basics down!