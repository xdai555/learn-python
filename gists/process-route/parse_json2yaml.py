import json
import yaml

lis1 = []
count = 1
# json_file = './route.json'
json_file = './test.json'


with open(json_file,"r") as f:
    for i in f:
        raw_json = json.loads(i.strip())
        dict_tmp = {
            "count":count,
        }
        dict_tmp.update(raw_json)
        count = count + 1
        lis1.append(dict_tmp)
final = {"route":lis1}
with(open('route.yml', 'w')) as f1:
    yaml.safe_dump(final,stream=f1)



# test_yaml = yaml.dump(test_dict)
# #或者直接转换为文件
# new_yaml_file = open("new_file","w")
# yaml.safe_dump(test_dict,stream=new_yaml_file,default_flow_style=False)
    # print(test_dict)

# data = '{"type":"INTRA_VRF","dst_network":"1.0.1.0/24","next_hop_addr":"192.168.100.254","vrf_id":0}'
# a = json.loads(data)
# dic = yaml.dump(a)
# print(dic)