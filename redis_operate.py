from redis import StrictRedis
class redis_operate():
    def __init__(self):
        self.redis=StrictRedis(host="localhost",port=6379,db=0)
    def add(self,value):
        self.redis.zadd("proxy",100,value)
    def decrease(self,value):
        self.redis.zincrby("proxy",value,-1)
    def increase(self,value):
        self.redis.zincrby("proxy", value, 1)
    def delete(self,value):
        self.redis.zremrangebyscore("proxy",0,10)


