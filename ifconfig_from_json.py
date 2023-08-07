import os
import json

json_path = "test_network_config.json" #change with the name of (or path to) your json file

json_file = open(json_path, "r")

json_data = json_file.read()

json_dictionary = json.loads(json_data)  #file is opened, read and parsed into a dictionary (in this order)

for config in json_dictionary["IPConfiguration"]: #IPConfiguration is the single key which is assigned to a list of aspects
    main_interface_mtu = 0
    if (config["mtu"] >= main_interface_mtu):
            main_interface_mtu = config["mtu"]
    if (str(config["vlan"]) == "-1"): #no vlan 
        os.system("sudo ip addr add {}/{} dev {}".format(config["localIp"],config["localPrefix"],config["interface"])) 
        os.system("sudo ip link set {} mtu {}".format(config["interface"],main_interface_mtu))  #mtu set up
        os.system("sudo ip link set {} {}".format(config["interface"],config["status"]))   #vlan is up
    else:
        os.system("sudo modprobe 8021q")
        os.system("sudo vconfig add {} {}".format(config["interface"],config["vlan"]))   #vlan created
        os.system("sudo ip addr add {}/{} dev {}.{}".format(config["localIp"],config["localPrefix"],config["interface"],config["vlan"]))  #ip set up with prefix
        os.system("sudo ip link set {}.{} mtu {}".format(config["interface"],config["vlan"],config["mtu"]))  #mtu set up
        os.system("sudo ip link set {}.{} {}".format(config["interface"],config["vlan"],config["status"]))   #vlan is up