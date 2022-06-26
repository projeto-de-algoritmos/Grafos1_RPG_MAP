import uvicorn
import json 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import Path
from app.structures.graph import Graph
from app.edges import countries as edges


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = Graph(edges=edges)

@app.post('/find_path')
def find_path(path: Path):
    path = graph.find_shortest_path(
        start=path.source,
        end=path.destination
    )
    return dict(path=path) 

@app.get('/countries')
def get_countries():
    countries = graph.get_nodes()
    return dict(countries=countries)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)