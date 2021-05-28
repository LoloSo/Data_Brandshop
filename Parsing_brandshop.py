import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json


def get_data(url):
    options = webdriver.ChromeOptions()

    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

    options.add_argument('--disable-blink-features=AutomationControlled')

    # options.add_argument('--headless')

    try:
        driver = webdriver.Chrome(
            executable_path=r'C:\Users\artem\Documents\PythonProjects\pythonProject2\BeatifulSoup\Parsing_brandshop_1\chromedriver.exe',
            options=options
        )

        driver.get(url=url)
        driver.implicitly_wait(5)

        items = driver.find_elements_by_class_name('product-container col col-4 col-sm-6')
        item_href = driver.find_elements_by_class_name('product_image').get('href')
        
        for i in range(len(items)):
            if item_href != 'javascript:void(0)':
                items[i].click()


    #    with open('brandshop.html', 'w', encoding='utf-8') as file:
    #        file.write(driver.page_source)
#
    #    driver.implicitly_wait(5)
#
    #    with open('brandshop.html', encoding='utf-8') as file:
    #        src = file.read()
#
    #    soup = BeautifulSoup(src, 'lxml')
#
    #    items_profile = soup.find_all(class_='product-container col col-4 col-sm-6')
    #    for href in items_profile:
    #        item_text = href.text
    #        item_href = href.find(class_='product-image').get('href')
    #        #if item_href != 'javascript:void(0)':
    #            #item_article = item_href.split('/')[-2]
    #        #else:
    #            #item_article = None
    #        print(f'{item_text}: {item_href}')
    #        #print(f'Артикул: {item_article}')
#
#
    except Exception as ex:
       print(ex)
    finally:
       driver.close()
       driver.quit()


def main():
    # for i in range(1, 112):
    # get_data(f'https://brandshop.ru/goods/?page={i}', i)
    get_data('https://brandshop.ru/goods/?page=1')


if __name__ == '__main__':
    main()
