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


def int2list(x:int,dig:int=1)->list[int]:
    data:list[int] = []
    for i in range(0,dig):
        data.append(x & 0xff)
        x >>= 8
    return data

def token2str(x:str)->list[int]:
    data:list[int] = []
    x = x.replace("-","")
    for i in range(0,32,2):
        data.append(int(x[i:i+2],16))
    return data

async def pong() -> bytes:
    return b"\xfb"

async def paint(x:int,y:int,color:tuple[int,int,int],uid:int,token:str) -> tuple[int, list[int]]:
    id = random.randint(0,65535)
    text = [0xfe]+int2list(x,2)+int2list(y,2)+int2list(color[0])+int2list(color[1])+int2list(color[2])+int2list(uid,3)+token2str(token)+int2list(id,4)
    return id,text
# 00000000-0000-0000-0000-000000000000


async def bytes2int(raw:bytes,st:int,ed:int):
    num:int = 0
    for i in range(0,ed-st):
        num+=raw[i+st]*(1<<(8*i))
    return num


async def set_col(raw:bytes):
    x = await bytes2int(raw,1,3)
    y = await bytes2int(raw,3,5)
    r = await bytes2int(raw,5,6)
    g = await bytes2int(raw,6,7)
    b = await bytes2int(raw,7,8)

    # 在这里写你自己的处理方法
    ...

async def pt_res(raw:bytes,ress:dict[int,int]|None=None):
    id = await bytes2int(raw,1,5)
    op = await bytes2int(raw,5,6)
    op_text = ""
    if not ress is None:
        ress[id]=op
    match op:
        case 0xef:
            op_text = "Successful."
        case 0xee:
            op_text = "Too fast."
        case 0xed:
            op_text = "Token error."
        case 0xec:
            # 这本来是格式错误的，但是格式错误会直接掐连接
            op_text = ""
        case 0xeb:
            op_text = "Promission error."
        case 0xea:
            op_text = "Server error."
        case _:
            raise TypeError(f"op {op} not found.")
    
    print(id,op,op_text)

    
    # 在这里写你自己的处理方法
    ...