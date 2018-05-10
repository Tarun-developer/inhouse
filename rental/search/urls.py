from django.conf.urls import url
from .views import HomePage

urlpatterns = [
	url(r'^$', HomePage.as_view(), name='homepage'),
	# url(r'^sample_csv$', sample_csv, name='sample_csv')
]
