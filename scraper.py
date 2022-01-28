import requests
import sys
from bs4 import BeautifulSoup
import smtplib

def scrape():
    global URL
    global URL_input
    global price
    global title
    global headline
    global product_price_1
    global product_price_2
    global number_of_reviews
    global price_save
    URL_input = input("Enter your URL")
    URL = URL_input
    headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    headline = soup.find(id='productTitle')
    if headline is not None:
        title = headline.get_text
    try:
        price = soup.find(id='priceblock_ourprice')
        print(f"The name of the product you wish to buy is {headline.strip()}")
        product_price_1 = print(f"The price of your item is {price.get_text()}")
        number_of_reviews = soup.find(id='acrCustomerReviewText').get_text()
        print(f"The number of ratings are {number_of_reviews.strip()}")
        price_save = soup.find(id='regularprice_savings')
        print(f"The amount {price_save.get_text()}")
    except AttributeError:
        deal = soup.find(id='priceblock_dealprice')
        print(f"The name of the product you wish to buy is {headline.get_text()}")
        product_price_2 = print(f"The price of your item is {deal.strip()}.")
        number_of_reviews = soup.find(id='acrCustomerReviewText').get_text()
        print(f"The number of ratings are {number_of_reviews.strip()}")
        price_save = soup.find(id='regularprice_savings').strip()
        print(f"The amount {price_save.get_text()}")
scrape()

def use_again():
    again = input('Do you want to use the scraper again? (y/n)').lower()
    if again == 'y':
        scrape()
        use_again()
    elif again == 'n':
        print("Thanks for using the scraper! Do visit again!")
        sys.exit()
    else:
        print("Please enter a valid response")
        use_again()
use_again()