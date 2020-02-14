from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv,re
import time

def yt_main():
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(executable_path='youtube/geckodriver', options=options)
    base = csv.reader(open('youtube/yt.csv'))
    error = []
    # user_url = ['https://www.youtube.com/user/motomobitv','https://www.youtube.com/user/ridwanhr']
    user_url = []

    with open('youtube/yt_channel_id.csv', 'w') as f:
        w = csv.writer(f)
        for a in base:
            try:
                print(a[0])
                driver.get('https://www.youtube.com/results?search_query={}'.format(str(a[0]).replace(' ', '+')))
                id = driver.find_element_by_xpath('//*[@id="main-link"]').get_attribute('href')
                if 'channel' in id:
                    pattern = re.compile('[^\/]+$')
                    get_id = re.findall(pattern, id)
                    w.writerow([get_id])
                if 'user' in id:
                    user_url.append(id)
                print(id)
            except Exception:
                error.append(a[0])
        print(error)

        for b in user_url:
            driver.get('https://commentpicker.com/youtube-channel-id.php')
            driver.find_element_by_xpath('//*[@id="input-youtube-url-js"]').send_keys(b)
            driver.find_element_by_css_selector('#get-channel-id').click()
            time.sleep(3)
            get = driver.find_element_by_xpath('/html/body/main/div[3]/div[1]/p[1]').text
            channel_id = re.sub('^[^:]+\:\s', '', get)
            w.writerow([channel_id])
            print(b)

            # driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/button').submit()

    # cek = 'https://www.youtube.com/channel/UCT-K6e-taJBl8FkCEaKf1Ew'
    # if 'channel' in cek:
    #     pattern = re.compile('[^\/]+$')
    #     get_id = re.findall(pattern,cek)
    #     print get_id
    #     print 'succes'