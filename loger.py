from functools import wraps
from datetime import datetime


def saveInfoToFile(info:str):
    with open("logger.txt" , "a") as file:
        file.write(info + "\n")

def ResponseDecor(func):
    @wraps(func)

    def inner(*args,**kwargs):
        info = "Get request at " + str(datetime.now())
        saveInfoToFile(info)

        rezult = func(*args, **kwargs)
        status = rezult.decode().split("\n")[0]

        info = "Status of Request - " + status + "\n"
        info += "Sent request at " + str(datetime.now()) + "\n"
        saveInfoToFile(info)
        return rezult

    
    return inner


def ParseRequelstDecor(func):
    @wraps(func)
    def inner(*args,**kwargs):
        type1, path = func(*args, **kwargs)
        info = "Type of Request - " + type1 + " . To adress - " + path
        saveInfoToFile(info)
        return type1, path       
    return inner

   