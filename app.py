from merrymake import Merrymake
from merrymake.merrymimetypes import MerryMimetypes
from merrymake.envelope import Envelope

def handle_hello(payloadBytes: bytearray, envelope: Envelope):
    payload = bytes(payloadBytes).decode('utf-8')
    Merrymake.reply_to_origin(f"Hello, {payload}!", MerryMimetypes.txt)

def main():
    (Merrymake.service()
        .handle("handle_hello", handle_hello))

if __name__ == "__main__":
    main()
