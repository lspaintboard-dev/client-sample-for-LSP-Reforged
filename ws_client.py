import asyncio
import websockets
import random

import lib as mr

resp:dict[int,str] = {}

async def send_pt(ws_c):
    # 这是一个向全版随机 #39C5BB 的 sample
    while True:
        try:
            x=random.randint(0,1000)
            y=random.randint(0,600)
            id,data = await mr.paint(x,y,(0x39,0xc5,0xbb),710036,"2f78a537-55ae-414a-8c76-1f679dbdafd0")
            await ws_c.send(bytes(data))
            await asyncio.sleep(0.01)
        except Exception as ex:
            print(str(ex))


async def connect(url:str):
    async with websockets.connect(url) as ws_c:
        asyncio.gather(send_pt(ws_c))
        while True:
            res = await ws_c.recv()
            unp = await mr.unpack(res)
            for pkg in unp:
                match pkg[0]:
                    case 0xfc:
                        await ws_c.send(await mr.pong())
                        print("Pong!")
                    case 0xff:
                        await mr.pt_res(pkg)
                    case 0xfa:
                        await mr.set_col(pkg)
                    
                
asyncio.get_event_loop().run_until_complete(connect("wss://api.paintboard.ayakacraft.com:32767/api/paintboard/ws"))
