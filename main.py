from fastapi import FastAPI

app = FastAPI()

@app.get("/name1/")
def read_root():
    return {"message":"Hello Karthik from GCP"}