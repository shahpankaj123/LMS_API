from django.urls import path
from .views import UserRegisterView,UserLoginView,Profileview,UserchangepasswordView,UserSendMailView,UserPasswordResetView,All_UserProfileView,UserProfile_ByIDView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('Userdetail/',Profileview.as_view()),
    path('changepassword/',UserchangepasswordView.as_view()),
    path('sendmail/',UserSendMailView.as_view()),
    path('reset/<uid>/<token>',UserPasswordResetView.as_view()),
    path('allUserdetail/',All_UserProfileView.as_view()),
    path('Userdetail/<id>/',UserProfile_ByIDView.as_view()),
]