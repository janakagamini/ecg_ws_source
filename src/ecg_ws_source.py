import csv
import time
import json
from websocket import create_connection

ws = create_connection("ws://localhost:9003/stream")

FILE_NAME = 'mgh001.csv'


current_milli_time = lambda: int(round(time.time() * 1000))

with open('/home/janaka/IdeaProjects/ecg_ws_source/data/mgh001.csv', 'rt') as f:
    reader = csv.reader(f)
    count = 0
    s = ''
    for row in reader:
        dict = {
            "timestamp": current_milli_time(),
            "lead1": float(row[1]),
            "lead2": float(row[2])
        }
        ws.send(json.dumps(dict))
        time.sleep(0.003)
