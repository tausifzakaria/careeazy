from django.contrib import admin

import Profile.models as models


class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'phone',
        'blood_group',
        'dob',
        'profile_pic',
        'user',
        'address',
    )
    list_filter = (
        'dob',
        'user',
        'address',
        'id',
        'phone',
        'blood_group',
        'profile_pic',
    )


class DoctorProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'phone',
        'speciality',
        'dob',
        'profile_pic',
        'user',
        'address',
    )
    list_filter = (
        'dob',
        'user',
        'address',
        'id',
        'phone',
        'speciality',
        'profile_pic',
    )


class AddressAdmin(admin.ModelAdmin):

    list_display = ('id', 'city', 'landmark', 'pincode', 'address')
    list_filter = ('id', 'city', 'landmark', 'pincode', 'address')


class ClinicProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'open_time',
        'close_time',
        'open_days',
        'address',
    )
    list_filter = (
        'address',
        'id',
        'name',
        'open_time',
        'close_time',
        'open_days',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.UserProfile, UserProfileAdmin)
_register(models.DoctorProfile, DoctorProfileAdmin)
_register(models.Address, AddressAdmin)
_register(models.ClinicProfile, ClinicProfileAdmin)