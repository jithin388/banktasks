
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('logon',views.logon,name='logon'),
    #path('detail',views.detail,name='detail'),
   
    path('goldrate',views.goldrate,name='goldrate'),
    #path('places',views.places,name='places'),
    path('logout',views.logout,name='logout'),
    path('data',views.data,name='data'),
    path('loandata',views.loandata,name='loandata'),
    path('',views.home,name='home'),
    path('1', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]




