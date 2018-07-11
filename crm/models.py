from django.db import models
from django.contrib.auth.models import User
# user: admin  pwd: admin123


# def get_team():
#     return Teams.objects.all()
#
#
# def get_leader():
#     return UserProfile.objects.all()


class UserProfile(models.Model):
    """
        账号表格
        记录登录信息
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True, null=True)  # 成对出现
    job_number = models.CharField(max_length=32, unique=True)
    shot_number = models.CharField(max_length=32, blank=True, null=True)
    phone_number = models.CharField(max_length=64, blank=True, null=True)
    belong_to_team = models.ForeignKey("Team", on_delete=models.CASCADE,  blank=True, null=True)
    # team_leader = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    university = models.CharField(max_length=128, blank=True, null=True)
    major = models.CharField(max_length=128, blank=True, null=True)
    role = models.ManyToManyField('Role')

    def __str__(self):
        return self.name


class Team(models.Model):
    """
        Team表
        记录Team信息
        一对多：
            Tester
    """
    name = models.CharField(max_length=32, blank=True, null=True)
    Team_number = models.CharField(max_length=32, blank=True, null=True)
    Team_leader = models.ForeignKey("UserProfile", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    角色表
    Tester, TestLeader, TeamLeader
    """
    name = models.CharField(max_length=32, unique=True)
    menu = models.ManyToManyField("Menu", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Role"


class Menu(models.Model):
    """
    角色菜单表
    """
    name = models.CharField(max_length=32)
    url_name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Menu"


class TestCase(models.Model):
    """
        Test case表
        记录test case.
    """
    case_id = models.CharField(max_length=64, unique=True)
    case_name = models.CharField(max_length=256, blank=True, null=True)
    function = models.ForeignKey("Function", on_delete=models.CASCADE, default="")
    procedure = models.CharField(max_length=2048, blank=True, null=True)
    pass_criteria = models.CharField(max_length=2048, blank=True, null=True)
    test_plan_pic_path = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.case_name


class Function(models.Model):
    """Functions Table"""
    function = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.function


class Project(models.Model):
    """
        Project表
        记录project信息
        多对多：
            TestCase
        一对多：
            Issue
    """
    project_id = models.CharField(max_length=256, unique=True)
    project_name = models.CharField(max_length=64, blank=True, null=True)
    test_leader_wzs = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    test_leader_whq = models.CharField(max_length=64, blank=True, null=True)
    schedule_start = models.DateField(verbose_name="开始日期")
    schedule_end = models.DateField(verbose_name="结束日期")

    def __str__(self):
        return self.project_name


class ControlTable(models.Model):
    """Control Table """
    project_name = models.ForeignKey("Project", on_delete=models.CASCADE, default="")
    function = models.ForeignKey("Function", on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.project_name

    class Meta:
        unique_together = ('project_name', 'function')
        verbose_name_plural = "Control Table"


class Issue(models.Model):
    """
        Issue表
        记录project Issue
        多对一：
            Tester
            TestLeader
    """
    issue_id = models.IntegerField(auto_created=True)
    bugzilla_id = models.CharField(max_length=32, blank=True, null=True)
    category_choices = (
        (0, 'HW'),
        (1, 'Key_Component'),
        (2, 'FW'),
        (3, 'Driver'),
        (4, 'SW'),
        (5, 'ME'),
    )
    category = models.SmallIntegerField(choices=category_choices, verbose_name='Category')
    attribute_choices = (
        (0, '[HW]Main Board'),
        (1, '[HW]Daughter Board'),
        (2, '[HW]Signal Integrity'),
        (3, '[HW]Antenna'),
        (4, '[HW]EMC/Safety'),
        (5, '[HW]Thermal'),
        (6, '[HW]Acoustic'),
        (7, '[HW]Others'),
        (8, '[KC]Chipset'),
        (9, '[KC]CPU/APU'),
        (10, '[KC]VGA'),
        (11, '[KC]Memory'),
        (12, '[KC]HDD/SDD/mSATA'),
        (13, '[KC]ODD'),
        (14, '[KC]Panel'),
        (15, '[KC]Touch Panel'),
        (16, '[KC]Camera'),
        (17, '[KC]Card Reader'),
        (18, '[KC]LAN'),
        (19, '[KC]WLAN'),
        (20, '[KC]BlueTooth'),
        (21, '[KC]Micphone'),
        (22, '[KC]KB/Mouse'),
        (23, '[KC]Remote Control'),
        (24, '[KC]Adapter/PSU'),
        (25, '[KC]USB'),
        (26, '[KC]Audio'),
        (27, '[KC]Speaker'),
        (28, '[KC]Sensor'),
        (29, '[KC]NFC'),
        (30, '[KC]TPM'),
        (31, '[KC]Others'),
        (32, '[FW]BIOS'),
        (33, '[FW]EC'),
        (34, '[FW]Inter ME'),
        (35, '[FW]Others'),
        (36, '[Driver]Chipset'),
        (37, '[Driver]CPU/APU'),
        (38, '[Driver]VGA'),
        (39, '[Driver]Touch Panel'),
        (40, '[Driver]Camera'),
        (41, '[Driver]Card Reader'),
        (42, '[Driver]LAN'),
        (43, '[Driver]WLAN'),
        (44, '[Driver]BlueTooth'),
        (45, '[Driver]Hot Key'),
        (46, '[Driver]Audio'),
        (47, '[Driver]Sensor'),
        (48, '[Driver]Others'),
        (49, '[SW]OS'),
        (50, '[SW]Application'),
        (51, '[SW]Preload'),
        (52, '[ME]Structure'),
        (53, '[ME]Cosmetic'),
        (54, '[ME]Cable'),
        (55, '[ME]Parts'),
        (56, '[ME]Packing'),
        (57, '[ME]ID'),
        (58, '[ME]Others'),
    )
    attribute = models.SmallIntegerField(choices=attribute_choices, verbose_name='attribute')
    attribute_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='ex. Intel, AMI')
    severity_choices = (
        (0, '1'),
        (1, '2'),
        (2, '3'),
        (3, '4'),
    )
    severity = models.SmallIntegerField(choices=severity_choices, verbose_name='severity')
    description = models.TextField(max_length=2048, blank=True, null=True)
    procedure = models.TextField(max_length=2048, blank=True, null=True)
    comment = models.TextField(max_length=2048, blank=True, null=True)
    root_cause = models.TextField(max_length=2048, blank=True, null=True)
    solution = models.TextField(max_length=2048, blank=True, null=True)
    status_choice = (
        (0, 'Open'),
        (1, 'Closed'),
        (2, 'Verify'),
        (3, 'Limitation'),
    )
    status = models.SmallIntegerField(choices=status_choice, verbose_name='status')
    solving_type_choices = (
        (0, 'Fixed'),
        (1, 'Spec Changed'),
        (2, 'Design'),
        (3, 'Limitation'),
        (4, 'Deferred'),
        (5, 'Withdraw'),
        (6, 'Duplicated'),
        (7, 'Cannot Duplicated'),
    )
    solving_type = models.SmallIntegerField(choices=solving_type_choices)
    open_date = models.DateField()
    verify_date = models.DateField()
    close_date = models.DateField()
    Owner = models.CharField(max_length=64, blank=True, null=True)
    motherboard_version = models.CharField(max_length=32, blank=True, null=True)
    bios_version = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=64, blank=True, null=True)
    remark = models.TextField(max_length=1024, blank=True, null=True)
    submitter = models.ForeignKey("UserProfile", verbose_name='bug 提交人', on_delete=models.CASCADE)

    def __str__(self):
        return self.issue_id


class TestResult(models.Model):
    """
        Test result表
        记录每个test case 的测试结果，
        多对一：
            TestCase
            Tester
            Project
        多对多：
            Issue
    """
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    tester = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    test_case = models.ForeignKey('TestCase', verbose_name='test case', on_delete=models.CASCADE)
    test_result_choice = (
        (0, 'Pass'),
        (1, 'Fail'),
        (2, 'N/A')
    )
    test_result = models.SmallIntegerField(choices=test_result_choice)
    issue_id = models.ForeignKey('Issue', on_delete=models.CASCADE)

    def __str__(self):
        return self.project

    class Meta:
        unique_together = ('project', 'test_case')
        verbose_name_plural = "测试结果"
