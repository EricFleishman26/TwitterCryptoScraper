import csv
from time import sleep
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

    while wait is True: #PROBLEMATIC FUNCTION - Needs to scrape data from tweets

            cards = driver.find_element_by_xpath("//div[@data-testid='tweet']")
            card = cards[0]
            print(card.find_element_by_xpath(".//span[contains(text(),'@')]"))
            wait = False


##Issues with scraping the text.
#So far it is able to log into twitter and search but the scraping of the tweet information
#must be implemented.
