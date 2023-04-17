# Reference: https://beebom.com/how-train-ai-chatbot-custom-knowledge-base-chatgpt-api/

# Install:

- Install `Python`
- Install: `OpenAI`, `GPT Index`, `PyPDF2`, and `Gradio` Libraries by `requirements.txt`
Command: `pip install -r requirements.txt`
- Sign-up ChatGPT account and Create an API key account via this link: https://platform.openai.com/signup (Free Account with 5 USD)
(Note: Check usage on ChatGPT account via this link: https://platform.openai.com/account/usage)
- We will use the `“gpt-3.5-turbo”` model because it’s cheaper and faster than other models. If you want to use the latest “gpt-4” model, you must have access to the GPT 4 API which you get by joining the waitlist here. 
- `docs` folder, where we save all PDF document that ChatGPT will learn.
- Next, move the documents you wish to use for training the AI inside the “docs” folder. You can add multiple text or PDF files (even scanned ones).

# Run:
python app.py [OPEN_AI_KEY]