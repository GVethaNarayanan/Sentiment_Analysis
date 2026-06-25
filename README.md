---
title: Sentiment Analysis
emoji: 🏆
colorFrom: purple
colorTo: yellow
sdk: gradio
sdk_version: 6.19.0
python_version: '3.13'
app_file: app.py
pinned: false
---

# 🧠 AI Sentiment & Topic Analyzer

A professional, web-based NLP tool designed to analyze text sentiment and categorize it into specific topics using state-of-the-art transformer models.

🚀 **Live Demo**: [Run the App on Hugging Face Spaces](https://huggingface.co/spaces/VethaNarayananG/Sentiment_Analysis)

---

## 🌟 Features

- **Sentiment Analysis**: Evaluates text sentiment (Positive, Negative, Neutral) using the `cardiffnlp/twitter-roberta-base-sentiment-latest` model.
- **Zero-Shot Classification**: Categorizes text into 10 pre-defined topics (Sports, Education, Technology, Politics, Finance, Health, Entertainment, Business, Travel, Food) using the `facebook/bart-large-mnli` model.
- **Explainable AI**: Provides a confidence score and a human-readable explanation of the prediction.
- **Interactive UI**: Built with a sleek, clean interface using **Gradio**.

## 🛠️ Installation & Local Setup

To run this project locally, ensure you have Python 3.10+ installed, then follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GVethaNarayanan/Sentiment_Analysis.git
   cd Sentiment_Analysis
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to the local URL provided by Gradio (typically `http://127.0.0.1:7860`).

## 📦 Dependencies

The application relies on:
- `gradio` - UI framework
- `transformers` - Hugging Face library for deep learning models
- `torch` - PyTorch backend
- `accelerate` - Optimizations for model loading
- `sentencepiece` - Text tokenizer

---
Designed and maintained by [Vetha Narayanan G](https://huggingface.co/VethaNarayananG).
