from django.urls import path
from .views import *
urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup_view, name='signup'),
    path('post/<id>/', details_view, name='detailPost'),
    path('<category>/', category_view, name='categoryPost'), 
]