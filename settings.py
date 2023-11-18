import redis

conn = redis.Redis(host='dev_test_bd', port=6379, db=1, decode_responses=True)
