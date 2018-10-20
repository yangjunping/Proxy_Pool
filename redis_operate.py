from redis import StrictRedis
class redis_operate():
    def getredis(self):
        self.redis=StrictRedis(host="localhost",port=6379,db=0)
        return self.redis
    def add(self,value):
        self.redis.zadd("proxy",100,value)
    def decrease(self,value):
        self.redis.zincrby("proxy",value,-1)
    def increase(self,value):
        self.redis.zincrby("proxy", value, 1)
    def delete(self,value):
        self.redis.zremrangebyscore("proxy",0,10)
    def isexit(self,redis):
        b=self.redis.zcard('proxy')
        if b>0:
            return True
        else:
            return False


