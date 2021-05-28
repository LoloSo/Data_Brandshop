import time
from selenium import webdriver
from bs4 import BeautifulSoup
import json


def get_data(url):
    options = webdriver.ChromeOptions()

    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

    options.add_argument('--disable-blink-features=AutomationControlled')

    try:

        driver = webdriver.Chrome(
            executable_path=r'C:\Users\artem\Documents\PythonProjects\pythonProject2\BeatifulSoup\Parsing_brandshop_1\chromedriver.exe',
            options=options
        )

        driver.get(url=url)
        driver.implicitly_wait(5)

        with open('brand.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

        driver.implicitly_wait(2)

        with open('brand.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        items_status = soup.find_all(class_='product-container col col-4 col-sm-6')
        items = driver.find_elements_by_class_name('product')

        for k in range(len(items_status)):

            status = items_status[k].find(class_='product-image').get('href')

            if status != 'javascript:void(0);':

                driver.get(url=status)
                driver.switch_to.window(driver.window_handles[0])

                with open('item_info.html', 'w', encoding='utf-8') as file:
                    file.write(driver.page_source)

                with open('item_info.html', encoding='utf-8') as file:
                    src = file.read()

                soup = BeautifulSoup(src, 'lxml')

                item_brand_name = soup.find('div', class_='product-title').find('h1').find_all('span')
                item_brand = item_brand_name[0].text
                item_name = item_brand_name[1].text
                item_price = soup.find('span', class_='regprice').text.strip()
                item_description = soup.find('div', class_='box').find('p').text.strip().split()
                item_article = item_description[1].strip()
                item_sizes = soup.find('div', class_='product-size').find_all('div')
                item_sizes_list = []

                for size in item_sizes:
                    item_size = size.text
                    item_sizes_list.append(item_size)

                item_image = soup.find('div', class_='col col-10 col-sm-12 product-image-big').find('img').get('src')

                """print(item_brand)
                print(item_name)
                print(item_price)
                print(item_article)
                print(*item_sizes_list)
                print(item_image)"""

                items_data = []

                item_full_info = {
                    'Brand': item_brand,
                    'Name': item_name,
                    'Price': item_price,
                    "Article": item_article,
                    'Sizes': item_sizes_list,
                    'Photo': item_image
                }

                items_data.append(item_full_info)

                driver.implicitly_wait(2)

                with open('item_data.json', 'a', encoding='utf-8') as file:
                    json.dump(items_data, file, indent=4, ensure_ascii=False, sort_keys=True)

                time.sleep(1)
                driver.implicitly_wait(2)
                driver.back()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

            else:
                continue

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


# def get_true():
def main():
    get_data('https://brandshop.ru/goods/?page=1')


if __name__ == '__main__':
    main()
