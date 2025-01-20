from django.db import models

class TechnicalForm(models.Model):
    project_no = models.CharField(max_length=100)
    work_order_date = models.DateField()
    project_plan = models.TextField()
    due_date = models.DateField()
    additional_info = models.TextField(blank=True, null=True)
    client = models.ForeignKey('myapp.Client', on_delete=models.CASCADE, null=True, blank=True)
class ScopeOfWork(models.Model):
    technical_form = models.ForeignKey(TechnicalForm, on_delete=models.CASCADE, related_name='scope_of_work')
    description = models.TextField()

class ProjectTeamLeader(models.Model):
    technical_form = models.ForeignKey(TechnicalForm, on_delete=models.CASCADE, related_name='project_team_leaders')
    name = models.CharField(max_length=100)

class PTLRoles(models.Model):
    technical_form = models.ForeignKey(TechnicalForm, on_delete=models.CASCADE, related_name='ptl_roles')
    role = models.TextField()

class ProjectTeamMember(models.Model):
    technical_form = models.ForeignKey(TechnicalForm, on_delete=models.CASCADE, related_name='project_team_members')
    name = models.CharField(max_length=100)

class PTMRoles(models.Model):
    technical_form = models.ForeignKey(TechnicalForm, on_delete=models.CASCADE, related_name='ptm_roles')
    role = models.TextField()

class ProjectStatus(models.Model):
    technical_form = models.ForeignKey(TechnicalForm, on_delete=models.CASCADE, related_name='project_status')
    status = models.TextField()

