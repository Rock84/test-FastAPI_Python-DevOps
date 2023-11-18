import psutil

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


from settings import conn

app = FastAPI()


class InputModel(BaseModel):
    value: str = Field(default='', max_length=64, min_length=1)


@app.get('/memory')
def memory_limit(percent: int):
    m: int = (psutil.virtual_memory().total - psutil.virtual_memory().available) / psutil.virtual_memory().total * 100
    if m >= percent:
        return f"warning memory limit {m - percent}"
    else:
        return 'is fine'


@app.put('/put')
def new_value(form: InputModel):
    if conn.set(name='key', value=form.value, xx=True):
        return form
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post('/post')
def create_value(form: InputModel):
    if conn.set(name='key', value=form.value, nx=True):
        return form
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@app.get('/get')
def get_value():
    return conn.get('key')
