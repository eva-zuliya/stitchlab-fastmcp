from instance import mcp

# Import tools to register them with the MCP server
from tools import calculation

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

