from typing import List, Tuple
from openai import AzureOpenAI
from dotenv import load_dotenv
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageParam,
)


load_dotenv()
CLIENT = AzureOpenAI()


def generate_answer(
    text: str,
    system_message: str = "You are a helpful chatbot that tries to answer questions to the best of your ability.",
    chat_history: List[Tuple[str, str]] = [],
    deployment_name="gpt-35-turbo",
) -> None | str:
    """
    Generate an answer from a given text using OpenAI's API.

    Parameters
    ----------
    text : str
        The text to generate the answer from.

    system_message : str , optional
        The system message to use for the answer generation.

    chat_history : List[Tuple[str, str]] , optional
        The chat history to use for the answer generation.
        Each tuple should contain the role and the content of the chat message, respectively.

    deployment_name : str, optional
        The name of the deployed model to use for the answer generation. The default is "gpt-35-turbo".

    Returns
    -------
    str
        The generated answer.
    """

    messages: List[ChatCompletionMessageParam] = []

    # Add the system message to the messages list
    messages.append(
        ChatCompletionSystemMessageParam(content=system_message, role="system")
    )

    # Add the chat history to the messages list
    for chat in chat_history:
        if chat[0] == "assistant":
            messages.append(
                ChatCompletionAssistantMessageParam(
                    content=chat[1],
                    role="assistant",
                )
            )

        else:
            messages.append(
                ChatCompletionUserMessageParam(content=chat[1], role="user")
            )

    # Add the user message to the messages list
    messages.append(
        ChatCompletionUserMessageParam(
            content=text,
            role="user",
        )
    )

    response = CLIENT.chat.completions.create(model=deployment_name, messages=messages)

    return response.choices[0].message.content
