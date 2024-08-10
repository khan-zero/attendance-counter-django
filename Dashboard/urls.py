from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('accounts/', views.accounts, name='accounts'),
    path('security/', views.security, name='security'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register-staff/', views.create_staff, name='register_staff'),
    path('attendance-create/', views.create_attendance, name='attendance_create'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('update-password/', views.update_password, name='update_password'),
    path('delete-attendance/<int:attendance_id>/', views.delete_attendance, name='delete_attendance'),
    path('edit-attendance/<int:attendance_id>/', views.edit_attendance, name='edit_attendance'),
    path('list', views.list, name='list'),
    path('list-delete/<int:staff_id>/', views.delete_staff, name='list_delete'),
    path('list-edit/<int:staff_id>/', views.edit_staff, name='list_edit'),

]
