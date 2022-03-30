from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import textfsm
import tempfile


def str_to_file_obj(text):
    f_obj = tempfile.NamedTemporaryFile()
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
        return str(tfte)


app = FastAPI()

origins = [
    "http://localhost:8080",
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


@app.post("/parser")
async def parse_textfsm(textfsm_body: TextFSMBody):
    return textfsm_parser(**dict(textfsm_body))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
