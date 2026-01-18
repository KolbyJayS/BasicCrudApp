from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# On section parameters on fastapi