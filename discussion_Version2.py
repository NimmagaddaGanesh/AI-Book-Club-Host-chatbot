import os
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def generate_discussion_prompt(book_title):
    prompt = (
        f"Generate three thought-provoking discussion questions for a book club reading the book '{book_title}'."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful book club assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating discussion prompt: {e}"

def summarize_chapter(chapter_text):
    prompt = (
        f"Summarize the following book chapter in 3-5 concise bullet points:\n\n{chapter_text[:1200]}"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful book club assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=180,
            temperature=0.6,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating summary: {e}"