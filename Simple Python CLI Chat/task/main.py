import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion


def get_api_key() -> str | None:
    """Load API key from .env file."""
    load_dotenv(r"C:\Users\aaa\PycharmProjects\Simple Python CLI Chat\.env")
    key = os.environ.get("OpenAI_API_KEY", None)
    return key


def get_chat_completion(messages_: list[dict[str, str]]) -> ChatCompletion:
    """Send messages to OpenAI API and get the chat completion."""
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_,
        temperature=1.0,
    )


def get_prompt() -> str:
    """Get a prompt from user input."""
    return input("Enter a message: ")


def get_cost(response_: ChatCompletion) -> float:
    """Calculate cost in USD for the given ChatCompletion response."""
    # Pricing for gpt-4o-mini (in USD per 1K tokens)
    PROMPT_PRICE = 0.005
    COMPLETION_PRICE = 0.02

    prompt_tokens: int = response_.usage.prompt_tokens
    completion_tokens: int = response_.usage.completion_tokens

    return (prompt_tokens / 1000 * PROMPT_PRICE) + (completion_tokens / 1000 * COMPLETION_PRICE)


if __name__ == '__main__':
    prompt = get_prompt()
    API_KEY = get_api_key()
    client = OpenAI(api_key=API_KEY)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant for a simple CLI chat. Only respond with text messages. Get creative with the answers!"
        },
        {"role": "user", "content": prompt}
    ]

    response = get_chat_completion(messages)
    reply = response.choices[0].message.content
    cost = get_cost(response)

    print(f"You: {prompt}")
    print(f"Assistant: {reply}")
    print(f"Cost: ${cost}")
