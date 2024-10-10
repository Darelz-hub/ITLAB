from django.urls import path, include
import Information_about_IT_LAB.views as information


app_name = 'information'
urlpatterns = [
    path('', information.BasicInformation.as_view(), name='basic_information'), # основная страница
    path('maindocumentspage/', information.MainDocumentsPage.as_view(), name='main_documents_page'),
    path('management/', information.ManagementPage.as_view(), name='management_page'),
]