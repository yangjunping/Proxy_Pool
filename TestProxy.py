import requests
from get_proxies import Get_Proxies
import time
from redis_operate import redis_operate
class TestProxy():
    def __init__(self):
        self.redislink = redis_operate()
    def detection(self,proxy):
        # proxies={
        #     'http':'http://'+proxy,
        #     'https':'https://'+proxy,
        # }
        res=requests.get("https://www.baidu.com",proxy,timeout=10)
        if(res.status_code==200):
            self.redislink.add(proxy)
            print("有效代理",proxy)
        else:
            print("不是有效代理")
#         conn=aiohttp.TCPConnector(verify_ssl=False)
#         async with aiohttp.ClientSession(connnector=conn) as session:
#             async with session.get("https://www.baidu.com") as res:
#                 if(res.status_code==200):
#                     self.redislink.add(proxy)
#                     print("有效IP",proxy)
#                 else:
#                 #   redis_operate.decrase(proxy)
#                     print("不是有效IP")
if __name__ == '__main__':
    pro=Get_Proxies()
    proxy_list=pro.crawl_xici()
    ptest=TestProxy()
#    loop=asyncio.get_event_loop()
    for i in proxy_list:
        if isinstance(i,bytes):
            i=i.decode("utf-8")
        pro='http://'+i
        ptest.detection(pro)
        time.sleep(2)


