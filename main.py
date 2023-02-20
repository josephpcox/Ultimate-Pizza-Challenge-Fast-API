
from fastapi import FastAPI

app = FastAPI()
# Note that client_id connection and database should be secrets

@app.get("/")
def read_root():
    return {"Hello": "World"}
