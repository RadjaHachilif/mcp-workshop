from openai import OpenAI

client = OpenAI()

MCP_SERVER_URL = input("MCP_SERVER_URL: ")

previous_response_id = None

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        break

    response = client.responses.create(
        model="gpt-5",
        input=user_input,
        previous_response_id=previous_response_id,
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

    # store session state
    previous_response_id = response.id