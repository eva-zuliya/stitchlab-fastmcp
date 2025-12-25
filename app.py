from mcp.server.fastmcp import FastMCP

# Initialize the MCP server with host and port
mcp = FastMCP("Simple MCP Server", host="0.0.0.0", port=8000)

# Import tools to register them with the MCP server
from tools import calculation

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

