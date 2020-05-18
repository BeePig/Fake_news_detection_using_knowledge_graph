from selenium import webdriver
import os
import time

def count_luanvan(luanvan_results):
    results = luanvan_results.find_elements_by_tag_name("div")

    return len(results)

DIR_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) + "/"
pattern_url = "https://www.dailymail.co.uk/news/donald_trump/index.html"

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(DIR_PATH + "chromedriver/chromedriver", chrome_options=options)

driver.get(pattern_url)

contain = driver.find_element_by_xpath(
                                '//*[@class="football-team-news"]')
#
number = int(count_luanvan(contain)/3)

i = 1

while i < number:
    try:
        time_data = driver.find_element_by_xpath(
                                    '//*[@class="football-team-news"]/div[' + str(i) + ']/div/div/span').text
    except:
        time_data = driver.find_element_by_xpath(
            '//*[@class="football-team-news"]/div[' + str(i) + ']/div/span').text

    time_data = time_data.replace('/', '_').replace(':', '_')

    article = driver.find_element_by_xpath(
                                    '//*[@class="football-team-news"]/div[' + str(i) + ']/h2/a[1]')

    driver.execute_script("arguments[0].click();", article)

    title = driver.find_element_by_xpath(
                                    '//*[@id="js-article-text"]/h2[1]').text

    content = driver.find_element_by_xpath(
                                    '//*[@id="js-article-text"]/div[2]').text

    text = title + "\n"
    for item in content.split('\n'):
        if len(item.split(' ')) < 5:
            continue

        if item[len(item)-3: ] == "...":
            continue

        text += item + "\n"

    i += 1

    with open(DIR_PATH +  'dailymail/dailymail_' + time_data, 'w') as f:
        f.write(text)

    driver.execute_script("window.history.go(-1)")
    time.sleep(3)