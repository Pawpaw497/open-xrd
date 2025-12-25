# app.py
import pandas as pd
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

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
    data = np.loadtxt(file.file)

    if data.ndim != 2 or data.shape[1] < 2:
        raise HTTPException(400, "File must have at least two columns")

    x = data[:, 0]
    y = data[:, 1]

    return {
        "x": x.tolist(),
        "y": y.tolist(),
        "meta": {
            "source": file.filename,
            "x_label": "2θ (deg)",
            "y_label": "Intensity (a.u.)"
        }
    }
