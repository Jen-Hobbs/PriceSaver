from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from selenium import webdriver
import logging
import requests


logger = logging.getLogger(__name__)

def index(request):
    url = "https://www.thriftyfoods.com/product/ricelong-grain/00000_000000005910000802"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0")
    profile.set_preference("javascript.enabled", True)
    profile.set_preference("cookies.enabled", True)
    browser = webdriver.Firefox(profile)
    browser.get(url)
    
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')
    logger = logging.getLogger("mylogger")
    logger.info(soup.prettify())
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }