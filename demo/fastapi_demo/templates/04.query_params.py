from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# 直接访问路径 /items/ 会获取到 "limit" 个值
# 访问不属于路径的其他函数参数时，会被解析为“查询”参数，即：？skip=x&limit=xx
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 2):
    return fake_items_db[skip: skip + limit]

# 可以设置默认值为 None
from typing import Optional
@app.get("/items/{item_id}")
async def read_items(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 有多个路径参数和查询参数时，FastAPI 会自动识别，而且不用注意顺序
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
    ):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"desc": "长长的描述"}
        )
    return item


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)