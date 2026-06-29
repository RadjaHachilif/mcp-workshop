from openai import OpenAI

client = OpenAI()

MCP_SERVER_URL = input("MCP_SERVER_URL: ")

history = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        break

    history.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-5",
        input=history,
        tools=[
            {
                "type": "mcp",
                "server_label": "demo",
                "server_url": MCP_SERVER_URL,
                "require_approval": "never",
            }
        ],
    )

    assistant_text = response.output_text
    print("Assistant:", assistant_text)

    history.append({"role": "assistant", "content": assistant_text})
