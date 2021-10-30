from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
import random
import uvicorn
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
import numpy as np

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
model = pickle.load(open('model.pkl', 'rb'))
class iris(BaseModel):
	Category: int
	sellable_online: int
	other_colors: int
	depth: int
	height: int
	width: int

@app.get("/")
def home(request: Request):
	return templates.TemplateResponse("form.html", {"request": request})


@app.post('/predict', response_class=HTMLResponse)
async def make_predictions(request: Request, Category: int = Form(...), sellable_online: int = Form(...),other_colors: int = Form(...),depth: int = Form(...),height: int = Form(...),width: int = Form(...)):

    result = model.predict([[int(Category), int(sellable_online), int(other_colors),int(depth),int(height), int(width)]])[0]
    return templates.TemplateResponse("form.html", {"request": request, "result":result})

