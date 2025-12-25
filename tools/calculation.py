# Import the mcp instance from app.py
from app import mcp

# Define a simple tool (non-streaming)
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

