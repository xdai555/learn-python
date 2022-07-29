from ttp import ttp
import json

def parse_running_config(data, template):
    parser = ttp(data=data, template=template)
    parser.parse()
    result = parser.result()[0][0]
    return result

def parse_vpn_config(vrf, config, map_name="cryto_map_common"):
    try:
        iface_id = config["interfaces"][vrf]["66.66.66.66"]["id"]
    except:
        iface_id = config["interfaces"][vrf]["66.66.66.65"]["id"]
    result = config["ipsec"][map_name][iface_id]
    result["acl"] = config["acl"]["acc_acl_" + vrf]
    result["isa_profile"] = config["isakmp"]["profile"]["isa_profile_" + vrf]
    result["isa_profile"]["keyring"] = config["isakmp"]["keyring"]["keyring_" + vrf]
    result["route"] = config["route"].get(vrf, [])
    return result

config = parse_running_config("./test.log", "./1.txt")
with open("result.json", 'w') as f:
    f.write(json.dumps(config))

# for i in config["ipsec"]["cryto_map_common"].values():
#     print(i.get("isa_profile"),i.get("is_complete","1"))


result = parse_vpn_config("9e3rszehv0qlxijzv03bd5rhz", config)
from pprint import pprint
pprint(result)

# import csv


# def get_device_list(filename):
#     """csv to dict"""
#     with open(filename) as f:
#         reader = csv.DictReader(f)
#         return list(reader)

# from netmiko import ConnectHandler as ch

# CISCO_CMD = "show run"
# H3C_CMD = "dis curr"


