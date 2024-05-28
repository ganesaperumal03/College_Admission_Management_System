from application.views.dashboard import (
    dashboard,
    personal_update,
    address_update,
    sslc_update,
    hsc_update,
    academic_update,
    update_index,
    ad,
    cse,
    civil,
    ece,
    eee,
    csbs,
    mech,
    it,
    name_search,
    dip_name_search,
    export_to_excel,
    export_page,
    export_to_personal_excel,
    export_to_excel_colum,
    export_to_excel_column,
    data_changed,
    delete,
    no_auth,
    certificate_view,
    certificate_view_excel,
    transport_dashboard,
        update_bus_number_check,
    update_bus_data,
    store_admissionno,
    update_mode

)

from application.views.preform_dashboard import (
    preform_dashboard,
    preform_ad,
    preform_cse,
    preform_civil,
    preform_ece,
    preform_eee,
    preform_csbs,
    preform_mech,
    preform_it,
    preform_data_changed,
    student_info,
    preform__delete,
    preform_update,
    preform_update_index,
    preform_sslc_update,
    preform_diploma_update,
    preform_declare_update,
    pre_export_to_excel,
    pre_name_search
)

from application.views.postform import (
   index,
   login,
   signup,
   post_index,
   postform,
   address,
   sslc,
   hsc,
   diploma,
   academic_details,
   thankyou,
   preview,
   pdf_check,
   postform_view,
   dashboard_pdf_show,
   certificate_check,
   office_check,
   bus_number_check,
   bus_root_check,
   certificate_dashboard,
   image_upload,
   image_check,
   qrcode
   
   
)

from application.views.preform import (
 preform_pesonal,
 preform_hsc,
 preform_diploma,
 preform_declare,
 pre_index,
 preform_pdf_check,
 preform_login

)

from application.views.post_pdf import (
 post_aca,
 post_voc,
 post_dip,
 post_dip_aca,
 post_dip_voc,

)

from application.views.pre_pdf import (
 pre_aca,
 pre_voc

)
from application.views.personal_form import (
personal_form,
personalform_dashboard,
personalform_ad,
personalform_cse,
personalform_civil,
personalform_ece,
personalform_eee,
personalform_mech,
personalform_it,
personalform_csbs,
gm_conformation,
date_filter,
personal_form_login,
check_form,
logout,
reception_dashboard


)
from application.views.fees import (
fees,
fees_form
)



__all__ = [
    index,
    postform,
    login,
    signup,
    post_index,
    pdf_check,
    address,
    sslc,
   hsc,
   diploma,
   academic_details,
   postform_view,
   thankyou,
   dashboard,
    personal_update,
    address_update,
    sslc_update,
    hsc_update,
    academic_update,
    update_index,
    ad,
    cse,
    civil,
    ece,
    eee,
    csbs,
    mech,
    it,
    name_search,
    dip_name_search,
    export_to_excel,
    export_to_excel_colum,
    export_page,
    export_to_personal_excel,
    export_to_excel_column,
    data_changed,
    delete,
    preform_login,
    preform_pesonal,
    preform_hsc,
    preform_diploma,
    preform_declare,
    preform_dashboard,
    preform__delete,


    preform_ad,
    preform_cse,
    preform_civil,
    preform_ece,
    preform_eee,
    preform_csbs,
    preform_mech,
    preform_it,
    preform_data_changed,
    student_info,
    post_aca,
    post_voc,
    post_dip,
    post_dip_aca,
    post_dip_voc,
    preview,
    pre_index,
    pre_aca,
    pre_voc,
    preform_pdf_check,
    preform_update,
    preform_update_index,
        preform_sslc_update,
    preform_diploma_update,
    preform_declare_update,
    pre_export_to_excel,
    pre_name_search,
    personal_form,
    personalform_dashboard,
    personalform_ad,
    personalform_cse,
    personalform_civil,
    personalform_ece,
    personalform_eee,
    personalform_mech,
    personalform_it,
    personalform_csbs,
    gm_conformation,
    date_filter,
    personal_form_login,
    check_form,
    logout,
    reception_dashboard,
    fees,
    fees_form,
    no_auth,
    dashboard_pdf_show,
    office_check,
    certificate_check,
    bus_number_check,
    bus_root_check,
    certificate_dashboard,
    image_upload,
    image_check,
    qrcode,
    certificate_view,
    transport_dashboard,
            update_bus_number_check,
    update_bus_data,
    store_admissionno,
    update_mode,
    ]
