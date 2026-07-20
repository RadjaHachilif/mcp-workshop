from mcp.server.fastmcp import FastMCP

# Create the MCP server. Streamable HTTP is configured below for remote use.
mcp = FastMCP(
    "demo-server",
    host="0.0.0.0",
    port=8000,
    log_level="INFO",
    stateless_http=True,
)

# A simple test tool
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
