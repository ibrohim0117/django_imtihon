from django.urls import path

from apps.views import (index, portfolio,
                        sign_up, login,
                        updete_servis,
                        updete_anketa,
                        updete_blog, blog,
                        updete_skill, updete_portfolio, contact_form)

urlpatterns = [
    path('index/<int:pk>/', index, name='index'),
    path('portfolio/<int:pk>/', portfolio, name='portfolio'),
    path('blog/<int:pk>/', blog, name='blog'),
    path('signup/', sign_up, name='signup'),
    path('', login, name='login'),
    path('updete_servis/<int:pk>/', updete_servis, name='updete_servis'),
    path('updete_anketa/<int:pk>/', updete_anketa, name='updete_anketa'),
    path('updete_blog/<int:pk>/', updete_blog, name='updete_blog'),
    path('updete_skill/<int:pk>/', updete_skill, name='updete_skill'),
    path('updete_portfolio/<int:pk>/', updete_portfolio, name='updete_portfolio'),
    path('contact_us/<int:pk>', contact_form, name='contact_us')

]