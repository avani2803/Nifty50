import time
from nsetools import Nse
from Nifty50.settings import FILE_DIR
import json
import threading


def getData():
    nse = Nse()
    data = nse.get_top_gainers()
    file =  open(FILE_DIR, "w")
    file.flush
    file.write(json.dumps(data))
    print("Successfully updated cache data")

def initThread():
    while True:
        _thread = threading.Thread(target=getData)
        _thread.start()
        time.sleep(60*5)