from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()
class iris(BaseModel):
	a:float
	b:float
	c:float
	d:float
	e:float
	f:float
 

from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

#we are loading the model using pickle
model = pickle.load(open('model.pkl', 'rb'))

@app.get("/")
def home():
	return {'ML model for Iris prediction'}

@app.post('/make_predictions')
async def make_predictions(features: iris):
	return({"prediction":str(model.predict([[features.a,features.b,features.c,features.d,features.e,features.f]])[0])})

"""
if _name_ == "_main_":
	uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
"""