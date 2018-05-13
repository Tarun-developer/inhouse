from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
import requests
import json
from .models import *
from datetime import datetime,timedelta
from django.db.models import Q
from django.utils.decorators import method_decorator
import csv
import base64
from passlib.hash import django_pbkdf2_sha256 as handler
from random import randint
from django.conf import settings
import pytz
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponseRedirect, render_to_response
from django.contrib import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import requests,time
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
utc=pytz.UTC
from search.models import *

					# ADMIN



class Makkan(TemplateView):
	template_name = "dashboard.html"

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(Makkan, self).dispatch(request, *args, **kwargs)



	def get_context_data(self, *args, **kwargs):
		context = super(Makkan, self).get_context_data()
		
		
		return context
	def post(self,request):
		html=requests.get('https://www.makaan.com/listings?postedBy=owner&listingType=rent&pageType=CITY_URLS&cityName=Chandigarh&cityId=24&templateId=MAKAAN_CITY_LISTING_RENT')
		soup = BeautifulSoup(html.text, 'html.parser')
		# print (soup)
		final_property_links=[]
		all_links=soup.find_all('div',{'class':'infoWrap'})
		for link in all_links:
			a_tags=link.find('a')
			final_property_links.append((a_tags['href']))

		print ('\n\n **************************************888')
		
		driver = webdriver.Chrome(settings.CHROMEDRIVER_PATH)
		driver.set_window_size(1700, 700)
		records = []

		all_properties=[]
		for counter,page in enumerate(final_property_links):
			try:
				if counter == 10:
					break
				print (' WROTE '+str(counter)+' out of '+str(len(final_property_links)))
				json={}
				driver.get(page)
				data={}
				if counter == 0:
					time.sleep(60)
				else:
					time.sleep(9)
					elemt=driver.find_element_by_class_name('txtlink')
					driver.execute_script("arguments[0].scrollIntoView();", elemt)
					time.sleep(3)
					elemt.click()
					time.sleep(3)
					print ('999')
					phone=driver.find_element_by_class_name('see-phoneno')
					title=driver.find_element_by_xpath("//div[@class='type-col']//span[@class='type']")
					location1=driver.find_element_by_class_name('loc-name')
					location2=driver.find_element_by_class_name('city-name')
					location=(location1.text)+' '+str(location2.text)
					price=driver.find_element_by_xpath("//div[@class='price-wrap']//span")
					bhk=driver.find_element_by_xpath("//div[@class='type-col']//span[@itemprop='name']")
					bhk=bhk.text
					bhk=bhk.split('BHK')
					bhk=bhk[0]
					

					table=driver.find_element_by_xpath("//table[@class='sub-points']//td[@id='Status']")
					if table.text =='Furnished':
						status=1
					if table.text =='Semi-Furnished':
						status=2
					
					image_list=[]
					all_images=driver.find_elements_by_class_name("imgzoom")
					for image in all_images:
						src=image.find_element_by_tag_name('img').get_attribute("data-src")
						image_list.append(str(src))
					
					json['phone'],json['title'],json['location'],json['price'],json['status'],json['bhk'],json['image_list']=str(phone.text),str(title.text),str(location),str(price.text),status,bhk,image_list
					all_properties.append(json)
					print (all_properties)
					
					print('\n')
					# breakowner_name
			except Exception as r:
				print (r)
				pass
		
		print ('\n\n\n')
		print ('writing to db')
		for i,lis in enumerate(all_properties):
			try:

				older_property=Property.objects.filter(name=lis['title'],budget=str(lis['price']),location=lis['location'])
				print ('ssssssssss')
				if not older_property:
					myString = ",".join(lis['image_list'] )
					image_obj=Images.objects.create(name=myString)

					if lis['status']==1:
						furn_obj=Furnish.objects.create(fully=1)
					if lis['status']==2:
						furn_obj=Furnish.objects.create(partially=1)

					bhk_obj=BHK.objects.create(name=lis['bhk'])
					new_property=Property.objects.create(name=lis['title'],location=lis['location'],status=1,budget=str(lis['price']),furnish=furn_obj,bhk=bhk_obj,image=image_obj)
					

				image_obj=''
				myString=''
			except Exception as rr:
				print (rr)

		return  HttpResponse('1')






