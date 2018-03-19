'''
Created on 18.03.2018

@author: geri
'''
from stem import Signal
from stem.control import Controller
print("TEST")
def set_new_ip():
    """Change IP using TOR"""
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='my_password')
        controller.signal(Signal.NEWNYM)
        
import requests
 
local_proxy = '127.0.0.1:8118'
http_proxy = {
    'http': local_proxy
    #'https': local_proxy
}
 
current_ip = requests.get(
    url='http://icanhazip.com/',
    proxies=http_proxy,
    verify=False
)
#set_new_ip()



    
print(current_ip.text)
      
#       https://www.privoxy.org/user-manual/quickstart.html
#       http://tuxdiary.com/2015/04/10/tor-privoxy/
#       https://www.privoxy.org/faq/misc.html#T
# https://www.deepdotweb.com/2015/09/05/tutorial-installing-tor-with-privoxy/
# https://www.vanimpe.eu/2014/07/24/use-privoxy-tor-increased-anonymity/
# https://dm295.blogspot.co.at/2016/02/tor-ip-changing-and-web-scraping.html
