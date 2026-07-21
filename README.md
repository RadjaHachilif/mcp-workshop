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
./server.py >& server.log
```

The server output is written to `server.log`. It includes messages similar to:

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
- Right-click the port, then select **Port Visibility** → **Public**.

## 5. Configure the chat client

Click `chat.conf` in the left-hand file explorer and replace both placeholder values:

```text
OPENAI_API_KEY="your-api-key-here"
MCP_SERVER_URL="https://<your-codespace>-8000.app.github.dev/mcp"
```

Keep the `/mcp` suffix on the MCP server URL. Do not commit a real API key. Then return to this README.

## 6. Open a new terminal

Open the **Terminal** tab and click **+** to start a fresh terminal.

## 7. Open the server log

Click `server.log` in the left-hand file explorer and keep it open on the right. It shows errors and debug information from your MCP server.

## 8. Start the chat client and begin chatting

```bash
./chat.py
```

The client reads the server URL from `chat.conf`. You can now start interacting with the MCP server through the chat interface.

## Troubleshooting

- Ensure the server is fully running before starting `chat.py`.
- The connection will fail if port `8000` is still private.
- Ensure both values in `chat.conf` have been replaced before starting the chat client.
- If the endpoint fails, double-check the `/mcp` suffix.

## Dataset included

The included example dataset is from ['The project Wortschatz Leipzig'](https://wortschatz.uni-leipzig.de/en)
