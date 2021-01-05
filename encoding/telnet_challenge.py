import telnetlib
import json
from ascii_decode import *

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)




while(True):
    received = json_recv()
    print("Received: ")
    print(received)
    decoded = ''
    if received["type"] == "utf-8":
        decoded = decode_list(received["encoded"])
    elif received["type"] == "hex":
        decoded = hex_to_str(received["encoded"])
    elif received["type"] == "base64":
        decoded = base64_decode(received["encoded"])
    elif received["type"] == "bigint":
        decoded = base16_decode(received["encoded"])
    elif received["type"] == "rot13":
        decoded = rot(received["encoded"], 13)

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

