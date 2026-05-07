# 🔥 Trend Content Generator

An AI-powered automation platform that converts live trending news into engaging social media content using **Groq AI**, **n8n**, and **Streamlit**.

🌐 **Live Demo:**  
https://trend-content-generator-xdlowpbqsb3jc6fwsi4sfi.streamlit.app/

---

# 🚀 Overview

Trend Content Generator automatically fetches real-time trending news from RSS feeds and transforms them into ready-to-post social media content for platforms like:

- LinkedIn
- Instagram
- Twitter/X

The workflow is powered by **n8n automation** and **Groq LLMs**, enabling ultra-fast AI content generation with a lightweight frontend built in Streamlit.

---

# ✨ Features

- 📰 Live RSS Trend Fetching
- ⚡ Ultra-Fast Groq AI Processing
- 🤖 Automated AI Content Generation
- 📱 Platform-Specific Social Media Posts
- 🏷️ Smart Hashtag Generation
- 🔄 n8n Workflow Automation
- 🌐 Streamlit Cloud Deployment
- 📦 Structured JSON Response Handling

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Streamlit | Frontend UI |
| n8n | Workflow Automation |
| Groq AI | AI Content Generation |
| RSS Feed | Live Trend Source |
| Python | Frontend Logic |
| JavaScript | JSON Formatting |

---

# 🏗️ System Architecture

## 1️⃣ Data Ingestion

### API Entry Point
Receives requests from the Streamlit frontend.

### Live News Fetcher
Fetches trending headlines from live RSS feeds.

---

## 2️⃣ AI Processing

### Rate Limit Buffer
Controls API request flow to avoid quota issues.

### AI Content Orchestrator
Processes news data using Groq LLMs and generates:

- Content Title
- AI Summary
- Social Media Posts
- Hashtags

---

## 3️⃣ Data Output

### JavaScript Formatter
Cleans and structures the AI response into JSON format.

### Frontend Success Return
Returns generated content back to the Streamlit interface.

---

# 📂 Project Structure

```plaintext
├── app.py                  # Streamlit frontend
├── requirements.txt        # Python dependencies
├── assets/                 # Images and workflow screenshots
├── workflow.json           # Exported n8n workflow
└── README.md               # Project documentation
```

---

# 🚦 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/trend-content-generator.git
cd trend-content-generator
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure n8n

- Import your `workflow.json` into n8n
- Add your Groq API credentials
- Configure Webhook node as `POST`
- Copy the Production Webhook URL

---

## 4️⃣ Configure Streamlit

Add your webhook URL inside `app.py`

```python
N8N_URL = "YOUR_N8N_WEBHOOK_URL"
```

---

## 5️⃣ Run Application

```bash
streamlit run app.py
```

---

# 📸 Application Preview

## 🔹 n8n Workflow

![n8n Workflow](assets/n8n-workflow.png)

---

## 🔹 Streamlit Interface

![Streamlit UI](assets/streamlit-ui.png)

---

# 🔐 Streamlit Secrets (Recommended)

Instead of hardcoding URLs or API keys:

```python
import streamlit as st

N8N_URL = st.secrets["N8N_URL"]
```

---

# 📦 requirements.txt

```plaintext
streamlit
requests
```

---

# 🧠 Future Improvements

- 🎨 AI Image Generation
- 📅 Social Media Scheduling
- 🌍 Multi-language Support
- 📊 Trend Analytics Dashboard
- 🔥 Viral Score Prediction
- 📱 Mobile Responsive UI

---

# 📝 Author

### Charitha V.

AI Automation Enthusiast | AI Workflow Builder | 2026

---

# ⭐ Support

If you found this project useful, give it a ⭐ on GitHub.

---
