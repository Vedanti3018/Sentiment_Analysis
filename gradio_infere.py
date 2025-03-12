import gradio as gr
import json
from fastapi.testclient import TestClient
from sentiment import app

# Initialize FastAPI test client
client = TestClient(app)

# Load pre-stored examples
with open("examples.json") as f:
    stored_examples = json.load(f)


def analyze(text, use_stored=False):
    """Analyze text sentiment using either stored examples or live API"""
    if use_stored:
        # Return pre-stored response if available
        for example in stored_examples:
            if example["input"] == text:
                return example["output"]
        return "No stored example found"
    else:
        # Live API call
        response = client.post("/api/sentiment", json={"text": text})
        if response.status_code == 200:
            data = response.json()
            return f"Score: {data['score']}%\nSentiment: {data['sentiment']}"
        return "Error analyzing text"


# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Sentiment Analysis Demo")

    # Section for pre-stored examples
    with gr.Tab("Stored Examples"):
        gr.Markdown("## Pre-stored Examples")
        example_selector = gr.Dropdown(
            choices=[ex["name"] for ex in stored_examples],
            label="Select Example"
        )

        with gr.Row():
            input_display = gr.Textbox(label="Example Input", interactive=False)
            output_display = gr.Textbox(label="Stored Output", interactive=False)

        example_selector.change(
            lambda x: next(
                (ex["input"], ex["output"])
                for ex in stored_examples
                if ex["name"] == x
            ),
            inputs=example_selector,
            outputs=[input_display, output_display]
        )

    # Section for live analysis
    with gr.Tab("Live Analysis"):
        gr.Markdown("## Live Sentiment Analysis")
        live_input = gr.Textbox(label="Input Text", placeholder="Enter text here...")
        live_output = gr.Textbox(label="Analysis Result")
        analyze_btn = gr.Button("Analyze")

        analyze_btn.click(
            fn=lambda x: analyze(x, use_stored=False),
            inputs=live_input,
            outputs=live_output
        )

if __name__ == "__main__":
    demo.launch()