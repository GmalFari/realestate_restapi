from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import( 
    UserAccount,
                    Profile)

# UserModel = get_user_model()


# class VerificationInline(admin.StackedInline):
#     model = User
#     can_delete = False
#     verbose_name_plural = 'verification'


# class UserAdmin(BaseUserAdmin):
#     inlines = (VerificationInline,)


admin.site.register(UserAccount)
# admin.site.register(User)
