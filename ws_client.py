import asyncio
import websockets
import random

import lib as mr
import config as cg

resp:dict[int,str] = {}

data_all = []

async def mk_req():
    # 这是一个向全版随机 #39C5BB 的 sample
    while True:
        try:
            for tk in cg.token_list:
                x=random.randint(0,999)
                y=random.randint(0,599)
                id,data = await mr.paint(x,y,(0x39,0xc5,0xbb),710036,tk)
                global data_all
                data_all += data
                await asyncio.sleep(0.0001)
        except Exception as ex:
            print(str(ex))

async def send_req(ws_c):
    global data_all
    while True:
        if len(data_all) != 0:
            print(len(data_all))
            await ws_c.send(bytes(data_all))
            data_all.clear()
        await asyncio.sleep(cg.cd_req)

async def connect(url:str):
    async with websockets.connect(url) as ws_c:
        asyncio.gather(mk_req(),send_req(ws_c))
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
