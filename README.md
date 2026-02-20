# 🎧 Game Sound Effect Planner

An AI-powered web application that turns any game action description into a detailed, professional sound design brief — powered by **Pollinations AI** with **no API keys or sign-up required**.

## ✨ Features

- **AI Sound Design Briefs**: Describe any game action and get a full sound design document.
- **Emotional Feel Analysis**: How the sound should make the player feel.
- **Frequency Profile**: Detailed low/mid/high frequency breakdown.
- **Layer Breakdown**: Attack, body, tail, and sweetener layer descriptions.
- **Production Notes**: Synthesis vs. foley, tools, processing chains, duration.
- **Genre-Aware**: Select from 10+ game genres for tailored results.
- **100% Free**: Powered by Pollinations AI — no account, API key, or sign-up needed.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Waveform Noir design)
- **Backend**: Python FastAPI (Vercel Serverless)
- **AI Core**: Pollinations AI (free, no API keys)
- **Markdown**: Marked.js for rich output rendering

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8+
- pip

### Steps
```bash
# Navigate to the project
cd game-sfx-planner

# Install dependencies
pip install -r requirements.txt

# Run the local server
python app.py
```

Open [http://localhost:8010](http://localhost:8010) in your browser.

## 🌍 Deployment

This project is optimized for deployment on **Vercel**. Simply connect your GitHub repository to Vercel and it will auto-deploy using the provided `vercel.json` and serverless functions in the `api/` directory.

## 📁 Project Structure

```
game-sfx-planner/
├── api/
│   └── describe.py      # Vercel Serverless Function
├── planning/
│   ├── implementation_plan.md
│   └── walkthrough.md
├── app.py               # Local Dev Server
├── index.html           # Frontend
├── vercel.json          # Deployment Config
├── requirements.txt
└── README.md
```

## 📜 License

MIT

---

*Built with ❤️ — Powered by Pollinations AI*
