import tempfile
import csv
import os
import logging
import textfsm
from importlib.resources import path as importresources_path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


base_path = os.path.dirname(__file__)
parent_path = os.path.dirname(base_path)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s[line:%(lineno)d ] %(levelname)s %(message)s",  # 时间 文件名 line:行号  levelname logn内容
    datefmt="%d %b %Y,%a %H:%M:%S",  # 日 月 年 ，星期 时 分 秒
    filename=parent_path + "/log/gunicorn_access.log",
    filemode="w",
)


def str_to_file_obj(text, mode="wb+"):
    f_obj = tempfile.NamedTemporaryFile(mode=mode)
    f_obj.write(text)
    # 确保 string 立即写入文件
    f_obj.flush()
    # 将文件读取指针返回到文件开头位置
    f_obj.seek(0)
    return f_obj


def textfsm_parser(raw_text: str, template_text: str) -> str:
    textfsm_data = []
    fsm_handler = None
    # 字符串转为 bytes
    template_text = template_text.encode("utf-8")
    try:
        fsm_handler = textfsm.TextFSM(str_to_file_obj(template_text))
        for obj in fsm_handler.ParseText(raw_text):
            entry = {}
            for index, entry_value in enumerate(obj):
                entry[fsm_handler.header[index]] = entry_value
            textfsm_data.append(entry)
        return textfsm_data

    except textfsm.parser.Error as tfte:
        return {"parse_error": str(tfte)}


def get_ntc_path():
    with importresources_path(
        package="ntc_templates", resource="templates"
    ) as posix_path:
        # Example: /opt/venv/netmiko/lib/python3.8/site-packages/ntc_templates/templates
        template_dir = str(posix_path)

    index = os.path.join(template_dir, "index")
    if not os.path.isdir(template_dir) or not os.path.isfile(index):
        raise ValueError("Using `pip install ntc-templates` to install.")
    return os.path.abspath(template_dir)


def get_tmpl_by_platform(platform, template_list):
    tmpl_list = []
    for tmpl in template_list:
        if platform and platform in tmpl["Platform"]:
            tmpl_list.append(tmpl["Template"])
    return tmpl_list


def parse_csv_to_list(index_file):
    template_list = []
    platform_list = []
    with open(index_file, "r") as f:
        buf = ""
        for line in f:
            if line.startswith("#") or line.startswith("\n"):
                continue
            lst = [l.strip() for l in line.split(",")]
            buf += ",".join(lst) + "\n"
    reader = csv.DictReader(str_to_file_obj(buf, mode="w+"))
    for i in reader:
        template_list.append(i)
        platform_list.append(i.get("Platform"))
    return set(platform_list), template_list


def load_template(base_dir, tmpl_name):
    try:
        with open(base_dir + "/" + tmpl_name, "r") as f:
            content = f.read()
    except:
        content = ""
    return content


app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:80",
    "http://textfsm.xdai.vip",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextFSMBody(BaseModel):
    raw_text: str
    template_text: str


platform_list, template_list = parse_csv_to_list(get_ntc_path() + "/index")


@app.post("/parser")
async def parse_textfsm(textfsm_body: TextFSMBody):
    textfsm_body = dict(textfsm_body)
    result = textfsm_parser(**textfsm_body)
    if isinstance(result, list) and len(result) > 0:
        textfsm_body["result"] = result
        logging.info(textfsm_body)
    return result


@app.get("/parser/getPlatformList")
def get_platform_list():
    return {"data": {"platform_list": platform_list}}


@app.get("/parser/getTemplateList")
def get_template_list(platform):
    tmpl_list = get_tmpl_by_platform(platform, template_list)
    return {"data": {"platform": platform, "template_list": tmpl_list}}


@app.get("/parser/loadTemplate")
def load_tmpl(template):
    base_dir = get_ntc_path()
    content = load_template(base_dir, template)
    print(content)
    return {"data": {"template": template, "content": content}}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
    # uvicorn.run(app, host="0.0.0.0", port=8000)
