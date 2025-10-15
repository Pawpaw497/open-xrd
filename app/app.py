# app.py
import pandas as pd
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
database = []  # 模拟内存数据库
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 桌面端和后端同机，直接放开
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    # 转成前端方便展示的格式
    data = {
        "columns": list(df.columns),
        "rows": df.to_dict(orient="records")
    }
    return data


class Item(BaseModel):
    name: str
    value: int


# @app.post("/add")
# def add_item(item: Item):
#     database.append(item.model_dump())
#     return {"message": "added", "data": database}


# @app.get("/list")
# def list_items():
#     return {"data": database}
