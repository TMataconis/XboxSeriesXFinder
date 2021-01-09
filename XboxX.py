#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:03:43 2020

@author: thomasmataconis
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os


def check_BB_available(url,headers):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("button",text='Sold Out')
    if (title is  None):
        send_mail(url)

def check_W_available(url,headers):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find("div",text='Oops! This item is unavailable or on backorder.')
    if (title is None):
        send_mail(url)
        
        
#def check_T_available(url,headers):
#    page = requests.get(url, headers=headers)
#    soup = BeautifulSoup(page.content, 'html.parser')
#    title = soup.find('a',text='Xbox Series X Console')
#    print(title)
#    #print(soup)
        
#def check_Microsoft(url,headers):
#    page = requests.get(url, headers=headers)
#    soup = BeautifulSoup(page.content,'html.parser')
#    title = soup.find_all("span",{"class": "retline retstockbuy"})
#    title = soup.select(".c-dialog f-flow hatchDialog")
#    print(title)

def check_L(url,headers):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(text='Sold Out')
    if (title is None):
        send_mail(url)

def check_N(url,headers):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(text='CURRENTLY SOLD OUT')
    if (title is None):
        send_mail(url)
        
def check_Micro(url,headers):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(text='Out of stock')
    if (title is None):
        send_mail(url)

#def check_amazon(url,headers):
#    page = requests.get(url, headers=headers)
#    soup = BeautifulSoup(page.content,'html.parser')
#    title = soup.find(text="Xbox Series X")
#    print(title)
#    if (title is None):
#        send_mail(url)
         
def send_mail(url):
    os.system('afplay /Users/thomasmataconis/Desktop/air_raid.wav&')
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('thmsmtcns@gmail.com','Tomaeux1')
    subject = 'Xbox X Available!'
    body = 'Check the link!! \n' + url
    
    msg = f"Subject: {subject} \n\n{body}"
    
    server.sendmail(
            'thmsmtcns@gmail.com', 
            'thmsmtcns@gmail.com',
            msg
            )
    print('EMAIL SENT')
    server.quit()


def main():
    bestBuyURL = 'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324'
    walmartURL = 'https://www.walmart.com/ip/Xbox-Series-X/443574645'
    #targetURL = 'https://www.target.com/c/xbox-series-x-video-games/-/N-fd2hh?lnk=snav_rd_xbox_series_x'
    #microsoftURL = 'https://www.xbox.com/en-US/consoles/xbox-series-x?xr=shellnav#purchase'
    lenovoURL = 'https://www.lenovo.com/us/en/accessories-and-monitors/consumer-electronics/gaming-consoles/Microsoft-Xbox-Series-X-game-console-1-TB-SSD/p/78015889?clickid=3TCSPGx6txyLTXqwUx0Mo38ZUkE39WwJ3WNUWA0&irgwc=1&PID=221109&acid=ww%3Aaffiliate%3Abv0as6'
    #neweggURL = 'https://www.newegg.com/p/N82E16868105273?nm_mc=AFC-RAN-COM&cm_mmc=AFC-RAN-COM&utm_medium=affiliates&utm_source=afc-Future+Publishing+Ltd&AFFID=2294204&AFFNAME=Future+Publishing+Ltd&ACRID=1&ASUBID=tomsguide-us-5288776448554119000&ASID=https%3A%2F%2Fwww.tomsguide.com%2Fnews%2Fwhere-to-buy-xbox-series-x-stock&ranMID=44583&ranEAID=2294204&ranSiteID=kXQk6.ivFEQ-qKTYZP45O2pDSK_nEplaVg#'
    #gameStopURL = 'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x/B224744V.html?utm_source=rakutenls&utm_medium=affiliate&utm_content=Future+Publishing+Ltd&utm_campaign=10&utm_kxconfid=tebx5rmj3&cid=afl_10000087&affID=77777&sourceID=kXQk6.ivFEQ-Kki285_qAaxPN8QFmPE8tg'
    #microsoftURL = 'https://www.microsoft.com/en-us/p/xbox-series-x/8WJ714N3RBTL/P1LV?ranMID=24542&ranEAID=kXQk6*ivFEQ&ranSiteID=kXQk6.ivFEQ-QC33yXYYNOhxb.5URTFGOg&epi=kXQk6.ivFEQ-QC33yXYYNOhxb.5URTFGOg&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=%28ir__gjiaq3sa9okfqgdykk0sohzn332xsbelvtzmvu1y00%29%287593%29%281243925%29%28kXQk6.ivFEQ-QC33yXYYNOhxb.5URTFGOg%29%28%29&irclickid=_gjiaq3sa9okfqgdykk0sohzn332xsbelvtzmvu1y00'
    #amazonURL = 'https://www.amazon.com/dp/B08H75RTZ8/?coliid=I1EAWQQ5BMP08I&colid=1OY7Q3QURQPHD&psc=1&ref_=lv_ov_lig_dp_it&th=1'
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    
    counter = 0
    while(True):
        try:
            check_BB_available(bestBuyURL,headers)
        except(ConnectionError):
            print('Connection Failed')
            
        #check_W_available(walmartURL,headers)
        #check_L(lenovoURL,headers)
        #check_N(neweggURL,headers)
        #check_Micro(microsoftURL,headers)
        counter += 1
        print(counter)
        hour = time.localtime().tm_hour
        minute = time.localtime().tm_min
        sec = time.localtime().tm_sec
        ampm = ""
        if (hour > 12):
            ampm = "PM"
        else:
            ampm = "AM"
            
        print(hour%12,":",minute,".",sec,ampm)
           
#        if hour == 23:
#           print("sleeping for", ((60 - minute)*60 + 15 - sec), "seconds\n")
#           time.sleep((60 - minute)*60 + 15 - sec)
#                
#        elif hour == 0 and minute < 30:
#            #print("sleeping for", (60*5), 'seconds\n')
#            time.sleep(60*4)
#                
#        else :
#            time.sleep(60*30)
        time.sleep(15)
                
        
            
        
        
main()





    
