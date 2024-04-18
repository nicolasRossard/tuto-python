import gradio as gr
from tasks import greet


interface = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Name"),
    outputs=gr.Textbox(),
    title="Simple Gradio App",
    description="Type your name and get greeted!"
)

if __name__ == "__main__":
    print("hello world")
    interface.launch()