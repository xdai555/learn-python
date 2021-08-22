import logging
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command as exec_cmd
from nornir.core.plugins.runners import RunnersPluginRegister
# from nornir.plugins.runners import ThreadedRunner
from nornir.core.plugins.register import PluginRegister
import pkg_resources
from nornir.core.helpers.jinja_helper import render_from_file
from functools import partial


# nr = InitNornir(
#     inventory = {
#         "options":{
#             "host_file": "hosts.yaml" ,
#             },
#         },
#     )

def subtask1(task):
    # print(task.name)
    return Result(host=task.host,result=task.name,failed=True)

def subtask2(task):
    # print(task.name)
    return Result(host=task.host,result=task.name, changed=True)
    
def subtask3(task):
    # print(task.name)
    return Result(host=task.host,result=task.name)

def task1(task):
    
    try:
        task.run(task=subtask1)
    except Exception as e:
        pass
    task.run(task=subtask2)
    task.run(task=subtask3)
    return Result(host=task.host, result=task.name)

# r = nr.run(task=task1,)
# print_result(r,severity_level=logging.DEBUG)


# p = PluginRegister("test")
# print(p.available)
# RUNNERS_PLUGIN_PATH = "nornir.plugins.runners"

# a = PluginRegister(RUNNERS_PLUGIN_PATH)
# a.auto_register()
# print(a.available)
# a = pkg_resources.get_entry_map("nornir-napalm")
# print(a)
