import mbed_lstools
import os
import json

mbeds = mbed_lstools.create()
connected_devices = mbeds.list_mbeds()
json_file = os.path.join(os.getcwd(), "Board.json")

board = {
    "model": "app.board",
    "pk": -1,
    "fields": {
        "name": "",
        "state": "NOTAVAILABLE",
        "family": "...",
        "port": "SWD",
        "write_address": "0x08000000",
        "serial_number": "",
        "flash_memory_size": 0
    }
}

boards = json.load(open(json_file, 'r'))  # all existen boards
sn_boards = list(map(lambda x: x['fields']['serial_number'], boards))  # all sn of existen boards
ids_boards = list(map(lambda x: x['pk'], boards))  # all ids of existen boards
ids_boards.sort()
last_id = int(ids_boards[-1])

for device in connected_devices:
    last_id+=1
    device_name = device['platform_name']
    device_serial_number = device['target_id_usb_id']
    device_serial_port = device['serial_port']
    if device_serial_number not in sn_boards:
        # here we add new board
        board["pk"]=last_id
        board["fields"]["serial_number"] = device_serial_number
        board["fields"]["name"] = device_name
        board["fields"]["port"] = device_serial_port
        boards.append(board)
with open(json_file, 'w') as ff:
    ff.write(json.dumps(boards))
