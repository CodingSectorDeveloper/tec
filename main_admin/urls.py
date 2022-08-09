from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('courses/', views.courses, name="courses"),
    path('students/', views.student_record_list, name="students"),
    path('software/', views.software, name="software"),
    path('create_notice/', views.create_notice, name="create_notice"),
    path('material_required/', views.material_required, name="material_required"),
    path('material_entry/', views.material_entry, name="material_entry"),
    path('notices/', views.notice, name="notices"),
    path('create_course/', views.create_course, name="create_course"),
    path('branch_admins/', views.branch_admins, name="branch_admins"),
    path('zonal_admins/', views.zonal_admins, name="zonal_admins"),
    path('regional_admins/', views.regional_admins, name="regional_admins"),
    path('create_branch_admin/', views.create_branch_admin, name="create_branch_admin"),
    path('create_zonal_admin/', views.create_zonal_admin, name="create_zonal_admin"),
    path('create_regional_admin/', views.create_regional_admin, name="create_regional_admin"),
    path('delete_branch_admin/<int:id>/', views.delete_branch_admin, name="delete_branch_admin"),
    path('delete_zonal_admin/<int:id>/', views.delete_zonal_admin, name="delete_zonal_admin"),
    path('delete_regional_admin/<int:id>/', views.delete_regional_admin, name="delete_regional_admin"),
]
