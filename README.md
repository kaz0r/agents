# Research agent
Simple research agent using Anthropics API and langchain

# Installation
Create a virtual environment
```
conda create -n research_agent python=3.12 && conda activate research_agent
```
Install dependencies
```
pip install -r requirements.txt
```

# Usage
run the main file
```
python main.py
```

# Example input
research the current OSINT SaaS platforms out there and what their key selling points are and how we can create a new one that imrpoves the current ones. Also take into account sources that explain what would be nice to have, what the current ones fail at, their pricing. Keep in mind that i only want you to research the ones utilizing AI in some way. I am currently working on a system that aggregates news from news sources and social media and analyzes these new events such as when bombings happen, fires, natural disasters, murders etc and creating an event thread using RAG kind of like dataminr does. Look up all the platforms similar to this and dataminr. Some other key platforms i know about are pentester.com, palantir etc. can you research more compeptitors for me as well?