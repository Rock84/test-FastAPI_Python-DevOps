import psutil
import redis

from fastapi import FastAPI

app = FastAPI()


@app.get('/memory')
def memory_limit(percent: int):
    m: int = (psutil.virtual_memory().total - psutil.virtual_memory().available) / psutil.virtual_memory().total * 100
    if m >= percent:
        return f"warning memory limit {m - percent}"
    else:
        return 'is fine'

@app.put('/put')
def new_value(percent: int):
    conn = redis.Redis(host='dev_test_bd', port=6379, db=0, decode_responses=True)
    conn.set('1', percent)
    return {conn.get('1')}

@app.post('/post')
def create_value(percent: int):
    conn = redis.Redis(host='dev_test_bd', port=6379, db=0, decode_responses=True)
    conn.set('1', percent)
    return {conn.get('1')}

@app.get('/get')
def get_value():
    conn = redis.Redis(host='dev_test_bd', port=6379, db=0, decode_responses=True)
    return {conn.get('1')}
