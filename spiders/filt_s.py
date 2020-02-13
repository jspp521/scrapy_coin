import scrapy,re

class filt_s(scrapy.Spider):
    name='filt_s'
    coin=''

    def start_requests(self):
        urls={
            'https://cn.etherscan.com/token/generic-tokentxns2?contractAddress='+coin+'&mode=&m=normal&p=1'
        }

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        item={}
        item['value']=[]
        item['to']=[]
        item['from1']=[]
        item['time']=[]

        for i in range(26):
            _value=response.xpath('/html/body/div[2]/div[2]/table/tbody/tr['+str(i)+']/td[7]/text()').extract_first()
            _from=response.xpath('/html/body/div[2]/div[2]/table/tbody/tr['+str(i)+']/td[4]/a/text()').extract_first()
            _to=response.xpath('/html/body/div[2]/div[2]/table/tbody/tr['+str(i)+']/td[6]/a/text()').extract_first()
            _time=response.xpath('/html/body/div[2]/div[2]/table/tbody/tr['+str(i)+']/td[3]/span/text()').extract_first()
            if _value and _from and _to and _time:
                item['value'].append(_value)
                item['from1'].append(_from)
                item['to'].append(_to)
                item['time'].append((_time))

        _t=response.xpath('/html/body/div[2]/div[2]/div/div/ul/li[4]/a/@href').extract_first()
        if _t is not None:
           _t=re.findall("move\('(.*?)'\)",_t,re.S)
           if _t is not None:
               _t='https://cn.etherscan.com/token/'+_t[0] 
               yield scrapy.Request(_t,callback=self.parse)

        yield item