from ptrlib import *


def send_character(char):
    io.sendlineafter("your choice> ", bytes(char, "utf-8"))


io = Socket("nc 34.170.146.252 30573")

# 10行飛ばす
for _ in range(10):
    print(io.recvline())

stock = {"a": 30, "b": 60, "c": 20, "d": 50, "e": 40}

for key in stock:
    for _ in range(stock[key]):
        send_character(key)
        print(io.recvline())
        print(io.recvline())

send_character("a")
print(io.interactive())
