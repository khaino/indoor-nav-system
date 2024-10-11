import asyncio
from websockets.asyncio.server import serve
import cv2
from time import sleep
import base64

PORT = 8000
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

class Camera_Server:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, FRAME_WIDTH)
        self.cap.set(4, FRAME_HEIGHT)
        self.cap.set(10,150)

    async def handler(self, websocket):
        message = await websocket.recv()
        print(message)
        while True:
            success, img = self.cap.read()
            if success:
                # Source: https://gist.github.com/patharanordev/e22f2fe1c2593c9e5d9f7fbd00d8da09
                img_bytes = cv2.imencode('.jpg', img)[1].tobytes()
                b64 = base64.b64encode(img_bytes).decode()
                await websocket.send(f"{b64}")
            # sleep(1)

    async def start(self):
        async with serve(self.handler, "localhost", PORT):
            await asyncio.get_running_loop().create_future()  # run forever

def main():
    s = Camera_Server()
    asyncio.run(s.start())

if __name__ == '__main__':
    main()