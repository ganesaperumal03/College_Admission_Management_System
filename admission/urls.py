"""admission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.decorators import login_required
from application import views
from application import academic,duplicate
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),

    path('', views.index, name="index"),
    path('address/<str:admission_number>/<str:admissionFor>/', views.address, name="address"),
    path('postform', views.postform, name="postform"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('post_index', views.post_index, name="post_index"),
    path('pre_index', views.pre_index, name="pre_index"),
    path('sslc/<str:admission_number>/<str:admissionFor>/', views.sslc, name="sslc"),
    path('hsc/<str:admission_number>/', views.hsc, name="hsc"),
    path('diploma/<str:admission_number>/', views.diploma, name="diploma"),
    path('academic_details/<str:admission_number>/', views.academic_details, name="academic_details"),
    path('post_aca/<str:admission_number>/', views.post_aca, name="post_aca"),
    path('post_voc/<str:admission_number>/', views.post_voc, name="post_voc"),
    path('post_dip/<str:admission_number>/', views.post_dip, name="post_dip"),
    path('post_dip_aca/<str:admission_number>/', views.post_dip_aca, name="post_dip_aca"),
    path('post_dip_voc/<str:admission_number>/', views.post_dip_voc, name="post_dip_voc"),
    path('show_pdf', academic.create_pdf, name="create_pdf"),

    path('pdf_check', views.pdf_check, name="pdf_check"),

    path('populate_fake_data/', duplicate.populate_fake_data, name='populate_fake_data'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('ad', views.ad, name="ad"),
    path('cse', views.cse, name="cse"),
    path('csbs', views.csbs, name="csbs"),
    path('civil', views.civil, name="civil"),
    path('ece', views.ece, name="ece"),
    path('eee', views.eee, name="eee"),
    path('mech', views.mech, name="mech"),
    path('it', views.it, name="it"),
    path('name_search', views.name_search, name="name_search"),
    path('dip_name_search', views.dip_name_search, name="dip_name_search"),

    path('export_page/', views.export_page, name='export_page'),
    path('export_to_personal_excel', views.export_to_personal_excel, name='export_to_personal_excel'),
    path('export_to_excel_colum', views.export_to_excel_colum, name='export_to_excel_colum'),
    path('export_to_excel_column', views.export_to_excel_column, name='export_to_excel_column'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    path('update_index/<str:admissionNo>/', views.update_index, name="update_index"),
    path('personal_update/<str:admissionNo>/', views.personal_update, name="personal_update"),
    path('address_update/<str:admissionNo>/', views.address_update, name="address_update"),
    path('sslc_update/<str:admissionNo>/', views.sslc_update, name="sslc_update"),
    path('hsc_update/<str:admissionNo>/', views.hsc_update, name="hsc_update"),
    path('academic_update/<str:admissionNo>/', views.academic_update, name="academic_update"),
    path('data_changed/<str:admissionNo>/', views.data_changed, name="data_changed"),
    path('delete/<str:admissionNo>/', views.delete, name="delete"),


    path('preform_pesonal', views.preform_pesonal, name="preform_pesonal"),
    path('preform_hsc', views.preform_hsc, name="preform_hsc"),
    path('preform_diploma', views.preform_diploma, name="preform_diploma"),
    path('preform_declare', views.preform_declare, name="preform_declare"),

    path('preform_dashboard', views.preform_dashboard, name="preform_dashboard"),
    path('preform_ad', views.preform_ad, name="preform_ad"),
    path('preform_cse', views.preform_cse, name="preform_cse"),
    path('preform_csbs', views.preform_csbs, name="preform_csbs"),
    path('preform_eee', views.preform_eee, name="preform_eee"),
    path('preform_ece', views.preform_ece, name="preform_ece"),
    path('preform_mech', views.preform_mech, name="preform_mech"),
    path('preform_it', views.preform_it, name="preform_it"),
    path('preform_civil', views.preform_civil, name="preform_civil"),
    path('preform_data_changed/<str:admissionNo>/', views.preform_data_changed, name="preform_data_changed"),

    path('student_info', views.student_info, name="student_info"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)