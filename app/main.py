from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.logging_config import setup_logging

from dotenv import load_dotenv
import os


load_dotenv()

setup_logging()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("Origin", "*"),
    allow_credentials=True,
    allow_methods=os.getenv("Allow_Methods", "*"),
    allow_headers=["*"],
)
@app.get('/')
def home():
    return {"Hello": "World"}

app.include_router(router, prefix='/api/v1/news')

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
