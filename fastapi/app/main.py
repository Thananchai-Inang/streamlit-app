import uvicorn
import asyncio
if __name__ == "__main__":

    asyncio.create_task(uvicorn.run("server.app:app", host="0.0.0.0", port=80, reload=True))
    asyncio.get_event_loop().run_forever()
