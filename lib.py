import random

endpoint = ""

async def unpack(raw:bytes):
    packages = []
    l = len(raw)
    i = 0
    offset = 0 
    while(i<l):
        match raw[i]:
            case 0xfc:
                offset = 1
            case 0xfa:
                offset = 8
            case 0xff:
                offset = 6
            case _:
                print("Unknown op %d"%raw[i])
                raise TypeError("Unknown op %d"%raw[i])
        packages.append(raw[i:i+offset])
        i+=offset
    return packages

    

def int2str(x:int,dig:int=1)->str:
    text:str = ""
    for i in range(0,dig):
        text+=chr(x & 0xff)
        x >>= 8
    return text

def token2str(x:str):
    text:str = ""
    x = x.replace("-","")
    for i in range(0,32,2):
        text+=chr(int(x[i:i+2],16))
    return text

async def pong() -> bytes:
    return b"\xfb"

def paint(x:int,y:int,color:tuple[int,int,int],uid:int,token:str) -> str:
    id = random.randint(0,65535)
    text = "\xfe"+int2str(x,2)+int2str(y,2)+int2str(color[0])+int2str(color[1])+int2str(color[2])+int2str(uid,3)+token2str(token)+int2str(id,4)
    return id,text
# 00000000-0000-0000-0000-000000000000

print(1)