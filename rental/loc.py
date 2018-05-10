import selenium,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import requests
import pandas as pd  
# chrome_options = Options()

html=requests.get('https://www.makaan.com/listings?postedBy=owner&listingType=rent&pageType=CITY_URLS&cityName=Chandigarh&cityId=24&templateId=MAKAAN_CITY_LISTING_RENT')
soup = BeautifulSoup(html.text, 'html.parser')
# print (soup)
final_property_links=[]
all_links=soup.find_all('div',{'class':'infoWrap'})
for link in all_links:
	a_tags=link.find('a')
	final_property_links.append((a_tags['href']))
	

# print (final_property_links)

driver = webdriver.Chrome('/home/ip-d/Documents/tinder/chromedriver')
driver.set_window_size(1700, 700)
session_id = driver.session_id
records = []
for counter,page in enumerate(final_property_links):
	try:
		driver.get(page)
		data={}
		if counter == 0:
			time.sleep(40)
		time.sleep(4)
		print session_id
		html=(driver.page_source)
		soup = BeautifulSoup(html, 'lxml')
	
 		table = soup.find('table')
		status = table.find("td", {"id": "Status"})
		data['status']=(status.text)
		security_deposit=table.find("td", {"id": "Security Deposit"})
		data['security']=(security_deposit.text)
		availability=table.find("td", {"id": "Availability"})
		data['avavi']=(availability.text)
		preferred=table.find("td", {"id": "Preferred Tenants"})
		data['pref']=(preferred.text)
		owner_name=driver.find_element_by_class_name('leagalname')
		owner_name=(owner_name.text)
		data['owner']=(owner_name)


		img_div=soup.find("div", {"data-bucket": "Title Image"})
		# print(img_div)
		# type(img_div.attrs)

		img_url=(img_div.attrs['data-sourcemodule'])
		data['img']=(img_url)
		location=driver.find_element_by_class_name('loc-name')
		location=(location.text)
		data['location']=(location)
		seller_type=driver.find_element_by_class_name('seller-type')
		seller_type=(seller_type.text)
		data['seller']=(seller_type)
		title=driver.find_element_by_class_name('type')
		title=(title.text)
		data['title']=(title)
		size=driver.find_element_by_class_name('size')
		size=(size.text)
		data['size']=(size)
		value=driver.find_element_by_class_name('val')
		value=(value.text)
		data['value']=(value)
		phone_view=driver.find_element_by_class_name('txtlink')
		actions = ActionChains(driver)
		actions.move_to_element(phone_view).perform()
		time.sleep(3)
		phone_view.click()
		time.sleep(2)
		phone = driver.find_element_by_class_name('see-phoneno')
		phone=(phone.text)
		data['phone']=(phone)
		records.append(data)
		# df = pd.DataFrame(records, columns=['phone', 'owner_name', 'location', 'img_url']) 
		print('\n')
		# breakowner_name
	except Exception as r:
		print (r)
		pass

print(records)
# for phone in all_phone:
# print (dir(all_phone[0]))

# link.click()
# print (all_phone)

# passw.send_keys(password)
# driver.find_element_by_id("loginbutton").click()
# driver.switch_to_window(driver.window_handles[0])

# # time.sleep(5driver.switch_to_window(driver.window_handles[0])
# modal=driver.find_element_by_id("modal-manager")
# element2=modal.find_element_by_xpath(".//button[@aria-label='Login with Facebook']")
# element2.click()

# # print (dir(driver))
# time.sleep(8)
# elem = driver.find_elements_by_class_name('button__text')
# # for i,ead in enumerate(elem):
# #     print(i)
# #     print(ead.text)
# elem[5].click()
# time.sleep(1)
# elem = driver.find_elements_by_class_name('button__text')
# elem[5].click()
# time.sleep(1)
# elem = driver.find_elements_by_class_name('button__text')
# elem[5].click()
# time.sleep(1)
# elem = driver.find_elements_by_class_name('button__text')
# elem[5].click()
# time.sleep(1)
# # driver.send_keys("", Keys.ARROW_RIGHT)
# elem = driver.find_elements_by_class_name('button__text')
# # for i,ead in enumerate(elem):
# #     print(i)
# #     print(ead.find_elements_by_tag_name('svg'))
# #     print(ead.text)
# # elem[4].click()
# for i in range(0,1000):
#     time.sleep(2)
#     elem[3].click()
# # tagNames = driver.find_elements_by_tag_name('button')
# # for i,ead in enumerate(tagNames):
#     # print(i)
# # ead[5].click()
# # time.sleep(2)
#     # print(ead.text)
# # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# # # print(tagNames)
# # for i in tagNames:
# #     print(i.get_attribute('aria-label'))
# # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# # su=driver.find_element_by_class_name('onboarding__buttons')
# #
# # print 'ss',su
# # try:
# #     elem=su.find_element_by_xpath(".//button[@aria-label='Great!']")
# #     elem.click()
# # except:
# #     print 'in except'
# #     elem=su.find_element_by_xpath(".//button[@aria-label='Next']")
# #     elem.click()
# # print (len(driver.window_handles))
# # print (dir(driver.window_handles))
# #
# # window_before = driver.window_handles[0]
# # window_after = driver.window_handles[2]
# # driver.switch_to_window(window_after)
# # time.sleep(2)
# # email = driver.find_element_by_id("email")
# # passw = driver.find_element_by_id("pass")
# #
# # email.send_keys('9780329759')
# # passw.send_keys("32@#hs5991inAT")
# #
# # loginin = driver.find_element_by_name('login')
# # loginin.click()


# # driver.quit()
