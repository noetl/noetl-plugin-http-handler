import asyncio
from nats.aio.client import Client as NATS
import httpx
import json
import os

async def run(loop):
    nc = NATS()
    await nc.connect(servers=[os.getenv("NATS_SERVER", "nats://nats-server:4222")], loop=loop)

    registration_payload = {
        "name": "http-request",
        "source_path": "https://github.com/noetl/noetl-plugin-http-handler.git",
        "image_path": "registry/noetl-plugin-request-image:latest",
        "schema": {
            "input": {"type": "string", "description": "URL to fetch"},
            "output": {"type": "string", "description": "HTTP response"}
        },
        "run_option": "service"  # or "job"
    }
    await nc.publish("registration", json.dumps(registration_payload).encode())

    async def handle_command(msg):
        url = msg.data.decode()
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        result_payload = {
            "result": resp.text
        }
        await nc.publish("events", json.dumps(result_payload).encode())

    await nc.subscribe("commands", cb=handle_command)

    await asyncio.sleep(3600)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()
