import redis

conn = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)
