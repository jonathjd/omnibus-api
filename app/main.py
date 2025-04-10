from fastapi import FastAPI

app = FastAPI(title="Omnibus", description="Omnibus API", version="0.1.0")


@app.get("/")
async def read_root():
    return {"message": "Welcome to Omnibus!"}
