from django.contrib import admin

# Register your models here.
from crm import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_number', 'user')


admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Role)
admin.site.register(models.Team)
admin.site.register(models.TestCase)
admin.site.register(models.Function)
admin.site.register(models.Project)
admin.site.register(models.ControlTable)
admin.site.register(models.Issue)
admin.site.register(models.TestResult)
admin.site.register(models.Menu)



