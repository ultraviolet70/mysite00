from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('crm/', views.crm, name='crm'),
	path('crm_insert/', views.crm_insert, name='crm_insert'),
	path('download/', views.download, name='download'),
]