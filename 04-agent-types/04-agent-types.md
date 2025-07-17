# 4. 🎭 Types of AI Agents: A Look at the Different Roles
We've built a basic agent and learned about the frameworks that give them superpowers. Now, let's explore the "species" in the agent kingdom. Understanding these different types helps us choose the right design for the right problem.

The primary way to classify agents is by their intelligence and capabilities, ranging from simple reactive machines to complex learning systems.

### 1. Simple Reflex Agents:
These are the most basic types of agents. They make decisions based only on the current situation, ignoring past history completely. They operate on a simple "condition-action" or "if-then" rule.

- **Analogy**: A thermostat. If the current temperature is below the set point, it turns on the heat. It doesn't remember that it was cold an hour ago; it only knows what the temperature is right now.

- **How it Works**: It perceives its environment and acts according to a predefined set of rules.

- **Example**: Our first agent from lesson 2 was a simple reflex agent. It took our prompt and reacted to it without any memory of previous questions.

### 2. Model-Based Agents:
These agents are a step up from simple reflex agents. They maintain an internal "model" or state of how the world works. This allows them to handle situations where they can't see everything at once (partially observable environments).

- **Analogy**: A self-driving car changing lanes. It doesn't just see the car in front of it; it maintains an internal model of other cars' speeds and trajectories to predict where they will be in the next few seconds.

- **How it Works**: It uses its internal model of the world, combined with what it currently perceives, to make a decision.

- **Example**: A robot vacuum that remembers the layout of a room and keeps track of which areas it has already cleaned.

### 3. Goal-Based Agents:
Instead of just reacting, these agents have a specific goal to achieve. They can look ahead and choose from a sequence of actions that will lead them to their desired outcome. This involves basic planning and searching.

- **Analogy**: A GPS navigation app. You give it a destination (the goal), and it calculates the best sequence of turns to get you there.

- **How it Works**: It considers various action paths and selects the one that leads to the achievement of its goal state.

- **Example**: A chess-playing AI that plans several moves ahead to reach a checkmate position.

### 4. Utility-Based Agents:
These are more sophisticated goal-based agents. They are used when achieving a goal isn't enough; the quality of the outcome matters. They aim to maximize their "utility," which is a measure of "happiness" or success.

- **Analogy**: A GPS app that not only finds a route to your destination but finds the best route by weighing factors like traffic, tolls, and travel time. The route with the highest utility (e.g., fastest and cheapest) is chosen.

- **How it Works**: It evaluates different goal states based on a utility function and chooses the action path that leads to the state with the highest utility.

- **Example**: A financial trading agent that doesn't just aim to make a profit (the goal) but aims to maximize profit while minimizing risk (the utility).

### 5. Learning Agents:
Learning agents can improve their performance over time. They start with some initial knowledge and are ableto adapt and get better through experience. This is the foundation of most modern AI.

- **Analogy**: A person learning to play tennis. They start with basic knowledge but get better by practicing, getting feedback (seeing if the ball went in), and adjusting their technique.

- **How it Works**: It has a "learning element" that critiques its own performance and modifies its decision-making rules for better results in the future.

- **Example**: A movie recommendation system like Netflix's, which learns your preferences over time based on what you watch and rate.

### Connecting to Modern Frameworks
So, where do frameworks like CrewAI and KaibanJS fit in? They excel at helping us build agents that are a powerful blend of these types, especially what we can call Tool-Using Agents.

A Tool-Using Agent is often a Goal-Based or Utility-Based Agent that has been given access to external tools (APIs, web search, databases, etc.). The framework manages the complex logic of deciding which tool to use and when to use it to achieve a goal.

For instance, a "researcher" agent built with CrewAI is:

- **Goal-Based**: Its goal is to write a report.

- **Model-Based**: It keeps track of the information it has found.

- **Tool-Using**: It uses a web search tool to find information.

- **Learning (Potentially)**: Over time, its underlying LLM can be fine-tuned to become better at research tasks.

### What's Next?
Now that we understand the different roles agents can play, a crucial question arises: How does a dynamic, thinking agent differ from a simple, predefined script? In our next lesson, we'll break down the critical differences between a Workflow vs. an Agent.