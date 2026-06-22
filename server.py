from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("demo-server")


# Add a simple tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add another tool
@mcp.tool()
def hello(name: str) -> str:
    """Say hello"""
    return f"Hello {name}!"


if __name__ == "__main__":
    mcp.run()
