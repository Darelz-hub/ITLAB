from django.urls import path, include
import Information_about_IT_LAB.views as information


app_name = 'information'
urlpatterns = [
    path('information/', information.BasicInformation.as_view(), name='basic_information'), # основная страница
]