from django.contrib import admin
from crm import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_number', 'user', 'shot_number', 'phone_number', 'belong_to_team', 'university',
                    'major')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_leader')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', )


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_name')


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('case_id', 'case_name', 'function', 'sheet', 'procedure')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'test_leader_wzs', 'test_leader_whq', 'schedule_start',
                    'schedule_end')


class FunctionAdmin(admin.ModelAdmin):
    list_display = ('function',)


class SheetAdmin(admin.ModelAdmin):
    list_display = ('sheet',)


class ControlTableAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'control_table',)


class IssueAdmin(admin.ModelAdmin):
    list_display = ('project', 'submitter', 'issue_id', 'bugzilla_id', 'category', 'attribute', 'attribute_name', 'severity',
                    'description', 'procedure', 'comment', 'root_cause', 'solution', 'status', 'solving_type',
                    'open_date', 'verify_date', 'close_date', 'owner', 'motherboard_version', 'bios_version',
                    'os_version', 'remark')


class TestResultAdmin(admin.ModelAdmin):
    list_display = ('project', 'control_table', 'tester', 'test_case', 'test_result', 'issue_id')


class PersonalTaskAdmin(admin.ModelAdmin):
    list_display = ('tester', )


admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.TestCase, TestCaseAdmin)
admin.site.register(models.Function, FunctionAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ControlTable, ControlTableAdmin)
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.TestResult, TestResultAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Sheet, SheetAdmin)
admin.site.register(models.PersonalTask, PersonalTaskAdmin)



