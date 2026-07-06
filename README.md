📦 Setup & Run Instructions

📌 1. Initial setup

  Open the project repository on GitHub
  Click Code → Codespaces → Create codespace
  
  Wait for the environment to finish building


⏳ 2. Wait for setup to finish

  After the dev container starts, allow some time for all dependencies to install automatically.

  During this step, you should see output similar to:

    ✔ Finishing up...
    ⠏ Running postCreateCommand...
    › pip install -r requirements.txt

  Wait until the process is fully completed before continuing.


🚀 3. Start the MCP server

  Once the setup is complete, start the MCP server using:

    mcp run server.py --transport sse

  You should see output similar to:

    INFO:     Started server process [2464]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


🌐 4. Make the port public

  Once the environment is running:
  
  Open the Ports tab
  Find port 8000
  Change its visibility from Private → Public


🖥️ 5. Open a new terminal

  Start a fresh terminal inside your Codespace/dev environment.


🔑 6. Set your OpenAI API key

    export OPENAI_API_KEY="your-api-key-here"

  
▶️ 7. Start the chat client
    
    python3 chat.py


🔗 8. Connect to the MCP server

  When prompted, paste your forwarded port URL and append "sse"
  
  Example:
    
    https://<your-codespace>-8000.app.github.dev/sse


💬 9. Start chatting 

  Once connected successfully, you can start interacting with the MCP server through the chat interface.


⚠️ Notes & Troubleshooting

  - Make sure the server is fully running before starting chat.py
  - If the port is still private, the connection will fail
  - Ensure OPENAI_API_KEY is set correctly before running the chat client
  - If the endpoint fails, double-check the /sse suffix
  
