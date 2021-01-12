import requests
import time
import bluetooth
from log import write_log_file
import json
import requests

class DeviceBitable():
    def __init__(self, devices, token):
        self.devices = devices
        self.request = 0
        self.request_success = 0
        self.request_fail = 0
        self.addr = None
        self.socket = None
        self.token = token

    def authen(self, engine_id):
        try:
            mac_authen = self.get_authen(engine_id)
            if mac_authen is None:
                write_log_file("BITABLE_{0}".format(engine_id), "Thiết bị chưa được khai báo", 0)
                return False
            mess = "{\"option\":\"0\", \"value\":\"" + mac_authen + "\"}\n"
            print(mess)
            self.socket.send(mess)
            response = self.socket.recv(8096)
            response = response.decode("utf-8")
            response = json.loads(response)
            print(response)
            if int(response['code']) != 14:
                write_log_file("BITABLE_{0}".format(engine_id), "Authen fail !", 0)
                return False
            else:
                write_log_file("BITABLE_{0}".format(engine_id), "Authen success !", 1)
                return True
        except Exception as e:
            write_log_file("BITABLE_{0}".format(engine_id), "Fail to send authen !", 0)

    def get_authen(self, engine_id):
        url = "http://api.cms.beetai.com/api/boxEngine/getById/{0}".format(engine_id)

        headers = {'Authorization': 'Bearer {0}'.format(self.token)}

        res = requests.get(url, headers=headers)

        res = json.loads(res.text)

        if res['status'] != 10000:
            return None

        mac = res['data']['box']['mac_address'].replace(":", "")

        return mac + "_{0}".format(engine_id)

    def call_camera_document(self, engine_id):
        try:
            mess = "{\"option\":\"6\", \"timeout\":\"6\"}\n"
            self.socket.send(mess)
            str_res = ""
            while True:
                res = self.socket.recv(1024)
                res = res.decode("utf-8")
                find = res.find("\n")
                if find != -1:
                    res = res[0: find]
                    str_res += res
                    break
                str_res += res
            res = json.loads(str_res)
            # print(res)
            if int(res['code']) == 1:
                write_log_file("BITABLE_{0}".format(engine_id), "Read camera document success !", 1)
            else:
                write_log_file("BITABLE_{0}".format(engine_id), "Read camera document fail !", 0)
                # print("code : ", res['code'])
        except Exception as e:
            write_log_file("BITABLE_{0}".format(engine_id), "Fail to send read camera document !", 0)

    def call_camera_face(self, engine_id):
        try:
            mess = "{\"option\":\"5\", \"timeout\":\"6\"}\n"
            self.socket.send(mess)
            str_res = ""
            while True:
                res = self.socket.recv(1024)
                res = res.decode("utf-8")
                find = res.find("\n")
                if find != -1:
                    res = res[0: find]
                    str_res += res
                    break
                str_res += res
            res = json.loads(str_res)
            if int(res['code']) == 1:
                write_log_file("BITABLE_{0}".format(engine_id), "Read camera face success !", 1)
            else:
                write_log_file("BITABLE_{0}".format(engine_id), "Read camera face fail !", 0)
        except Exception as e:
            write_log_file("BITABLE_{0}".format(engine_id), "Fail to send read camera face !", 0)

    def run(self):
        while True:
            for device in self.devices:
                name_device = device[1]
                ip_lan = device[2]
                ip_wifi= device[3]

                print("name_device : ", name_device)

                engine_id = name_device.split("_")[1]

                nearby_devices = bluetooth.discover_devices(lookup_names=True)

                print(nearby_devices)

                for addr, name in nearby_devices:
                    if name == name_device:
                        self.addr = addr
                        break
                if self.addr is None:
                    write_log_file("BITABLE_{0}".format(engine_id), "Cant scan bluetooth !", 0)
                    continue
                try:
                    self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                    self.socket.connect((self.addr, 1))
                    check_authen = self.authen(engine_id)
                    print("check_authen : ", check_authen)
                    self.call_camera_document(engine_id)
                    self.call_camera_face(engine_id)
                    self.socket.close()
                    print("DONE")
                except Exception as e:
                    print(e)
                    write_log_file("BITABLE_{0}".format(engine_id), "Fail to connect to device !", 0)
            print("=================")
            time.sleep(1)


# d = DeviceBitable([1, "BITABLE_DEV", 4, 5])
# d.start()
