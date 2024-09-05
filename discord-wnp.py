import threading
import time
from pywnp import WNPRedux
from pypresence import Presence
import config

RPC = Presence(config.client_id)
RPC.connect()


def logger(type, message):
    print(f"{type}: {message}")


WNPRedux.start(config.port, "0.1.0", logger)


def loop():
    while True:
        if WNPRedux.media_info.state == "PLAYING":
            RPC.update(
                state=f"by {WNPRedux.media_info.artist}",
                details=WNPRedux.media_info.title,
            )
        else:
            RPC.update(
                state="Idle",
            )
        time.sleep(15)


threading.Thread(target=loop, daemon=True).start()

print("Enterで終了")
input()

WNPRedux.stop()
