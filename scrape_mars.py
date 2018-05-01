#Dependencies

import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo


def init_browser():
    executable_path = {"./chromedriver"}
    return Browser("chrome", headless=False)

def scrape():


# Mars News

    def init_browser():
        # @NOTE: Replace the path with your actual path to the chromedriver
        executable_path = {"./chromedriver"}
        return Browser("chrome", headless=False)

    def scrape():
        browser = init_browser()
        url_news = "https://mars.nasa.gov/news/"
        browser.visit(url_news)
        #time.sleep(1)
        nasa_mars_scrape = {}
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        nasa_mars_scrape["headline"] = soup.find("div", class_ = "content_title").next_element.get_text()
        nasa_mars_scrape["body"] = soup.find("div", class_ = "article_teaser_body").get_text()
        return nasa_mars_scrape


    #Mars Image

    browser = Browser('chrome', headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/'
    browser.visit(url)

    def scrape_mars_image():
        browser = init_browser()
        url = "http://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
        image = soup.find("a", class_ = "button fancybox")
        featured_mars_image_url = "https://www.jpl.nasa.gov" + image["data-fancybox-href"]
        return featured_mars_image_url

    featured_mars_image_url = scrape_mars_image()

    #Mars Weather

    def scrape_mars_weather():
        browser = init_browser()
        url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(url)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
        mars_weather = soup.find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
        return mars_weather

    mars_weather = scrape_mars_weather()


    # pandas scrape of mars facts

    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url)
    tables

    mars_df = tables[0]
    mars_df.columns = ['Category', 'Fact']


    #Mars Hemispheres

    def scrape_mars_hem1():
        browser = init_browser()
        url1 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
        browser.visit(url1)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
    #     hem1 = soup.find("h2", class_ = "title")
        mars_hem1 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"
        return featured_mars_image_url


    def scrape_hem1():
        browser = init_browser()
        url1 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
        browser.visit(url1)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
        hem1 = {}
        hem1["body"] = soup.find("h2", class_ = "title").get_text()


    mars_hem1 = scrape_mars_hem1()
    hem1 = scrape_hem1()


    def scrape_mars_hem2():
        browser = init_browser()
        url2 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
        browser.visit(url2)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
    #     hem2 = soup.find("h2", class_ = "title")
        mars_hem2 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"
        return featured_mars_image_url


    def scrape_hem2():
        browser = init_browser()
        url2 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
        browser.visit(url2)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
        hem2 = {}
        hem2["body"] = soup.find("h2", class_ = "title").get_text()


    mars_hem2 = scrape_mars_hem2()
    hem2 = scrape_hem2()

    def scrape_mars_hem3():
        browser = init_browser()
        url3 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
        browser.visit(url3)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
    #     hem3 = soup.find("h2", class_ = "title")
        mars_hem3 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"
        return featured_mars_image_url


    def scrape_hem3():
        browser = init_browser()
        url3 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
        browser.visit(url3)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
        hem3 = {}
        hem3["body"] = soup.find("h2", class_ = "title").get_text()


    mars_hem3 = scrape_mars_hem3()
    hem3 = scrape_hem3()

    def scrape_mars_hem4():
        browser = init_browser()
        url4 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
        browser.visit(url4)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
    #     hem4 = soup.find("h2", class_ = "title")
        mars_hem4 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"
        return featured_mars_image_url


    def scrape_hem4():
        browser = init_browser()
        url4 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
        browser.visit(url4)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, "lxml")
        hem4 = {}
        hem4["body"] = soup.find("h2.title").get_text()


    mars_hem4 = scrape_mars_hem4()
    hem4 = scrape_hem4()


    #Dictionary of all data

    #set blank dictoinary
    Scraper_Dictionary = {}

    Scraper_Dictionary["news"] = nasa_mars_scrape
    Scraper_Dictionary["feat_img"] = featured_mars_image_url
    Scraper_Dictionary["weather"] = mars_weather
    Scraper_Dictionary["facts"] = mars_df
    Scraper_Dictionary["hemisphere 1"] = hem1
    Scraper_Dictionary["hemisphere 2"] = hem2
    Scraper_Dictionary["hemisphere 3"] = hem3
    Scraper_Dictionary["hemisphere 4"] = hem4

    return Scraper_Dictionary


