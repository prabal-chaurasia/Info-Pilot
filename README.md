# 🤖 Info Pilot — Multi-Tool AI Agent

Info Pilot is a Streamlit app powered by **LangGraph** that reads your query, decides which tool fits best, and routes it there automatically. Ask it for live web info, math, summaries, or general knowledge.

## ✨ Features

- **Smart routing**: an LLM-based decision node picks the right tool for each query
- **Web search**: real-time answers via the Tavily API, cleaned into a readable response (with a special format for weather queries)
- **Calculator**: safe math evaluation (no `eval`)
- **Summarizer**: condenses pasted text into 3 concise lines
- **Direct answer**: general-knowledge questions answered by the LLM

## 🧠 How It Works

```
              ┌──────────► search ───────┐
              │                          │
START ──► decide ──► calculator ─────────┼──► END
              │                          │
              ├──────► summarizer ───────┤
              │                          │
              └──────────► answer ───────┘
```

1. The user enters a query in the Streamlit UI.
2. The `decide` node asks the LLM to choose: `search`, `calculator`, `summarizer`, or `answer`.
3. A conditional edge routes the state to the chosen node.
4. The node produces `final_result`, which is displayed in the app.

## 🛠️ Tech Stack

- Python
- [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://www.langchain.com/)
- OpenAI (`gpt-4o-mini`)
- [Tavily](https://tavily.com/) search API
- Streamlit

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/prabal-chaurasia/Info-Pilot.git
cd Info-Pilot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API keys

Get your keys here:

- OpenAI: https://platform.openai.com/api-keys
- Tavily: https://app.tavily.com/

Then set them as environment variables.

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your_openai_api_key"
$env:TAVILY_API_KEY="your_tavily_api_key"
```

**macOS / Linux:**
```bash
export OPENAI_API_KEY="your_openai_api_key"
export TAVILY_API_KEY="your_tavily_api_key"
```

### 5. Run the app

```bash
streamlit run App.py
```

## 💡 Example Queries

| Query | Tool used |
|-------|-----------|
| `What's the weather in Bhopal today?` | Web search |
| `Latest news about AI agents` | Web search |
| `(25 * 4) + 10 / 2` | Calculator |
| `Summarize: <paste a long paragraph>` | Summarizer |
| `Explain what a closure is in JavaScript` | Direct answer |

## 📁 Project Structure

```
Info-Pilot/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚠️ Notes

- The calculator accepts numeric expressions only (`+ - * / // % **`). Text-form math like "twenty plus five" is not supported.

## 🔮 Future Improvements

- Conversation memory across queries
- Source links shown alongside search results
- More tools (file upload, unit conversion, code execution)

## 👤 Author

**Prabal Chaurasia**: [GitHub](https://github.com/prabal-chaurasia) · [LinkedIn](https://www.linkedin.com/in/prabal-chaurasia)
