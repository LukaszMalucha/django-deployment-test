from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('authenticate/', views.CreateTokenView.as_view(), name='authenticate'),
    path('my_account/', views.ManageUserView.as_view(), name='my_account')

]

