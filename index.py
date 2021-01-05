import requests
import time
import bluetooth

# class DeviceBitable:
#     def __init__(self, device):
#         self.name = device[1]
#         self.ip_lan = device[2]
#         self.id_wifi= device[3]
#         self.request = 0
#         self.request_success = 0
#         self.request_fail = 0
    
#     def start(self):
#         while True:


nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))