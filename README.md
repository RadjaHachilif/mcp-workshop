📦 Setup & Run Instructions

📌 1. Initial setup

  Open the project repository on GitHub
  Click Code → Codespaces → Create codespace
  Wait for the environment to finish building


⏳ 2. Wait for setup to finish

  After the dev container starts, allow time for dependencies to install.
  You will see:
  
  ⠋ Running postStartCommand...


🌐 3. Make the port public

  Once the environment is running:
  
  Open the Ports tab
  Find port 8000
  Change its visibility from Private → Public


🖥️ 4. Open a new terminal

  Start a fresh terminal inside your Codespace/dev environment.


🔑 5. Set your OpenAI API key

  export OPENAI_API_KEY="your-api-key-here"

  
▶️ 6. Start the chat client
    
    python3 chat.py


🔗 7. Connect to the MCP server

  When prompted, paste your forwarded port URL and append "sse"
  
  Example:
    
    https://<your-codespace>-8000.app.github.dev/sse


💬 8. Start chatting 

Once connected successfully, you can start interacting with the MCP server through the chat interface.


⚠️ Notes & Troubleshooting

  - Make sure the server is fully running before starting chat.py
  - If the port is still private, the connection will fail
  - Ensure OPENAI_API_KEY is set correctly before running the chat client
  - If the endpoint fails, double-check the /sse suffix
  
