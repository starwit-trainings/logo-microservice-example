from __future__ import annotations
from typing import List
from datetime import datetime
import pathlib

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from models import Logo
from models import Info

app = FastAPI(
    title='Logo service',
    version='0.0.1',
    description='This is a sample service, that provides logo images.\n',
    servers=[{'url': 'http://localhost:8080/v0'}],
)

data = [{"name": "starwit",
         "creator": "Markus",
         "imageUri": "resources/starwit.png"},
        {"name": "starwit-bw",
         "creator": "Markus",
         "imageUri": "resources/starwit-bw.png"}]

# for Docker paths
basepath = pathlib.Path(__file__).parent.resolve()

@app.get('/info', response_model=None)
def get_info() -> Info:
    info = Info()
    info.generation_date = datetime.now()
    info.systemDescription = "a sample service"
    info.apiVersion = "0.0.1"
    return info

@app.get('/logo/all', response_model=List[Logo])
def get_all_logos() -> List[Logo]:
    result = []
    for idx, d in enumerate(data):
        l = Logo()
        l.id = idx
        l.name = d['name']
        l.creator = d['creator']
        l.imageUri = d['imageUri']
        result.append(l)
    return result

@app.get('/logo/{id}', response_model=Logo)
def get_logo_by_id(id: int) -> Logo:
    d = data[id]
    l = Logo()
    l.id = id
    l.name = d['name']
    l.creator = d['creator']
    l.imageUri = d['imageUri']
    return l

@app.get('/logo/image/{id}', response_model=bytes)
def get_logo_image(id: int) -> bytes:
    imagePath = str(basepath) + "/" + data[id]['imageUri']
    fr = FileResponse(imagePath)
    return fr

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)