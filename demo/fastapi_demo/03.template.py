from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('index.html',{'request': request})

@app.get("/hi/{name}")
async def hi(request: Request ,name: str):
    return templates.TemplateResponse('hello.html', {'request': request, "name": name})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) 