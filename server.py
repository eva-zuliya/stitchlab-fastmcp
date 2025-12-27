from mcp.server.fastmcp import FastMCP
from tools import TOOL_REGISTRY

# Initialize the MCP server with host and port
mcp = FastMCP("Simple MCP Server", host="0.0.0.0", port=8000)

for tool in TOOL_REGISTRY:
    mcp.tool()(tool)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