class Housing(TemplateView):
	template_name = "dashboard.html"

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(Housing, self).dispatch(request, *args, **kwargs)



	def get_context_data(self, *args, **kwargs):
		context = super(Makkan, self).get_context_data()
		
		
		return context
	def post(self,request):
		url=('https://housing.com/rent/search-P679xe73u28050522V16ob6?locality_info=false')
		driver = webdriver.Chrome(settings.CHROMEDRIVER_PATH)
		driver.set_window_size(1700, 700)
		driver.get(url)
		time.sleep(3)
		loginbutton=driver.find_element_by_id('loginModalBtn')
		loginbutton.click()

		time.sleep(3)
		records = []

		# all_properties=[]
		# for counter,page in enumerate(final_property_links):
		# 	try:
		# 		if counter == 10:
		# 			break
		# 		print (' WROTE '+str(counter)+' out of '+str(len(final_property_links)))
		# 		json={}
		# 		driver.get(page)
		# 		data={}
		# 		if counter == 0:
		# 			time.sleep(60)
		# 		else:
		# 			time.sleep(9)
		# 			elemt=driver.find_element_by_class_name('txtlink')
		# 			driver.execute_script("arguments[0].scrollIntoView();", elemt)
		# 			time.sleep(3)
		# 			elemt.click()
		# 			time.sleep(3)
		# 			print ('999')
		# 			phone=driver.find_element_by_class_name('see-phoneno')
		# 			title=driver.find_element_by_xpath("//div[@class='type-col']//span[@class='type']")
		# 			location1=driver.find_element_by_class_name('loc-name')
		# 			location2=driver.find_element_by_class_name('city-name')
		# 			location=(location1.text)+' '+str(location2.text)
		# 			price=driver.find_element_by_xpath("//div[@class='price-wrap']//span")
		# 			bhk=driver.find_element_by_xpath("//div[@class='type-col']//span[@itemprop='name']")
		# 			bhk=bhk.text
		# 			bhk=bhk.split('BHK')
		# 			bhk=bhk[0]
					

		# 			table=driver.find_element_by_xpath("//table[@class='sub-points']//td[@id='Status']")
		# 			if table.text =='Furnished':
		# 				status=1
		# 			if table.text =='Semi-Furnished':
		# 				status=2
					
		# 			image_list=[]
		# 			all_images=driver.find_elements_by_class_name("imgzoom")
		# 			for image in all_images:
		# 				src=image.find_element_by_tag_name('img').get_attribute("data-src")
		# 				image_list.append(str(src))
					
		# 			json['phone'],json['title'],json['location'],json['price'],json['status'],json['bhk'],json['image_list']=str(phone.text),str(title.text),str(location),str(price.text),status,bhk,image_list
		# 			all_properties.append(json)
		# 			print (all_properties)
					
		# 			print('\n')
		# 			# breakowner_name
		# 	except Exception as r:
		# 		print (r)
		# 		pass
		
		# print ('\n\n\n')
		# print ('writing to db')
		# for i,lis in enumerate(all_properties):
		# 	try:

		# 		older_property=Property.objects.filter(name=lis['title'],budget=str(lis['price']),location=lis['location'])
		# 		print ('ssssssssss')
		# 		if not older_property:
		# 			myString = ",".join(lis['image_list'] )
		# 			image_obj=Images.objects.create(name=myString)

		# 			if lis['status']==1:
		# 				furn_obj=Furnish.objects.create(fully=1)
		# 			if lis['status']==2:
		# 				furn_obj=Furnish.objects.create(partially=1)

		# 			bhk_obj=BHK.objects.create(name=lis['bhk'])
		# 			new_property=Property.objects.create(name=lis['title'],location=lis['location'],status=1,budget=str(lis['price']),furnish=furn_obj,bhk=bhk_obj,image=image_obj)
					

		# 		image_obj=''
		# 		myString=''
		# 	except Exception as rr:
		# 		print (rr)

		# return  HttpResponse('1')
