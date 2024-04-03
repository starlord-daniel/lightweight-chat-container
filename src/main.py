from lib import generate_answer


def main():

    text = "What is the capital of France?"

    answer = generate_answer(text)

    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
