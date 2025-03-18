from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_file(data: str, filename: str = "output.md"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"# Research Report\n\n## {timestamp}\n\n{data}\n\n"
    with open(filename, "w") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_to_markdown_file",
    func=save_to_file,
    description="Save the data to a markdown file",
)

search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="Search",
    description="Search the web for information",
    func=search.run,
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2000)

wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
