# 🔥 Trend Content Generator

An automated content orchestration platform that transforms live news trends into high-engagement social media kits using **Groq AI**, **n8n**, and **Streamlit**.

---

## 🚀 Overview

The **Trend Content Generator** monitors live RSS feeds to identify breaking trends, summarizes them using AI, and automatically generates tailored content for multiple social media platforms.

### ✨ Key Features

- 📰 **Real-time Trend Ingestion**  
  Fetches the latest global trends using RSS feeds.

- ⚡ **Groq AI Integration**  
  Uses Groq's ultra-fast LPU inference for instant AI-generated outputs.

- 📱 **Multi-Platform Content Kits**  
  Generates:
  - LinkedIn posts
  - Instagram captions
  - Twitter/X posts
  - Hashtags
  - AI summaries

- ⏱️ **Smart Rate Limiting**  
  Built-in workflow buffers to handle API quota limits smoothly.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit (Python) |
| Backend Workflow | n8n |
| AI Engine | Groq (Llama-3 / Mixtral) |
| Data Source | RSS Feeds |
| Communication | REST API / Webhooks |

---

# 🏗️ System Architecture

## 1️⃣ Data Ingestion

### API Entry Point
Receives requests from the Streamlit frontend.

### Live News Fetcher
Collects trending headlines from RSS feeds in real-time.

---

## 2️⃣ AI Processing

### Rate Limit Buffer
Prevents excessive API requests to Groq.

### AI Content Orchestrator
Processes trending news and generates:
- Title
- Summary
- LinkedIn content
- Instagram caption
- Twitter/X post
- Relevant hashtags

---

## 3️⃣ Data Output

### JavaScript Formatter Node
Formats and cleans the JSON response.

### Frontend Response
Returns generated content back to Streamlit UI.

---

# 📂 Project Structure

```plaintext
├── app.py              # Streamlit frontend logic
├── requirements.txt    # Python dependencies
├── assets/             # Workflow screenshots/images
└── README.md           # Project documentation
```

---

# 🚦 Getting Started

## 1️⃣ Setup n8n Workflow

- Import your workflow JSON into n8n
- Configure your Groq API credentials
- Set the Webhook node method to `POST`
- Copy the Production Webhook URL

---

## 2️⃣ Setup Streamlit Frontend

### Install Dependencies

```bash
pip install streamlit requests
```

### Configure Webhook URL

Add your `N8N_URL` inside `app.py`.

Example:

```python
N8N_URL = "YOUR_N8N_WEBHOOK_URL"
```

### Run the App

```bash
streamlit run app.py
```

---

# 📸 Workflow Preview

> Add your n8n workflow screenshot inside the `assets/` folder and embed it here.

Example:

```markdown
![Workflow Preview](assets/workflow.png)
```

---

# 🔐 Recommended Security Practice

Instead of hardcoding your webhook URL, use **Streamlit Secrets Management**.

Example:

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

- AI image generation support
- Auto-posting to social media
- Multi-language content generation
- Trend analytics dashboard
- Content scheduling

---

# 📝 Author

### Charitha V.
AI Automation Enthusiast | 2026

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.

---
