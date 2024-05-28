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
    path('address/<path:admission_number>/<str:admissionFor>/', views.address, name="address"),
    path('postform', views.postform, name="postform"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('post_index', views.post_index, name="post_index"),
    path('pre_index', views.pre_index, name="pre_index"),
    path('sslc/<path:admission_number>/<str:admissionFor>/', views.sslc, name="sslc"),
    path('hsc/<path:admission_number>/', views.hsc, name="hsc"),
    path('diploma/<path:admission_number>/', views.diploma, name="diploma"),
    path('academic_details/<path:admission_number>/', views.academic_details, name="academic_details"),
    path('post_aca/<path:admissionNo>/', views.post_aca, name="post_aca"),
    path('post_voc/<path:admissionNo>/', views.post_voc, name="post_voc"),
    path('post_dip/<path:admissionNo>/', views.post_dip, name="post_dip"),
    path('post_dip_aca/<path:admissionNo>/', views.post_dip_aca, name="post_dip_aca"),
    path('post_dip_voc/<path:admissionNo>/', views.post_dip_voc, name="post_dip_voc"),
    path('postform_view', views.postform_view, name="postform_view"),
    path('dashboard_pdf_show/<str:Aadhaar_Number>/', views.dashboard_pdf_show, name="dashboard_pdf_show"),

    path('create_pdf', academic.create_pdf, name="create_pdf"),
    path('pdf_check', views.pdf_check, name="pdf_check"),
    path('preform_pdf_check', views.preform_pdf_check, name="preform_pdf_check"),
    path('no_auth', views.no_auth, name="no_auth"),

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
    path('pre_aca/<path:admissionNo>/', views.pre_aca, name="pre_aca"),
    path('pre_voc/<path:admissionNo>/', views.pre_voc, name="pre_voc"),

    path('export_page/', views.export_page, name='export_page'),
    path('export_to_personal_excel', views.export_to_personal_excel, name='export_to_personal_excel'),
    path('export_to_excel_colum', views.export_to_excel_colum, name='export_to_excel_colum'),
    path('export_to_excel_column', views.export_to_excel_column, name='export_to_excel_column'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    path('update_index/<path:admissionNo>/', views.update_index, name="update_index"),
    path('personal_update/<path:admissionNo>/', views.personal_update, name="personal_update"),
    path('address_update/<path:admissionNo>/', views.address_update, name="address_update"),
    path('sslc_update/<path:admissionNo>/', views.sslc_update, name="sslc_update"),
    path('hsc_update/<path:admissionNo>/', views.hsc_update, name="hsc_update"),
    path('academic_update/<path:admissionNo>/', views.academic_update, name="academic_update"),
    path('data_changed/<path:admissionNo>/', views.data_changed, name="data_changed"),
    path('delete/<path:admissionNo>/', views.delete, name="delete"),

    path('pre_export_to_excel', views.pre_export_to_excel, name="pre_export_to_excel"),
    path('pre_name_search', views.pre_name_search, name="pre_name_search"),

    path('preform_pesonal', views.preform_pesonal, name="preform_pesonal"),
    path('preform_hsc', views.preform_hsc, name="preform_hsc"),
    path('preform_diploma', views.preform_diploma, name="preform_diploma"),
    path('preform_declare', views.preform_declare, name="preform_declare"),
    path('preform_login', views.preform_login, name="preform_login"),
    path('preform_update_index/<path:admissionNo>/', views.preform_update_index, name="preform_update_index"),
    path('preform_update/<path:admissionNo>/', views.preform_update, name="preform_update"),
    path('preform_sslc_update/<path:admissionNo>/', views.preform_sslc_update, name="preform_sslc_update"),
    path('preform_diploma_update/<path:admissionNo>/', views.preform_diploma_update, name="preform_diploma_update"),
    path('preform_declare_update/<path:admissionNo>/', views.preform_declare_update, name="preform_declare_update"),


    path('preform_dashboard', views.preform_dashboard, name="preform_dashboard"),
    path('preform_ad', views.preform_ad, name="preform_ad"),
    path('preform_cse', views.preform_cse, name="preform_cse"),
    path('preform_csbs', views.preform_csbs, name="preform_csbs"),
    path('preform_eee', views.preform_eee, name="preform_eee"),
    path('preform_ece', views.preform_ece, name="preform_ece"),
    path('preform_mech', views.preform_mech, name="preform_mech"),
    path('preform_it', views.preform_it, name="preform_it"),
    path('preform_civil', views.preform_civil, name="preform_civil"),
    path('preform_data_changed/<path:admissionNo>/', views.preform_data_changed, name="preform_data_changed"),
    path('preform__delete/<path:admissionNo>/', views.preform__delete, name="preform__delete"),

    path('student_info', views.student_info, name="student_info"),
    path('personal_form', views.personal_form, name="personal_form"),
    path('personalform_dashboard', views.personalform_dashboard, name="personalform_dashboard"),
    path('personalform_ad', views.personalform_ad, name="personalform_ad"),
    path('personalform_cse', views.personalform_cse, name="personalform_cse"),
    path('personalform_civil', views.personalform_civil, name="personalform_civil"),
    path('personalform_ece', views.personalform_ece, name="personalform_ece"),
    path('personalform_eee', views.personalform_eee, name="personalform_eee"),
    path('personalform_mech', views.personalform_mech, name="personalform_mech"),
    path('personalform_it', views.personalform_it, name="personalform_it"),
    path('personalform_csbs', views.personalform_csbs, name="personalform_csbs"),
    path('gm_conformation/<path:admissionNo>/', views.gm_conformation, name="gm_conformation"),
    path('date_filter', views.date_filter, name="date_filter"),
    path('personal_form_login', views.personal_form_login, name="personal_form_login"),
    path('check_form', views.check_form, name="check_form"),
    path('logout', views.logout, name="logout"),
    path('reception_dashboard', views.reception_dashboard, name="reception_dashboard"),
    path('fees/<str:value>/<path:admissionNo>/', views.fees, name="fees"),
    path('fees_form/<path:admissionNo>/', views.fees_form, name="fees_form"),
    path('office_check/<int:Aadhaar_Number>/', views.office_check, name='office_check'),
    path('certificate_check', views.certificate_check, name="certificate_check"),
    path('bus_number_check', views.bus_number_check, name="bus_number_check"),
    path('bus_root_check', views.bus_root_check, name="bus_root_check"),
    path('certificate_dashboard', views.certificate_dashboard, name="certificate_dashboard"),


    path('image_upload/<int:Aadhaar_Number>/', views.image_upload, name='image_upload'),
    path('image_check', views.image_check, name="image_check"),
    path('qrcode', views.qrcode, name="qrcode"),
    path('certificate_view', views.certificate_view, name="certificate_view"),

    path('certificate_view_excel', views.certificate_view_excel, name="certificate_view_excel"),
    path('transport_dashboard', views.transport_dashboard, name="transport_dashboard"),
    path('store_admissionno/<path:admission_no>/', views.store_admissionno, name="store_admissionno"),
    path('update_bus_data', views.update_bus_data, name="update_bus_data"),
    path('update_bus_number_check', views.update_bus_number_check, name="update_bus_number_check"),
    path('update_mode/<path:admission_no>/', views.update_mode, name="update_mode"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)