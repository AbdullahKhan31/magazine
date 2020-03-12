from django.urls import path, include
from .api import views
from . import views as app_views
from rest_framework import routers
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('user', views.UserView)
router.register('roles', views.RoleView)
router.register('user-roles', views.UserRoleView)

urlpatterns = [
    path('', include(router.urls)),
    path('list-users', views.UserListView.as_view()),
    # url(r'^set-roles', views.SetRoleAPIView.as_view()),
    # url(r'^set-manager', views.SetUserManagerAPIView.as_view()),
    # url(r'^roles', views.RoleView.as_view()),
]

