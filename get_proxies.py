import requests
from lxml import etree
class Get_Proxies():
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"}
    def crawl_xici(self):
        res = requests.get("http://www.xicidaili.com/", headers=self.headers)
        file=open("xici.html","w+")
        file.write(res.text)
        html=etree.parse("xici.html",etree.HTMLParser())
        result_ip=html.xpath("//tr[@class='odd']/td[2]/text()")
        result_port = html.xpath("//tr[@class='odd']/td[3]/text()")
        for i in range(len(result_ip)):
            result=result_ip[i]+":"+result_port[i]
            yield result
        return result





