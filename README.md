# ECCB MCP Workshop: Setup and Run

## 1. Initial setup

1. Open the project repository on GitHub.
2. Select **Code**, then **Codespaces**, then **Create codespace**.
3. Wait for the environment to finish building.

## 2. Wait for setup to finish

After the dev container starts, allow time for all dependencies to install automatically.

During this step, you should see output similar to:

```text
Finishing up...
Running postCreateCommand...
pip install -r requirements.txt
```

Wait until the process has completed before continuing.

## 3. Start the MCP server

Once setup is complete, start the MCP server:

```bash
python3 server.py
```

You should see output similar to:

```text
INFO:     Started server process [2464]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## 4. Make the port public

Once the environment is running:

- Open the **Ports** tab.
- Find port `8000`.
- Change its visibility from **Private** to **Public**.

## 5. Open a new terminal

Start a fresh terminal inside the Codespace/dev environment.

## 6. Configure the chat client

Open `server.conf` and replace both placeholder values:

```text
OPENAI_API_KEY="your-api-key-here"
MCP_SERVER_URL="https://<your-codespace>-8000.app.github.dev/mcp"
```

Keep the `/mcp` suffix on the MCP server URL. Do not commit a real API key.

## 7. Start the chat client

```bash
python3 chat.py
```

## 8. Start chatting

The client reads the server URL from `server.conf`, then you can start interacting with the MCP server through the chat interface.

## Troubleshooting

- Ensure the server is fully running before starting `chat.py`.
- The connection will fail if port `8000` is still private.
- Ensure both values in `server.conf` have been replaced before starting the chat client.
- If the endpoint fails, double-check the `/mcp` suffix.
