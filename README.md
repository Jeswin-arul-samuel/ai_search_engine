# AI Search Engine

An intelligent search engine powered by Zero-shot ReAct agents that combines multiple knowledge sources (Wikipedia, ArXiv, Google Search) to provide comprehensive, AI-synthesized answers.

## Features

- **Multi-Source Search**: Queries Wikipedia, ArXiv, and Google Search simultaneously
- **ReAct Agent**: Uses reasoning + acting pattern for intelligent query routing
- **AI Synthesis**: Combines results from multiple sources into coherent answers
- **Streamlit UI**: Clean, interactive web interface

## Tech Stack

- **Framework**: LangChain
- **LLM**: OpenAI GPT
- **Tools**: Wikipedia API, ArXiv API, SerpAPI (Google Search)
- **Frontend**: Streamlit
- **Language**: Python

## Architecture

```
User Query
    │
    ▼
┌─────────────────┐
│  ReAct Agent    │
│  (Zero-shot)    │
└────────┬────────┘
         │
    ┌────┴────┬────────────┐
    ▼         ▼            ▼
┌───────┐ ┌───────┐ ┌──────────┐
│Wikipedia│ │ ArXiv │ │ Google   │
└───────┘ └───────┘ └──────────┘
    │         │            │
    └────┬────┴────────────┘
         ▼
┌─────────────────┐
│  AI Synthesis   │
└─────────────────┘
         │
         ▼
    Final Answer
```

## Installation

```bash
# Clone the repository
git clone https://github.com/Jeswin-arul-samuel/ai_search_engine.git
cd ai_search_engine

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env
```

## Environment Variables

```
OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_serpapi_key
```

## Usage

```bash
streamlit run app.py
```

## How It Works

1. **Query Analysis**: The ReAct agent analyzes the user's question
2. **Tool Selection**: Decides which sources to query based on the question type
3. **Information Retrieval**: Fetches relevant data from selected sources
4. **Synthesis**: Combines and summarizes information into a coherent response

## Use Cases

- Research questions requiring academic sources
- General knowledge queries
- Current events and news
- Technical documentation lookup

## License

MIT

## Author

**Jeswin Arul Samuel**
- [LinkedIn](https://www.linkedin.com/in/jeswinarul)
- [Portfolio](https://portfolio-jeswin.vercel.app)
- [GitHub](https://github.com/Jeswin-arul-samuel)
