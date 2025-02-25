from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello team. I have successfully hosted my API through ngrok. I am on a roll tonight."}
