import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import Path


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/find_path')
def find_path(path: Path):
    pass 


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)