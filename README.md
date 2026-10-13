# 🤖 Info Pilot — Multi-Tool AI Agent

Info Pilot is a Streamlit app built with **LangGraph**. It takes a query, uses an LLM to decide which tool fits best, and routes the query to that tool automatically.

## ✨ Features

- **Smart routing**: a decision node asks the LLM to choose one of four tools: `search`, `calculator`, `summarizer`, or `answer`
- **Web search**: fetches the top 3 results from the Tavily API and turns them into a clean, readable answer; weather queries are formatted as Location, Temperature, Condition, Humidity and Wind
- **Calculator**: evaluates math expressions
- **Summarizer**: summarizes the given text in 3 concise lines
- **Direct answer**: general-knowledge questions answered directly by the LLM

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

1. The user enters a query in the Streamlit UI and clicks **Run Agent**.
2. The `decide` node sends the query to the LLM, which picks a tool.
3. A conditional edge routes the state to the chosen node (anything unrecognized falls back to `answer`).
4. The node writes its output to `final_result`, which is shown as the final answer.

## 🛠️ Tech Stack

- Python
- LangGraph and LangChain (`langchain-openai`)
- OpenAI (`gpt-4o-mini`)
- Tavily (`tavily-python`) for web search
- Streamlit
- python-dotenv

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

The app reads two keys from environment variables:

- `OPENAI_API_KEY`: https://platform.openai.com/api-keys
- `TAVILY_API_KEY`: https://app.tavily.com/

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

## 👤 Author

**Prabal Chaurasia**: [GitHub](https://github.com/prabal-chaurasia) · [LinkedIn](https://www.linkedin.com/in/prabal-chaurasia)
