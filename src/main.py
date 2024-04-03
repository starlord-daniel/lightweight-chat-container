from lib import generate_answer


def main():

    chat_history = []

    for i in range(3):

        # ask the user for a question to the assistant
        text = input("Question: ")
        chat_history.append(("user", text))

        answer = generate_answer(text, chat_history=chat_history)
        chat_history.append(("assistant", answer))

        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
