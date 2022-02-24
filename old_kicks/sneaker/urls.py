from django.urls import path, include
from sneaker import views

urlpatterns = [
    path('featured-sneakers/', views.FeaturedSneakers.as_view()),
    path('sneakers/search/', views.search),
    path('sneakers/<slug:brand_slug>/<slug:sneaker_slug>/', views.SneakerInfo.as_view()),
    path('sneakers/<slug:brand_slug>/', views.BrandInfo.as_view()),
]
