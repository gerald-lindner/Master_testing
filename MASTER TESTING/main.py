'''
Created on 06.07.2016
@author: Gerald Lindner
'''

#tips: response.status 
#C:\Program Files\Python35\Lib\site-packages\scrapy-1.1.0-py3.5.egg\scrapy\settings
import requests #no idea what it does
from stem import Signal
import logging
import os #go get paths
import scrapy #the crawler import
import re #for finding patterns
import pandas as pd #for handling tables
from scrapy.crawler import CrawlerProcess #neccasary?
logger = logging.getLogger('mycustomlogger')
 #search engine
url_1="https://www.google.de/search?q=site%3A"
url="www.care.at"#list of url
path_cnames="C:/Users/geri/Dropbox/02_Main/04_Uni/02_MA Arbeit/final_output.xlsx"
#path_cnames="D:/04_Dropbox/Dropbox/02_Main/04_Uni/02_MA Arbeit/final_output.xlsx"
cnames=pd.read_excel(path_cnames,"Sheet1")
cnames_out=(cnames['de_man'])

path_out = os.path.join(os.path.expanduser('~'), 'Documents', 'MA_output.xlsx')
#path1 = os.path.join(os.path.expanduser('~'), 'Documents', 'ODA_2014_names_test.csv')
#path2 = os.path.join(os.path.expanduser('~'), 'Documents', 'ODA_2014_names_test.csv')
number=[]
url_out=[]
all_urls=[]
#creating the urls, must be done in loop before: from 0 works; arrays start at 1 :-)
#for y in range(0,len(cnames_out)):
for y in range(0,100):
    all_urls.append(url_1+url+"+"+cnames_out[y])
    

#start of tor 
from stem.control import Controller
with Controller.from_port(port = 9051) as controller:
    controller.authenticate(password = 'my_password')
    controller.signal(Signal.NEWNYM)
    controller.close()
SCRAPY_SETTINGS_MODULE="ma_setting.py"
class googlengo(scrapy.Spider): #scrapy class, contains everything
        handle_httpstatus_list = [301, 302]
        name = 'googlengo'
        start_urls = all_urls
        custom_settings = {
            'REDIRECT_ENABLED': False
        }
        def parse(self,response):
            i=0;
            print(response.status)
            if response.status==302:
                print ("NOPE DI DOPE ")
#                 url_out.append[cnames_out[i]]
#                 number.append("NA")
            else:
                number_t=response.xpath('//div[@id="resultStats"]/text()').extract()
                number_t=re.findall("(\d*) ",number_t[0])
                number.append(number_t[0])
                url_out.append(cnames_out[i])
#             except:
#                 print("FUNKT NICHT")
#                 url_out.append[cnames_out[i]]
#                 number.append("NA")               
            i=i+1
process = CrawlerProcess()
process.crawl(googlengo)
process.start()
    
number_df=pd.DataFrame(number)
ur_out_df=pd.DataFrame(url_out)
#print(number_df)
#print(names)
frames=[ur_out_df,number_df]
all_df=pd.concat(frames,axis=1,join='outer')
#writing all_df to xlsx
writer=pd.ExcelWriter(path_out)
all_df.to_excel(writer,'Sheet1')
writer.save()
print(all_df)
