from fastmcp import Client
from weather_service import mcp
import asyncio

async def main():
    async with Client(mcp) as mcp_client:
        response = await mcp_client.list_tools()
        print("Available tools:", response)


if __name__ == "__main__":
    test = asyncio.run(main())
