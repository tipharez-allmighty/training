from typing import Callable

from openai import OpenAI


SYSTEM_PROPMT = """
You are AI assistant that does {expertise}. Answer user messages taking
into consideration your prior message history.
Here is the message history: 
{history}
"""

history = []

client = OpenAI()

def chat_with_history(func) -> Callable:
    def wrapper(*args, **kwargs) -> dict[str, str]:
        user_message = kwargs['message']
        llm_response = func(*args, **kwargs)
        history.extend([
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": llm_response}
        ])
        return llm_response
    return wrapper
        
    

@chat_with_history
def llm_response(*, expertise: str, message: str) -> str:
    response = client.responses.create(
        model="chatgpt-4o-latest",
        input=[
            {"role": "system", "content": SYSTEM_PROPMT.format(
                expertise=expertise, history=history
            )},
            {"role": "user", "content": message}
        ]
    ).output_text
    return response
