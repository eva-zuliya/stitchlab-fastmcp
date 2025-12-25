"""MCP instance module to avoid circular imports."""
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server with host and port
mcp = FastMCP("Simple MCP Server", host="0.0.0.0", port=8000)

