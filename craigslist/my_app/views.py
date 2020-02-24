from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
from requests.compat import quote_plus
from . import models
from bs4.element import Tag
from selenium import webdriver

BASE_CRAIGSLIST_URL = "https://montreal.craigslist.org/search/sss?query={}&sort=rel&lang=en&cc=us"
BASE_IMAGE_URL = "https://images.craigslist.org/{}_300x300.jpg"
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search_phrase = request.POST.get('search')
    if search_phrase is None:
        search_phrase = "coffee table"
    models.Search.objects.create(search_content=search_phrase)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search_phrase))
    # driver1 = webdriver.Chrome("D:\Internet_Softwares\Browser\chromedriver_win32\chromedriver.exe")
    # driver1.get(final_url)
    # content = driver1.page_source
    response = requests.get(final_url)
    data = response.text
    # Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(data, features='html.parser')
    # Extracting all the <a> tags whose class name is 'result-title' into a list
    post_listings = soup.findAll('li', {'class': 'result-row'})
    final_postings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'
        if post.find(class_='result-image').get('data-ids'):
            post_image = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_src = BASE_IMAGE_URL.format(post_image)
        else:
            post_image_src = "https://sciences.ucf.edu/psychology/wp-content/uploads/sites/63/2019/09/No-Image-Available.png"


        final_postings.append((post_title, post_url, post_price, post_image_src))


    stuff_for_frontend = {
        'search_phrase': search_phrase,
        'final_postings': final_postings,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
