# # admin.py
# from django.contrib import admin
# from django.shortcuts import render
# from .models import CustomUser
# from .form import HodAssignmentForm

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'is_hod', 'hod_dashboard_url', 'is_staff')
#     actions = ['assign_hod_url_action']

#     def assign_hod_url_action(self, request, queryset):
#         # This is a custom admin action to assign URLs to selected HODs
#         form = HodAssignmentForm()
#         return render(
#             request,
#             'admin/assign_hod_url_action.html',
#             {'form': form, 'users': queryset},
#         )

# admin.site.register(CustomUser, CustomUserAdmin)
