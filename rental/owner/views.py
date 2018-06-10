# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from search.models import OwnerInfo
from search.models import Property
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
import json,pprint
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
class OwnerDashboard(TemplateView):
    template_name = "owner_dashboard.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerDashboard, self).get_context_data()
        return context

class OwnerProfile(TemplateView):
    template_name = "owner_profile.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerProfile, self).get_context_data()
        return context

class OwnerProperty(TemplateView):
    template_name = "owner_property.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerProperty, self).get_context_data()
        return context

class OwnerRegister(TemplateView):
    template_name = "owner_register.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerRegister, self).get_context_data()
        return context
    def post(self, request):
        islogin = request.POST.get('islogin')
        password = request.POST.get('password')
        mobile = request.POST.get('moblie')
        email = request.POST.get('email')

        if islogin:

            try:
                owner_obj = OwnerInfo.objects.get(owner_mobile=mobile)                
                bool_pass=check_password(password,owner_obj.owner_password)
                
                if bool_pass:
                    # login successfully, to do create session
                    return HttpResponseRedirect("/owner/")
                else:
                    messages.info(request,'invalid password. please try again')
                    return HttpResponseRedirect("/owner/owner_register")
            except Exception as r:
                print r
                messages.info(request,'invalid password. please try again')
                return HttpResponseRedirect("/owner/owner_register")
        else:
            try:
                owner_obj = OwnerInfo.objects.get(owner_mobile=mobile)
                if owner_obj:
                    messages.info(request,'please login at your right')
                    return HttpResponseRedirect("/owner/owner_register")
            
            except Exception as r:

                hashed_pwd = make_password(password)
                owner_register = OwnerInfo(email=email, owner_mobile=mobile,owner_password=hashed_pwd)
                owner_register.save()
                print owner_register.id
                return HttpResponseRedirect("/owner/owner_add_property/?own=" + str(owner_register.id))
                print (r)



class OwnerAddProperty(TemplateView):
    template_name = "owner_add_property.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerAddProperty, self).get_context_data()
        return context
    def post(self, request):
        try:
            property_type = request.POST.get('property_type')
            property_status = request.POST.get('property_status')
            loaction = request.POST.get('loaction')
            price = request.POST.get('price')
            city = request.POST.get('city')
            family = request.POST.get('family')
            bachelor = request.POST.get('bachelor')
            girls = request.POST.get('girls')
            if property_status=='Furnished':
                furn_obj=Furnish.objects.create(fully=1)
            if property_status=='Semi Furnished':
                furn_obj=Furnish.objects.create(partially=1)
            if property_status=='Unfurnished':
                furn_obj=Furnish.objects.create(unfurnished=1)

                new_property=Property.objects.create(name=str(property_type) +str(" - ")++ str(property_status) ,location=loaction,status=1,budget=price,furnish=furn_obj)
                print new_property.id
        except Exception as rr:
                print (rr)

        # return HttpResponseRedirect("/owner/owner_property")

	