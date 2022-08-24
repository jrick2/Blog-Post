from django.urls import path
from users import views
from myblog.views import HomeView, Article_DetailView, Add_PostView, Update_PostView, Delete_PostView, Add_CategoryView, LikeView, CategoryView

urlpatterns = [
    # path("", views.home, name="home")
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", Article_DetailView.as_view(), name="article_detail"),
    path("add_post", Add_PostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>", Update_PostView.as_view(), name="update_post"),
    path("article/<int:pk>/delete", Delete_PostView.as_view(), name="delete_post"),
    path("sign_up/", views.sign_up, name="sign_up" ),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("category/", Add_CategoryView.as_view(), name="add_category"),
    path("like/<int:pk>", LikeView , name="like_post"),
    path("category/<str:id>/", CategoryView, name="category"),
]