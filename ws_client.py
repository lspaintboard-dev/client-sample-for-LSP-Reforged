import asyncio
import websockets

import make_req_text as mr

resp:dict[int,str] = {}

async def connect(url:str):
    async with websockets.connect(url) as ws_c:
        while True:
            res = await ws_c.recv()
            match res[0]:
                case "\xfc":
                    if(len(res)==1):
                        await ws_c.send(await mr.pong())
                        continue
                    # set_color
                case "\xff":
                    resp[res[1]*256+res[2]]=res[3]
                

