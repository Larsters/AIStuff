import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate  
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import get_linkedin_profile_info
from agents.linkedin_lookup_agents import lookup as linkedin_lookup_agent


if __name__ == '__main__':

    load_dotenv()
    print ('Hello, Chain!')

    linkedin_profile_url = linkedin_lookup_agent(name = "Vasiliy Klyosov Mercedes-Benz")

    summary_template = """
    given the info {info} about a person I want you to create: 
    1. a short summary of the person from his linkedin
    2. 2 short interesting facts about the person
    3. Should he be hired to work in a company? Which role would suit him best?
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template)

    llm = ChatOpenAI(temperature = 0, model_name = "gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = get_linkedin_profile_info(
        linkedin_profile_url= linkedin_profile_url
        )

    print(chain.invoke(info=linkedin_data, input = summary_prompt_template.format_prompt(info=linkedin_data)))
    