from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('student_registration/', views.student_registration, name="student_registration"),
    path('prf/', views.prf, name="prf"),
    path('crf/', views.crf, name="crf"),
    path('download/', views.download, name="download"),
    path('material_entry/', views.material_entry, name="material_entry"),
    path('enquiry/', views.enquiry, name="enquiry"),
    path('material_requisition/', views.material_requisition, name="material_requisition"),
    path('student_login_creation/', views.student_login_creation, name="student_login_creation"),
    path('student_record_list/', views.student_record_list, name="student_record_list"),
    path('fees_collection/', views.fees_collection, name="fees_collection"),
    path('fees_collection_2/<int:id>', views.fees_collection_2, name="fees_collection_2"),
    path('paid/<int:id>/<int:money>', views.paid, name="paid"),
    path('notice/', views.notice, name="notice"),
    path('create_notice/', views.create_notice, name="create_notice"),
]
