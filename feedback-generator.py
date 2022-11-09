from bs4 import BeautifulSoup
from selenium import webdriver

def generator(product_input):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('chromedriver', options=chrome_options)
    driver.get('https://testimonial-generator.com/index.php')

    product = '//*[@id="content"]/form/div/p[1]/input'
    generate = '//*[@id="content"]/form/div/p[2]/input'
    result = '//*[@id="content"]/p[3]'
    
    driver.find_element("xpath", product).send_keys(product_input)
    driver.find_element("xpath", generate).click()
    
    output = driver.find_element("xpath", result).text.split("\n")[0][1:-1]
    driver.quit()
    return output
