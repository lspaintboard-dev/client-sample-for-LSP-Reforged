import random

endpoint = ""

async def int2str(x:int)->str:
    text:str = ""
    num:list[int] = []
    while(x):
        num.append(x%256)
        x = x//256
    for each in reversed(num):
        text+=chr(each)
    return text

async def pong() -> str:
    return "\xfb"

async def paint(x:int,y:int,color:tuple[int,int,int],uid:int,token:str) -> str:
    id = random.randint(0,65535)
    text = "\xfe"+await int2str(x)+await int2str(y)+await int2str(color[0])+await int2str(color[1])+await int2str(color[2])+await int2str(uid)+token+await int2str(id)
    return id,text
