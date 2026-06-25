import gradio as gr
from transformers import pipeline

# Load models
sentiment = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = [
    "Sports",
    "Education",
    "Technology",
    "Politics",
    "Finance",
    "Health",
    "Entertainment",
    "Business",
    "Travel",
    "Food"
]

def analyze(text):
    if not text.strip():
        return "Please enter some text.", "", "", ""

    # Sentiment
    s = sentiment(text)[0]
    sent = s["label"]
    score = round(s["score"] * 100, 2)

    # Category
    c = classifier(text, labels)
    category = c["labels"][0]

    explanation = f"The sentence is classified as '{sent}' and belongs to the '{category}' category."

    return sent, category, f"{score}%", explanation


demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter a sentence or paragraph..."
    ),
    outputs=[
        gr.Text(label="Sentiment"),
        gr.Text(label="Category"),
        gr.Text(label="Confidence"),
        gr.Textbox(label="Explanation")
    ],
    title="🧠 AI Sentiment & Topic Analyzer",
    description="Analyze text to determine its sentiment and topic using Hugging Face Transformers."
)

demo.launch()