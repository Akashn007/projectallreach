from django import forms
from .models import TechnicalForm, ScopeOfWork, ProjectTeamLeader, PTLRoles, ProjectTeamMember, PTMRoles, ProjectStatus

class TechnicalFormForm(forms.ModelForm):
    class Meta:
        model = TechnicalForm
        fields = ['client','project_no', 'work_order_date', 'project_plan', 'due_date', 'additional_info']

class ScopeOfWorkForm(forms.ModelForm):
    class Meta:
        model = ScopeOfWork
        fields = ['description']

class ProjectTeamLeaderForm(forms.ModelForm):
    class Meta:
        model = ProjectTeamLeader
        fields = ['name']

class PTLRolesForm(forms.ModelForm):
    class Meta:
        model = PTLRoles
        fields = ['role']

class ProjectTeamMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectTeamMember
        fields = ['name']

class PTMRolesForm(forms.ModelForm):
    class Meta:
        model = PTMRoles
        fields = ['role']

class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = ProjectStatus
        fields = ['status']

class TechnicalFormEditForm(forms.ModelForm):
    class Meta:
        model = TechnicalForm
        fields = ['project_no', 'work_order_date', 'project_plan', 'due_date', 'additional_info', 'client']