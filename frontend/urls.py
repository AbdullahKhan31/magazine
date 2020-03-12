from django.urls import path
from . import views


app_name = 'FrontEnd'
urlpatterns = [

    # Auditorium
    path('auditorium-reservation', views.auditorium_reservation, name='auditorium_reservation'),
    path('auditorium-list-reservation', views.auditorium_list_reservation, name='auditorium_list_reservation'),
    path('auditorium-edit-reservation/<int:reservation_id>', views.auditorium_edit_reservation, name="auditorium_edit_reservation"),
    path('auditorium-update-reservation/<int:reservation_id>', views.auditorium_update_reservation, name="auditorium_update_reservation"),
    path('auditorium-detail-reservation/<int:reservation_id>', views.auditorium_detail_reservation, name="auditorium_detail_reservation"),

    # Daycare
    path('daycare-reservation', views.daycare_reservation, name='daycare_reservation'),
    path('daycare-list-reservation', views.daycare_list_reservation, name='daycare_list_reservation'),
    path('daycare-edit-reservation/<int:reservation_id>', views.daycare_edit_reservation, name="daycare_edit_reservation"),
    path('daycare-update-reservation/<int:reservation_id>', views.daycare_update_reservation, name="daycare_update_reservation"),
    path('daycare-detail-reservation/<int:reservation_id>', views.daycare_detail_reservation, name="daycare_detail_reservation"),

]
