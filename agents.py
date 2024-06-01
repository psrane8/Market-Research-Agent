from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI
from tools import tool

load_dotenv()
import asyncio

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
#Defining the base llm model
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           google_api_key=os.environ.get("GOOGLE_API_KEY"),
                           temperature=0.5,
                           verbose=True)


#Market research analyst agent
market_research_analyst= Agent(
role="Market Research Analyst",
goal="Provide insights about {company} through market analysis",
verbose=True,
memory=True,
backstory=("""You are a Market Research Analyst conducting research on {company}.
Your main role is to gather and analyze market data to understand market trends, consumer behavior, and competitive dynamics.
Currently, you are working on a project to assess the market potential for {company} and analyze the competitive landscape."""),
tools=[tool],
llm=llm,
#max_rpm=15,
allow_delegation=True)

#Financial analyst agent
financial_analyst= Agent(
role="Financial  Analyst",
goal="Provide comprehensive financial insights about {company}",
verbose=True,
memory=True,
backstory=("""You are a Financial Analyst conducting research on {company}.
Your primary responsibility is to analyze financial data and provide insights
that support strategic decision-making. 
Currently, you are working on evaluating {company}'s quarterly performance and preparing financial forecasts for the upcoming year."""),
tools=[tool],
llm=llm,
#max_rpm=15,
allow_delegation=True)

#Reporting analyst age
reporting_analyst= Agent(
    role="Reporting  Analyst",
    goal="Create sophisticated reports based on the findings from financial and market research analysts about {company}",
    verbose=True,
    memory=True,
    backstory=("""You are a Report Analyst working on research for {company}.
    Your primary responsibility is to compile and synthesize data from the Financial Analyst and Market Research Analyst into 
    comprehensive and sophisticated reports. These reports are used to support strategic business decisions and communicate findings 
    to stakeholders.Currently, you are working on a detailed report that combines financial performance analysis with market trends 
    to provide a holistic view of {company}'s current standing and future prospects."""),
    tools=[tool],
    llm=llm,
    #max_rpm=15,
    allow_delegation=False)
