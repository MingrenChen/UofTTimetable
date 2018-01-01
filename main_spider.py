# -*-coding:UTF-8 -*-
import requests
import sys


def getWebPage(url, num):
    try:
        urlpage = requests.get(url)
    except IOError:
        print("IOError")
    '''
    urlpage.text中包含网页的源码内容
    '''
    WebPageDownload(urlpage.text,num)

def  WebPageDownload(text,num):
    '''
    将下载的网页保存到file.txt文件中
    '''
    ff = open("year_{}.txt".format(num),'w')
    ff.writelines(text)
    ff.close()


website = ["https://timetable.iit.artsci.utoronto.ca/api/20179/courses?org"+
                        "=&code=&section=&studyyear=1&daytime=&weekday=&prof=&breadth=&"+
                        "online=&waitlist=&available=&title=",
            "https://timetable.iit.artsci.utoronto.ca/api/20179/courses?org"+
                        "=&code=&section=&studyyear=2&daytime=&weekday=&prof=&breadth=&"+
                        "online=&waitlist=&available=&title=",
            "https://timetable.iit.artsci.utoronto.ca/api/20179/courses?org"+
                        "=&code=&section=&studyyear=3&daytime=&weekday=&prof=&breadth=&"+
                        "online=&waitlist=&available=&title=",
            "https://timetable.iit.artsci.utoronto.ca/api/20179/courses?org"+
                        "=&code=&section=&studyyear=4&daytime=&weekday=&prof=&breadth=&"+
                        "online=&waitlist=&available=&title="]

# for i in range(len(website)):
#     getWebPage(website[i], i)
#     print("succeed")
getWebPage("https://timetable.iit.artsci.utoronto.ca/api/20179/courses?org"+
                        "=&code=&section=&studyyear=2&daytime=&weekday=&prof=&breadth=&"+
                        "online=&waitlist=&available=&title=", 1)
