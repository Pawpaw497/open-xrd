# run.py
import threading

import uvicorn

from app.views.app import app
from app.views.gui import run_gui


def run_api():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")


if __name__ == "__main__":
    t = threading.Thread(target=run_api, daemon=True)
    t.start()
    run_gui()
