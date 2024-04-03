# Lightweight Chat Container

This repo contains a simple chat container that can be used to chat with other with an OpenAI LLM.

The intention is to be as simple and lightweight as possible.

You can interact with the assistant by typing messages in the terminal.

## Usage

To use the container, create a `.env` file from the `.env.example` file and fill in the necessary values.

Then, run the following command:

```bash
docker builld -t YOUR_CONTAINER_NAME:YOUR_VERSION .
docker run -it --rm YOUR_CONTAINER_NAME:YOUR_VERSION
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
