from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
