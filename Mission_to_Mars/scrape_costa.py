from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
   
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")
 
    titles = soup.find_all("div", class_="content_title")
    news_title = titles[1].text.replace('\n', '')
    news_title

    paragraphs = soup.find_all(class_="article_teaser_body")
    news_p = paragraphs[0].text.replace('\n', '')
    news_p

    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    featured_image_url = soup.find(class_="headerimage fade-in").get("src")

    featured_image_url
    fullurl = url + "/" + featured_image_url

    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    tables

    df = tables[0]

    html_table = df.to_html()
    html_table

    html_table.replace('\n', '')
    
    df.to_html('table.html')

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    print(len(browser.find_by_css("a.product-item h3")))
    hemisphere_image_urls = []

    for i in range (4):
        current = {}
        browser.find_by_css("a.product-item h3")[i].click()
        elements = browser.find_by_text('Sample').first
        current["image_url"] = elements['href']
        title = browser.find_by_css('h2.title').text
        current ["title"] = title
        hemisphere_image_urls.append(current)
        browser.back()

    print(hemisphere_image_urls)

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
