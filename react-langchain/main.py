from typing import Union, List
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import AgentAction, AgentFinish
from langchain.agents.format_scratchpad import format_log_to_str
from callbacks import AgentCallbackHandler  # Ensure this is correctly implemented

load_dotenv()

@tool
def get_text_length(text: str) -> int:
    """Returns the length of the input text."""
    print(f"Calculating length of text: {text}")
    return len(text)

@tool
def write_poem_in_kanye_style(topic: str) -> str:
    """Writes a small poem in Kanye West style about a given topic."""
    print(f"Writing poem about: {topic}")
    # Replace the next line with actual API call to generate a poem
    poem = "This is a placeholder poem about " + topic
    return poem

def find_tool_by_name(tools: list[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"Tool with name {tool_name} not found")

if __name__ == "__main__":
    print("Start")
    user_topic = input("Please enter a topic for the poem: ")
    tools = [get_text_length, write_poem_in_kanye_style]

    template = """..."""  # Use the template from your previous code

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools), tool_names=", ".join([t.name for t in tools])
    )

    llm = ChatOpenAI(
        temperature=0, stop=["\nObservation"], callbacks=[AgentCallbackHandler()]  # Ensure callbacks are properly set up
    )
    intermediate_steps = []
    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_log_to_str(intermediate_steps),
        }
        | prompt
        | llm
        | {"str": StrOutputParser()}  # Adjust as needed for your parsing
    )

    task_description = f"Write a small poem in Kanye West style about {user_topic} and then count the length by characters."

    agent_step = None
    max_iterations = 3  # Limit iterations for debugging
    iteration_counter = 0

    while not isinstance(agent_step, AgentFinish) and iteration_counter < max_iterations:
        iteration_counter += 1
        agent_step: Union[AgentAction, AgentFinish] = agent.invoke(
            {
                "input": task_description,
                "agent_scratchpad": format_log_to_str(intermediate_steps),
            }
        )
        print("Agent Step: ", agent_step)

        if isinstance(agent_step, AgentAction):
            tool_name = agent_step.tool
            tool_to_use = find_tool_by_name(tools, tool_name)
            tool_input = agent_step.tool_input

            observation = tool_to_use.func(tool_input)
            print(f"Observation: {observation}")
            intermediate_steps.append((tool_name, tool_input, observation))

        if iteration_counter == max_iterations:
            print("Reached maximum iterations.")
            break

    if isinstance(agent_step, AgentFinish):
        print("Final Answer: ", agent_step.return_values)
