import textfsm
import tempfile
from pprint import pprint
 
def str_to_file_obj(text):
    f_obj = tempfile.NamedTemporaryFile()
    f_obj.write(text)
    # 确保string立即写入文件
    f_obj.flush()
    # 将文件读取指针返回到文件开头位置
    f_obj.seek(0)
    return f_obj


def textfsm_parser(raw_text: str, template_text: str) -> str:
    textfsm_data = []
    fsm_handler = None
    template_text = template_text.encode('utf-8')
    try:
        fsm_handler = textfsm.TextFSM(str_to_file_obj(template_text))
        for obj in fsm_handler.ParseText(raw_text):
            entry = {}
            for index, entry_value in enumerate(obj):
                entry[fsm_handler.header[index]] = entry_value
            textfsm_data.append(entry)
        return textfsm_data

    except textfsm.parser.Error as tfte:
        return str(tfte)

raw_text = r'''IP
192.168.1.1
IP
192.168.1.12
IP
192.168.1.13
IP
192.168.1.14'''
template_text = '''Value IPADD (\d+(\.\d+){3})

Start
  ^IP
  ^${IPADD} -> Record'''

pprint(raw_text)
pprint(template_text)
ret = textfsm_parser(raw_text, template_text)
print(ret)