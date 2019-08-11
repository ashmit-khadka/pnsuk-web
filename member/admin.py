from django.contrib import admin
from .models import Member
from .models import Trustee
from .models import Advisor

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role'
        )

class TrusteeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role'        
        )

class AdvisorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        )              
admin.site.register(Member, MemberAdmin)
admin.site.register(Trustee, TrusteeAdmin)
admin.site.register(Advisor, AdvisorAdmin)