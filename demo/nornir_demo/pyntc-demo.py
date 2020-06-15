# import pyntc
# from napalm import get_network_driver
#
#
# driver = get_network_driver('ios')
# driver = driver('10.1.1.10','r1','cisco',optional_args={'secret':'cisco'})
# driver.open()
# # print(driver.get_ntp_servers())
# startup = driver.get_config(retrieve='startup')['startup']
# # print(startup)
# # with open('startup.cfg','w') as f:
# #     f.write(startup)
# print(driver.compare_config())
from  nornir import InitNornir
from test_task import napalm_compare_config as compare_config
nr = InitNornir()
print(nr.inventory.hosts)
result = nr.run(task=compare_config)
print(result['r1'][-1])