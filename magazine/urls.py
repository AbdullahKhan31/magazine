"""magazine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from user_management import views as user_views
from frontend.views import (
    home_screen_view,
    main_home_screen_view,
    about_view,
    students_view,
    arr_view,
    re_view,
    research_view,
    coc_view,
    history_view,
    cuiranking_view,
    cas_view,
    ad_view,
    ss_view,
    compres_view,
    office_view,
    md_view,
    contact_view,
    po_view,
    rector_view,
    chemres_view,
    civilres_view,
    biores_view,
)


schema_view = get_swagger_view(title='Magazine API')

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('home/', main_home_screen_view, name='mainhome'),
    path('admin/', admin.site.urls),
    path('auditorium/', include('auditorium.urls')),
    path('alumni/', include('alumni.urls')),
    path('chat/', include('chat.urls')),
    path('daycare/', include('daycare.urls')),
    path('frontend/', include('frontend.urls')),
    url(r'api-docs', schema_view),
    path('login-user', user_views.login_user, name='login_user'),
    path('register-user', user_views.register_user, name='register_user'),
    path('logout-user', user_views.logout_user, name='logout_user'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

# staticurls
    path('about', about_view, name='about'),
    path('students', students_view, name='students'),
    path('arr', arr_view, name='arr'),
    path('md', md_view, name='md'),
    path('re', re_view, name='re'),
    path('research', research_view, name='research'),
    path('cuiranking', cuiranking_view, name='cuiranking'),
    path('po', po_view, name='po'),
    path('contact', contact_view, name='contact'),
    path('ad', ad_view, name='ad'),
    path('ss', ss_view, name='ss'),
    path('coc', coc_view, name='coc'),
    path('office/', office_view, name='office'),
    path('cas', cas_view, name='cas'),
    path('biores', biores_view, name='biores'),
    path('chemres', chemres_view, name='chemres'),
    path('civilres', civilres_view, name='civilres'),
    path('compres', compres_view, name='compres'),
    path('rector', rector_view, name='rector'),
    path('history', history_view, name='history'),
    # endstaticurls

]
