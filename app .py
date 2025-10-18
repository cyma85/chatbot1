# app.py
import gradio as gr
from datetime import datetime

def chatbot_response(user_input):
    if user_input is None:
        return "Sorry, I didn't get that."

    user_input = user_input.strip().lower()

    if user_input == "":
        return "Please type something."

    if "hello" in user_input or user_input.startswith("hi"):
        return "Hello! 😊 How can I help you today?"
    if "your name" in user_input or "who are you" in user_input:
        return "I'm your friendly chatbot 🤖."
    if "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    if "time" in user_input:
        return "Current time is: " + datetime.now().strftime("%I:%M %p")
    if "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! 👋 Have a nice day!"
    # fallback
    return "I'm not sure I understand. Could you rephrase that?"

# A helper to keep simple chat history (list of [user, bot])
def respond(history, user_input):
    bot_reply = chatbot_response(user_input)
    history = history or []
    history.append([user_input, bot_reply])
    return history, ""

# Build Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 💬 Simple Rule-based Chatbot")
    gr.Markdown("This is a beginner-friendly chatbot (no API keys). Type anything and press Enter or the **Send** button.")
    chatbot = gr.Chatbot(elem_id="chatbox", label="Chat")
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Type your message and press Enter")
        send = gr.Button("Send")
    state = gr.State([])  # will hold chat history: list of [user, bot]

    # Actions
    send.click(respond, inputs=[state, txt], outputs=[chatbot, txt])
    txt.submit(respond, inputs=[state, txt], outputs=[chatbot, txt])

# Launch
if __name__ == "__main__":
    demo.launch()
