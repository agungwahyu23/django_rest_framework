from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserListView, UserDetailView, DeleteUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', UserDetailView.as_view()),
    path('users/<int:id>/', DeleteUserView.as_view(), name='user-delete'),
    path("logout/", LogoutView.as_view()),
    path("list/", UserListView.as_view()),
]
