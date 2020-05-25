#!/usr/bin/env python
# -*- coding:utf-8 -*-
from netmiko import ConnectHandler as ch
import time
from datetime import datetime
import pandas as pd
from multiprocessing.pool import ThreadPool


def get_device_info(filename):
    """
    读取excel文件，excel第一行为表头，且至少应包含host:IP地址、username:用户名、password:登录密码、device_type:设备型号、
    session_log:操作记录保存的文件名
    设备型号根据实际情况应为 hp_comware、cisco_ios、huawei 等。
    :param filename: str,excel 文件绝对路径
    :return: list, 每一行登录信息保存为字典形式，汇总为列表
    """
##    root_dir = os.getcwd()
    df = pd.read_excel(filename)
    device_info_list = df[['host', 'username', 'password', 'device_type', 'session_log']].to_dict(orient='records')
    return device_info_list


def login(device_info):
    global conn
    start_timer = datetime.now()
    try:
        conn = ch(**device_info, session_timeout=200, global_delay_factor=2)
    except Exception:
        # print(f"{device_info['session_log']} 连接失败,查看是否有登录权限/账号密码是否正确。")
        FAILED.append(device_info['session_log'])
    if device_info['device_type'] == 'hp_comware':
        conn.send_command(HP_COMMAND)
        # conn.read_until_pattern(r'.*(return\b)|(end\b).*')
    elif device_info['device_type'] == 'huawei':
        conn.send_command(HW_COMMAND)
    else:
        # conn.send_command(CISCO_COMMAND,expect_string=r'.*[(ore)(ORE)].*')
        conn.send_config_set(TEST)      # 针对现网迈普设备，more off == screen disable
        # conn.read_until_pattern(r'.*(return\b)|(end\b).*')
    time.sleep(10)
##    if conn.read_until_pattern(r'.*(return\b)|(end\b).*'):
    # if conn.read_until_prompt():
        # conn.close_session_log()
        # conn.disconnect()
    print(f"备份 {device_info['session_log']}\t共耗时\t {datetime.now() - start_timer}秒")



def main():
    i = int(input('备份后的配置文件保存在脚本同级目录。\n输入线程数（同时连接设备的数量）：'))
    pool = ThreadPool(i)
    filename = input('输入设备信息文件名（如：test.xlsx）：')
    print('正在执行命令中……')
    t = datetime.now()
    try:
        pool.map(login, get_device_info(filename))
    except:
        print('文件不存在或文件内容格式不正确。请检查！')
    print(f'Total Time: {datetime.now() - t }.\n以下执行失败：')
    for i in FAILED:
        print(i)

HP_COMMAND = 'display mac-address'
HW_COMMAND = 'display cur'
CISCO_COMMAND = 'show run'
TEST = ['do more off','do show run', 'show run']
FAILED = []

if __name__ == '__main__':
    main()
    input()
