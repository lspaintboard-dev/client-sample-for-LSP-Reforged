import random

endpoint = ""

def int2str(x:int,dig:int=1)->str:
    text:str = ""
    num:list[int] = []
    while(x):
        num.append(x%256)
        x = x//256
    for _ in range(len(num),dig):
        text+="\x00"
    for each in reversed(num):
        text+=chr(each)
    return text

def token2str(x:str):
    text:str = ""
    x = x.replace("-","")
    for i in range(0,32,2):
        text+=chr(int(x[i:i+2],16))
    return text

def pong() -> str:
    return "\xfb"

def paint(x:int,y:int,color:tuple[int,int,int],uid:int,token:str) -> str:
    id = random.randint(0,65535)
    text = "\xfe"+int2str(x,2)+int2str(y,2)+int2str(color[0])+int2str(color[1])+int2str(color[2])+int2str(uid,3)+token2str(token)+int2str(id,2)
    return id,text
# 00000000-0000-0000-0000-000000000000

print(1)