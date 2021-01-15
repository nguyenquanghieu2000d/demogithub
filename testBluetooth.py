# import bluetooth
#
# socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# sa
# for addr, name in nearby_devices:
#     if name == "BITABLE_550":
#         addr = addr
#         break
# socket.connect(())

import json
import os

dir = "./logs/"
l = os.listdir(dir)
ll = [i for i in l if len(i.split("_")) >= 3]
print(ll)

# x = json.loads(a.read())

# x[0]["1231321234"] = "234234234"
# k = json.dumps(x)
# a.write(k)