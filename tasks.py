from crewai import Task
from tools import tool
from agents import financial_analyst,market_research_analyst,reporting_analyst

#3 Tasks would be carried out by different agents, namely Finacial analysis, Market analysis, Report writing
#Financial Analysis
financial_analysis=Task(
        description="Analyze the financial performance of {company}",
        expected_output="A detailed financial report including key financial ratios, trends, and forecasts",
        tools=[tool],
        agent=financial_analyst,

) 

#Market Analysis
market_analysis=Task(
        description="Analyze market trends and competitive landscape for {company}",
        expected_output="A comprehensive market research report detailing market trends, consumer behavior, and competitive analysis",
        tools=[tool],
        agent=market_research_analyst,

) 

    #Report Wriring
reporting_analysis= Task(
        description="Compile and synthesize data from financial and market research analysts into a comprehensive report",
        expected_output="A detailed 2 page report that combines financial performance analysis with market trends and competitive analysis for {company}, all important findings should be highlighted",
        tools=[tool],
        agent=reporting_analyst,
        async_execution=False,
        

) 