from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("demo-server")

# Add a simple tool
@mcp.tool()
def hello(name: str) -> str:
    """Say hello"""
    return f"Salam Alaikom {name} :) !"


if __name__ == "__main__":
    mcp.run()
