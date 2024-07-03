import openai
import pandas as pd
from config.settings import OPENAI_API_KEY

def create_prompt(posts):
    prompt = "The following are posts from the game developer forum:\n"
    for post in posts:
        prompt += f"Author: {post['author']}\nDate: {post['date']}\nContent: {post['content']}\n\n"
    prompt += "Based on the above information, please summarize the key techniques used in the development of Rainworld."
    return prompt

def interact_with_api(prompt):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text

if __name__ == '__main__':
    df = pd.read_csv('data/processed/forum_data_processed.csv')
    posts = df.to_dict('records')
    prompt = create_prompt(posts)
    summary = interact_with_api(prompt)
    print(summary)
