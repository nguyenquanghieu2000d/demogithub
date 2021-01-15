import threading
from datetime import datetime

import time
import bluetooth
from log import write_log_file
import json
import requests


class DeviceBitable(threading.Thread):


    def __init__(self, device, token):
        threading.Thread.__init__(self)
        self.timesleep = 2
        self.status = 0
        self.device = device
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
                write_log_file("BITABLE_{0}".format(engine_id), "bluetooth" "Thiết bị chưa được khai báo", 0)
                return False
            mess = "{\"option\":\"0\", \"value\":\"" + mac_authen + "\"}\n"
            print(mess)
            self.socket.send(mess)
            response = self.socket.recv(8096)
            response = response.decode("utf-8")
            response = json.loads(response)
            print(response)
            if int(response['code']) != 14:
                self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Authen fail !", 0)
                return False
            else:
                self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Authen success !", 1)
                return True
        except Exception as e:
            self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Fail to send authen !", 0)

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
                self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Read camera document success !", 1)
            else:
                self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Read camera document fail !", 0)
                # print("code : ", res['code'])
        except Exception as e:
            write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Fail to send read camera document !", 0)

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
                self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Read camera face success !", 1)
            else:
                self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Read camera face fail !", 0)
        except Exception as e:
            self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Fail to send read camera face !", 0)

    def W_call_camera_face(self, option, engine_id, ip, Type):
        resp = requests.get('http://' + ip + ':8096/bitable?option=' + option + '&timeout=6')
        # print("Connect DONE !!!!")
        if int(resp.json()['code']) == 1:
            self.write_log_file("BITABLE_{0}".format(engine_id), Type, "Read camera document success !", 1)
        else:
            self.write_log_file("BITABLE_{0}".format(engine_id), Type, "Read camera document fail !", 0)

    def W_call_camera_document(self, option, engine_id, ip, Type):
        resp = requests.get('http://' + ip + ':8096/bitable?option=' + option + '&timeout=6')
        # print("Connect DONE !!!!")
        if int(resp.json()['code']) == 1:
            self.write_log_file("BITABLE_{0}".format(engine_id), Type, "Read camera document success !", 1)
        else:
            self.write_log_file("BITABLE_{0}".format(engine_id), Type, "Read camera document fail !", 0)

    def pause(self):
        self.status = 0

    def continues(self):
        self.status = 1

    def run(self):
        while True:
            print(self.status)
            if self.status == 0:
                while True:
                    time.sleep(1)
                    if self.status == 1:
                        break
            print("/////////// CHECKING DEVICE " + str(self.device[0]) + " ///////////////")
            name_device = self.device[1]
            ip_lan = self.device[2]
            ip_wifi = self.device[3]

            print("name_device : ", name_device)
            print("ip_lan: ", ip_lan)
            print("ip_wifi", ip_wifi)
            engine_id = name_device.split("_")[1]

            nearby_devices = bluetooth.discover_devices(lookup_names=True)

            print("===================== BLUETOOTH =====================")
            print("=== NEARBY DEVICE ===")
            print(nearby_devices)
            for addr, name in nearby_devices:
                if name == name_device:
                    self.addr = addr
                    break
            if self.addr is None:
                print("Cant scant device !!!")
                self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Cant scan device !", 0)
                # continue
            else:
                try:
                    self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                    self.socket.connect((self.addr, 1))
                    check_authen = self.authen(engine_id)
                    print("check_authen : ", check_authen)
                    self.call_camera_document(engine_id)
                    # print("Bluetooth OK4")
                    self.call_camera_face(engine_id)
                    self.socket.close()
                    print("DONE")
                except Exception as e:
                    print(e)
                    #     print("error")
                    self.write_log_file("BITABLE_{0}".format(engine_id), "bluetooth", "Fail to connect to device !", 0)
            print("=====================   LAN   ======================")
            print("Connecting LAN ...")

            try:
                self.W_call_camera_face("5", engine_id, ip_lan, "LAN")
                print("Connect cameraface LAN successful")
                self.W_call_camera_document("6", engine_id, ip_lan, "LAN")
                print("Connect cameradocument LAN successful")
            except:
                self.write_log_file("BITABLE_{0}".format(engine_id), "LAN", "Something wrong !", 0)
                pass

            print("=====================   Wifi   ======================")
            print("Connecting Wifi ...")

            try:
                if ip_wifi == "":
                    print("Device dont have Wifi ip !")
                    self.write_log_file("BITABLE_{0}".format(engine_id), "Wifi", "Device dont have Wifi ip !", 0)
                self.W_call_camera_face("5", engine_id, ip_wifi, "Wifi")
                print("Connect cameraface Wifi successful")
                self.W_call_camera_document("6", engine_id, ip_wifi, "Wifi")
                print("Connect cameradocument Wifi successful")
            except:
                self.write_log_file("BITABLE_{0}".format(engine_id), "Wifi", "Something wrong !", 0)
                pass

            print("")
            print("=======  DONE ==========")
            time.sleep(self.timesleep)

    def write_log_file(self, device, type, mess, type_mess):
        try:
            self.file_score = open("./logs/"+ device +"_score.json", "r")
        except:
            self.file_score = open("./logs/" + device + "_score.json", "x")
            self.file_score.close()
            self.file_score = open("./logs/" + device + "_score.json", "r")
        a = self.file_score.read()
        self.file_score.close()

        # file_score_ = open("./logs/Score.json", "r")


        try:
            a_json = json.loads(a)
            k = a_json[device]
        except:
            a_json = dict()
            a_json[device] = {
                "Wifi": [0, 0, 0],
                "LAN": [0, 0, 0],
                "bluetooth": [0, 0, 0]
            }
            k = a_json[device]
        # print("--------------------------")
        # print(json.dumps(k))
        # print( k[type][0])
        # print(k["LAN"][0])
        # print(k["Wifi"][0])
        if type_mess == 1:

            k[type][0] = k[type][0] + 1
            # k[1] = k[1] + 1
            k[type][2] = k[type][0] + k[type][1]
        else:
            k[type][1] = k[type][1] + 1
            k[type][2] = k[type][0] + k[type][1]
        a_json[device] = k
        a_text = json.dumps(a_json)

        self.file_score = open("./logs/"+ device +"_score.json", "w")
        self.file_score.write(a_text)
        self.file_score.close()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %d-%m-%Y")
        file_log = open("logs/{}.log".format(device), "a+")
        line = "{0}\t{1}\t{2}\t{3}\n".format(current_time, type, mess, type_mess)
        file_log.write(line)
        file_log.close()
# d = DeviceBitable([1, "BITABLE_DEV", 4, 5])
# d.start()
