# -*- coding: utf-8 -*-

# This is a spider crawl the University of Toronto calendar in order
# to help me find course I would like to enrol in.

import scrapy
import os
import sys
import re
import urllib.parse
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))



class CourseSpider(scrapy.Spider):
    name = 'course'
    allowed_domains = ['fas.calendar.utoronto.ca']
    start_urls = ['https://fas.calendar.utoronto.ca/search-courses?page=0']

    def parse(self, response):
        current_page = response.xpath("//*[@id=\"block-system-main\"]/div/div/div[2]/table/tbody/tr")
        # the for loop
        for course in current_page:
            course_url = urllib.parse.urljoin("https://fas.calendar.utoronto.ca",course.xpath("td/a/@href").extract()[0])
            yield scrapy.Request(course_url, callback=self.parse_course)

        next_page = response.xpath("//*[@id=\"block-system-main\"]/div/div/div[3]/ul/li[3]/a/@href")
        # next_page will be [] when crawling the last page.
        if next_page:
            next_page_url = urllib.parse.urljoin("https://fas.calendar.utoronto.ca/", next_page.extract()[0])
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_course(self, response):
        coursecode = response.xpath("//*[@id=\"page-title\"]/text()").extract()[0]
        lectut = response.xpath("//*[@class=\"node node-course node-full clearfix\"]/div/div[1]/div[2]/div/text()").extract()[0]
        code = re.search("[A-Z]{3}\d{3}", coursecode).group(0)
        name = re.search("[A-Z][a-z][A-Za-z &]+", coursecode).group(0)
        # item['lec'] = lectut.
        # if lectut = "TBA":
        #     item['lec'] = "TBA"
        print(code,": ", name)
