import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

def searchTweets(username, password, searchterm):

    driver = Chrome(ChromeDriverManager().install())
    driver.get('https://twitter.com/login')

    time.sleep(1)

    user = driver.find_element_by_xpath("//input[@name='session[username_or_email]']")
    user.send_keys(username)

    passw = driver.find_element_by_xpath("//input[@name='session[password]']")
    passw.send_keys(password)
    passw.send_keys(Keys.RETURN)

    time.sleep(1)

    search_input = driver.find_element_by_xpath("//input[@aria-label='Search query']")
    search_input.send_keys(searchterm)
    search_input.send_keys(Keys.RETURN)

    time.sleep(1)

    people = driver.find_element_by_link_text('People')
    people.click()

    time.sleep(1)

    driver.find_element_by_xpath("//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']").click()

    time.sleep(1)


    tweet = driver.find_element_by_xpath("//div[@class='css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']")

    return tweet.text


