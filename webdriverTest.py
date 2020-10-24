from selenium import webdriver
from dhooks import Webhook, File, Embed
import threading
import json
import time
from colored import fg, bg, attr
import os

webhookURL = 'WEBHOOK_URL'
url = 'https://www.sneakersnstuff.com/en/brands'

#Colors
info = bg('white') + fg('black')
error = bg('red') + fg('white')
warning = bg('yellow') + fg('white')
correct = bg('green') + fg('white')
reset = attr('reset')

#Variables
prevProducts = {}
products = {}
file = {}
brands = []
name1 = ''
name2 = ''
price = ''
sizes = ''
productImageURL = ''
logoImageURL = ''

#Turn on Selenium
DRIVER_PATH = 'C:/webdrivers/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func(url)
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def ScanBrands(url):
	#Getting on brand page by Selenium
	driver.get(url)

	#Checking every product
	#prevProducts = eval(open('txt/products.txt', 'r').read())
	#os.remove("txt/products.txt")

	brandList = driver.find_element_by_class_name('brand-list').find_elements_by_css_selector("*")
	print(len(brandList))
	for brand in range(1,len(brandList)): #Storing brands
		tempBrand = brandList[brand]
		if tempBrand.get_attribute("class") != '' or tempBrand.get_attribute("href") == None: #only get the li
			continue
		tempURL = tempBrand.get_attribute("href")
		brands.append(tempURL)
		pass
	#print(brands)
	for url in range(1,len(brands)): #Accessing the products
		ScanProducts(brands[url])
		pass
	results = open('txt/products.txt', 'a')
	results.write(str(products))

	#ScrapeSite()

def ScanProducts(brandURL):
	print(brandURL)
	driver.get(brandURL)
	
	try:
		driver.find_element_by_class_name('product-list')
	except:
		print('There is no products')
		return

	productList = driver.find_element_by_class_name('product-list').find_elements_by_class_name("card__name")
	for product in range(1,len(productList)):
		#print(productList[product].text)
		pass



def ScrapeSite(productURL):
	print(info + '\nSending the webhook!' + reset)

	#Getting selected product page by Selenium
	driver.get(productURL)

	#Waiting for website check
	try:
		driver.find_element_by_class_name('attack-box')
		print(yellow + 'The website is being checked...' + reset)
		time.sleep(10)
	except:
		print('This page is clean')

	#Scraping the page
	titleElem = driver.find_element_by_class_name('product-view__title').find_elements_by_css_selector("*")
	priceElem = driver.find_element_by_class_name('product-view__price').find_elements_by_css_selector("*")
	name1 = titleElem[0].text
	name2 = titleElem[1].text
	price = priceElem[0].text

	productImage = driver.find_element_by_class_name('image-gallery__link')
	productImageURL = productImage.get_attribute('href')

	logoImage = driver.find_element_by_class_name('site-logo--header').find_element_by_css_selector("*")
	logoImageURL = logoImage.get_attribute('src')

	#Scraping images
	driver.get(productImageURL)
	driver.save_screenshot("images/product.png")
	driver.get(logoImageURL)
	driver.save_screenshot("images/logo.png")

	#Creating Webhook
	webhook = Webhook(webhookURL)

	embed = Embed(
		title=name1 + ' ' + name2,
		url=productURL,
		color=65280,
		timestamp='now'
		)

	#Making a Discord Webhook
	embed.add_field(name='**Sizes**', value='[S](https://www.sneakersnstuff.com/en/product/40044/adidas-pleckgate-tp),'
											' [M](https://www.sneakersnstuff.com/en/product/40044/adidas-pleckgate-tp),'
											' [L](https://www.sneakersnstuff.com/en/product/40044/adidas-pleckgate-tp),'
											' [XL](https://www.sneakersnstuff.com/en/product/40044/adidas-pleckgate-tp)')
	embed.add_field(name='**Price**', value='$'+price)
	#embed.set_thumbnail("./product.png")
	#webhook.send(embed=embed)
	print(correct + 'webhook sent' + reset)
	

#Start the routine
set_interval(ScanBrands, 60)