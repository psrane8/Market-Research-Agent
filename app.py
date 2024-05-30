from crewai import Crew,Process
from agents import reporting_analyst,market_research_analyst,financial_analyst
from tasks import financial_analysis,reporting_analysis,market_analysis
import streamlit as st




#Defining the crew comprising of different agents
crew = Crew(
    agents=[financial_analyst, market_research_analyst, reporting_analyst],
    tasks=[financial_analysis,market_analysis,reporting_analysis],
    process=Process.sequential,
    verbose=2
)


result = crew.kickoff(inputs={"company": "Vissco" })
print(result)