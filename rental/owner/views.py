# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from search.models import OwnerInfo

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
        print (request.POST)
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        check_email = OwnerInfo.objects.filter(email=email)
        check_mobile = OwnerInfo.objects.filter(mobile=mobile)
        if check_email:
            return redirect('/owner/owner_dashboard/')
        if check_mobile:
            return redirect('/owner/owner_dashboard/')
        else:
            owner_register = OwnerInfo(email=email, mobile=mobile,password=password)
            owner_register.save()

      
class OwnerLogin(TemplateView):
    template_name = "owner_login.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerLogin, self).get_context_data()
        return context
class OwnerAddProperty(TemplateView):
    template_name = "owner_add_property.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerAddProperty, self).get_context_data()
        return context


	