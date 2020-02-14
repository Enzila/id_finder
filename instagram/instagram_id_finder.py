# enzila
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv, re
import time

def ig_main():
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(executable_path='instagram/geckodriver', options=options)

    base = open('instagram/ig.csv')
    a = csv.reader(base)

    driver.get('https://codeofaninja.com/tools/find-instagram-user-id')
    with open('instagram/ig_id.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(['user_id', 'username'])
        for row in a:
            ig2 = []
            username = driver.find_element_by_css_selector('#user_input')
            username.send_keys(row)
            submit = driver.find_element_by_css_selector('.btn')
            submit.submit()
            time.sleep(10)
            try:
                stat1 = driver.find_element_by_css_selector(
                    '#answer > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
                stat2 = driver.find_element_by_css_selector(
                    '#answer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)')
                result = stat1.text
                result2 = stat2.text
            except:
                print(row)
                result = 'Username Tidak Ditemukan'
                result2 = 'username tidak ditemukan'
            print(result)
            print(result2)
            w.writerow([row, result, result2])
            username.clear()
if __name__ == '__main__':
    ig_main()