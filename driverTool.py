import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

def searchTweets(username, password, searchterm):

    driver = Chrome(ChromeDriverManager().install())
    driver.get('https://twitter.com/login')

    wait = True #Prevents code from executing prior to page load

    while wait is True: #Logs into twitter
        try:
            user = driver.find_element_by_xpath("//input[@name='session[username_or_email]']")
            user.send_keys(username)

            passw = driver.find_element_by_xpath("//input[@name='session[password]']")
            passw.send_keys(password)
            passw.send_keys(Keys.RETURN)

            wait = False
        except:
            pass

    wait = True

    while wait is True: #Uses the twitter search query
        try:
            search_input = driver.find_element_by_xpath("//input[@aria-label='Search query']")
            search_input.send_keys(searchterm)
            search_input.send_keys(Keys.RETURN)
            wait = False
        except:
            pass

    wait = True

    while wait is True:
        try:
            people = driver.find_element_by_link_text('People')
            people.click()
            time.sleep(3)
            wait = False
        except:
            pass

    wait = True

    while wait is True:
        try:
            driver.find_element_by_xpath("//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']").click()
            wait = False
        except:
            pass

    wait = True

    while wait is True:
        try:
           tweet = driver.find_element_by_xpath("//div[@class='css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']")
           print(tweet.text)
           wait = False
        except:
            pass



    wait = True
    while wait is True:
        ctr = 0
        ctr += 1

