import streamlit as st
import re
import sys
from crewai import Crew,Process
import os
from agents import reporting_analyst,market_research_analyst,financial_analyst
from tasks import reporting_analysis,market_analysis,financial_analysis

# Used to stream sys output on the streamlit frontend
class StreamToContainer:
    def __init__(self, container):
        self.container = container
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  
        self.color_index = 0  
    
    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            # Apply different color and switch color index
            self.color_index = (self.color_index + 1) % len(self.colors)  # Increment color index and wrap around if necessary

            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "Financial  Analyst" in cleaned_data:
            cleaned_data = cleaned_data.replace("Financial  Analyst", f":{self.colors[self.color_index]}[Financial  Analyst]")
        if "Market Research Analyst" in cleaned_data:
            cleaned_data = cleaned_data.replace("Market Research Analyst", f":{self.colors[self.color_index]}[Market Research Analyst]")
        if "Reporting Analyst" in cleaned_data:
            cleaned_data = cleaned_data.replace("Reporting Analyst", f":{self.colors[self.color_index]}[Reporting Analyst]")
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.container.markdown(''.join(self.buffer) , unsafe_allow_html=True)
            self.buffer = []
    



st.header("Financial & Market Research Multi-Agent")
st.subheader("Generate a Financial and Market Research Analysis Report!",divider="rainbow",anchor=False)

with st.form("form"):
    company=st.text_input("Enter the name of the Company",key="company")
    submitted=st.form_submit_button("Submit")


    
if submitted:
    with st.status("🤖 **Agents at work...**",expanded=True,state="running") as status:
        with st.container(height=300):
            sys.stdout = StreamToContainer(st)
            #Defining the crew comprising of different agents
            crew = Crew(
            agents=[financial_analyst, market_research_analyst, reporting_analyst],
            tasks=[financial_analysis,market_analysis,reporting_analysis],
            process=Process.sequential,
            verbose=2)
            result=crew.kickoff(inputs={"company":company})
        


        status.update(label="✅ Your Report is ready",state="complete", expanded=False) 
    st.subheader("Financial and Market Research Report is ready!", anchor=False, divider="rainbow")
    st.markdown(result)


