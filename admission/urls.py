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
    path('post_index', views.post_index, name="post_index"),
    path('thankyou', views.thankyou, name="thankyou"),
    path('sslc/<str:admission_number>/<str:admissionFor>/', views.sslc, name="sslc"),
    path('hsc/<str:admission_number>/', views.hsc, name="hsc"),
    path('diploma/<str:admission_number>/', views.diploma, name="diploma"),
    path('academic_details/<str:admission_number>/', views.academic_details, name="academic_details"),
    path('show_pdf/', academic.create_pdf, name='show_pdf'),
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

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)