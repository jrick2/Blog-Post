from django.urls import path
from users import views
from myblog.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("sign_up", views.sign_up, name="sign_up")
]