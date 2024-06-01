from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import os
load_dotenv()


os.environ["SERPER_API_KEY"]=os.environ.get("SERPER_API_KEY")

#Tool for searching on Google
tool=SerperDevTool()