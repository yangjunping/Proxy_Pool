import requests
from get_proxies import Get_Proxies
import time
from redis_operate import redis_operate
class TestProxy():
    def __init__(self):
        self.redislink = redis_operate()
    def detection(self,proxy):          #检测装置，测试百度，获取返回码判断
        # proxies={
        #     'http':'http://'+proxy,
        #     'https':'https://'+proxy,
        # }
        res=requests.get("https://www.baidu.com",proxy,timeout=10)
        if(res.status_code==200):
            # self.redislink.add(proxy)
            print("有效代理",proxy)
            return True
        else:
            print("不是有效代理")
            return False
#         conn=aiohttp.TCPConnector(verify_ssl=False)
#         async with aiohttp.ClientSession(connnector=conn) as session:
#             async with session.get("https://www.baidu.com") as res:
#                 if(res.status_code==200):
#                     self.redislink.add(proxy)
#                     print("有效IP",proxy)
#                 else:
#                 #   redis_operate.decrase(proxy)
#                     print("不是有效IP")
    def byte_to_utf(self,proxy_list):   #redis存储的byte方式转换为utf-8,列表返回
        for i in proxy_list:
            if isinstance(i, bytes):
                i = i.decode("utf-8")
                pro = 'http://' + i
                yield pro
            # ptest.detection(pro)
            # time.sleep(2)
    def first_insert(self,redislink):         #第一次插入全部获取的代理
        pro = Get_Proxies()
        proxy_list = pro.crawl_xici()
        proxy_list=self.byte_to_utf(proxy_list)
        #    loop=asyncio.get_event_loop()
        for i in proxy_list:
            if self.detection(i):
                redislink.add(i)

    def exit_test(self,redislink):                        #在已经获取的数据库里获取前三位检测
        top3_proxy=redislink.zrevrange("proxy",0,2)
        top3_list=self.byte_to_utf(top3_proxy)
        for i in top3_list:
            if self.detection(i):
                print("代理可用")
            else:
                self.redislink.decrease(i)

if __name__ == '__main__':
    redislink=redis_operate()
    redis=redislink.getredis()
    testproxt=TestProxy()
    if(redislink.isexit(redis)):
        print("redis已经有现成的代理，尽情享用吧！")
        testproxt.exit_test(redis)
    else:
        first_insert()




