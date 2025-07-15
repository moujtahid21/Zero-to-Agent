import os
from openai import OpenAI
from dotenv import load_dotenv

# --- 1 PERCEIVE: Load environment and configuration ---
print("Agent: Loading configuration...")
load_dotenv()

# Check if the API key is set
if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

client = OpenAI()
print("Agent: Configuration loaded")


# -- 2 THINK: Define the agent's core logic --
def run_agent_once(user_prompt):
    """
    Rungs the agent's thinking process for a single interaction
    """
    print(f"You: {user_prompt}")
    print("Agent: Thinking...")

    # The system message defines the agent's personality or role.
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant. You keep your answers concise and to the point."
    }

    user_message = {
        "role": "user",
        "content": user_prompt
    }

    try:
        # This is the core call to the LLM
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[system_message, user_message]
        )
        agent_reply = response.choices[0].message.content
        return agent_reply
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I ran into an error."


# -- 3 ACT: Main loop to interact with the agent --
def main_loop():
    """
    The main loop where the agent perceives input and acts
    """
    print("\n--AI Agent is running--")
    print("Say 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")

        # Perception: Check for exit condition
        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        # Think & Act
        agent_response = run_agent_once(user_input)
        print(f"Agent: {agent_response}")


if __name__ == "__main__":
    main_loop()
