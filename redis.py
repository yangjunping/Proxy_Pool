from redis import StrictRedis
Class redis_operate():
    def __init__(self,host,pssword):
        self.redis=StrictRedis(host=host,prot=6379,db=0,None)
    def add(self,value):
        self.redis.zadd("proxy",value,100)
    def decrease(self,value):
        self.redis.zincrby("proxy",value,-1)
    def increase(self,value):
        self.redis.zincrby("proxy", value, 1)
    def delete(self,value):
        self.redis.zremrangebyscore("proxy",0,10)

