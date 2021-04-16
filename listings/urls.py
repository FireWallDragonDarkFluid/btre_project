from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='listings'), # '' 表示 /listings  # 所以左邊這一行指的是  "連到listings裡面views的index

    # 目標:: 讓網址輸入/listings/23(也就是編號)
    path('<int:listing_id>',views.listing,name='listing'),
    path('search',views.search,name='search') # 這邊不是用 /listings/search ，因為這個search不只會用在listing裡
]