import asyncio
import websockets
import ssl

WORKERS = 10
TOKEN = "MDoJIldpbmRvd3MiQggiMTAuMC4wIkoEIjY0IlJZIk5vdC9BKUJyYW5kIjt2PSI4LjAuMC4wIiwiQ2hyb21pdW0iO3Y9IjEyNi4wLjY0NzguNTYiLCJHb29nbGUgQ2hyb21lIjt2PSIxMjYuMC42NDc4LjU2IiJgyf7ytAY"
DELAY = 0.1

uri = f"wss://wss.yaytsogram.com/?token={TOKEN}"
ssl_context = ssl._create_unverified_context()

async def send_requests():
    while True:
        try:
            async with websockets.connect(uri, ssl=ssl_context) as websocket:
                while True: 
                    await websocket.send("addCoin")
                    await asyncio.sleep(DELAY)
        except: pass

async def main(): await asyncio.gather(*[send_requests() for _ in range(WORKERS)])

if __name__ == "__main__":
    asyncio.run(main())
