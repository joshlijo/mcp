from fastmcp import FastMCP
from api_v1 import app_v1
from api_v2 import app_v2
from api_v3 import app_v3

mcp = FastMCP(name="Movie Booking Server")

mcp.mount(FastMCP.from_fastapi(app=app_v1), namespace="movies")
mcp.mount(FastMCP.from_fastapi(app=app_v2), namespace="bookings")
mcp.mount(FastMCP.from_fastapi(app=app_v3), namespace="theatres")

if __name__ == "__main__":
    mcp.run()