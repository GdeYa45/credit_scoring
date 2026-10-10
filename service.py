from fastapi import FastAPI
from pydantic import BaseModel

class ClientData(BaseModel):
    age: int
    income: float
    education: bool
    work: bool
    car: bool

app = FastAPI()

@app.post('/score')
def score(data: ClientData):
    approved = data.income > 50 or (data.education and data.work)
    return {'approved':approved}