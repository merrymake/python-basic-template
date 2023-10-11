from merrymake.merrymake import Merrymake
from merrymake.envelope import Envelope

def handle_hello(payloadBytes: bytes, envelope: Envelope):
    payload = payloadBytes.decode('utf-8')
    Merrymake.reply_to_origin({
        "content": f"Hello, { payload }!"
    })

def main():
    (Merrymake.service()
        .handle("handle_hello", handle_hello))

if __name__ == "__main__":
    main()
