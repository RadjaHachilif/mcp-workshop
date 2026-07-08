from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("demo-server")

# A simple test tool
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    mcp.run()
