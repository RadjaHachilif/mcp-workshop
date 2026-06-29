from openai import OpenAI

client = OpenAI()

MCP_SERVER_URL = input("MCP_SERVER_URL: ")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        break

    response = client.responses.create(
        model="gpt-5",
        input=user_input,
        tools=[
            {
                "type": "mcp",
                "server_label": "demo",
                "server_url": MCP_SERVER_URL,
                "require_approval": "never",
            }
        ],
    )

    print("Assistant:", response.output_text)
