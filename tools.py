from langchain_community import tool
from langchain_community.tools import DuckDuckGoSearchRun

@tool
def save_to_file(content:str,filepath:str):
    """
    Save provided text content to a local file. 'filepath' is the path where file will be saved & 'content' will be the content that will be saved in the file.
    """

    # When langchain doesn't has the logic pre built like of saving all content, we then make our own logic
    with open(filepath,'a') as file:
        file.write(f'{content}\n')
        


search=DuckDuckGoSearchRun()
tools=[save_to_file, search]