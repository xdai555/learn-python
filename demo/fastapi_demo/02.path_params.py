from fastapi import FastAPI


app = FastAPI()

# 类型验证，输入值必须是 int, 返回值会转换为 int
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# 类型验证: 字符串
@app.get("/items_str/{item}")
async def read_item_str(item: str):
    return {"item": item}


# 如果路径操作是按照顺序依次运行的,需要确保路径 /users/me 声明在路径 /users/{user_id} 之前，否则/users/{user_id} 的路径还将与 /users/me 相匹配，"认为"自己正在接收一个值为 "me" 的 user_id 参数。
@app.get("/user/me")
def read_user_me():
    return {"user_id": "当前用户"}

@app.get("/user/{user_id}")
def read_user_me(user_id: int):
    return {"user_id": user_id}


# 给访问路径配置默认值，使用户只能传递指定的参数
from enum import Enum

class Person(str, Enum):
    name1 = "zhangsan"
    name2 = "lisi"
    name3 = "wangwu"

@app.get("/names/{name}")
def get_person_name(name: Person):
    if name == name.name1:
        return {"name": name}
    if name.value == "lisi":
        return {"name": name}
    return {"name": name}


# 获取路径，结尾部分的 :path 说明该参数应匹配任意的路径

@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)