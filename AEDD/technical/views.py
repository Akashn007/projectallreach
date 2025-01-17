from django.shortcuts import render, redirect
from .forms import TechnicalFormForm
from .models import ScopeOfWork, ProjectTeamLeader, PTLRoles, ProjectTeamMember, PTMRoles, ProjectStatus

def techform_view(request):
    if request.method == 'POST':
        form = TechnicalFormForm(request.POST)
        if form.is_valid():
            technical_form = form.save()

            # Save Scope of Work
            scope_data = request.POST.getlist('scope_of_work[]')
            for scope in scope_data:
                ScopeOfWork.objects.create(technical_form=technical_form, description=scope)

            # Save Project Team Leaders
            leader_data = request.POST.getlist('project_team_leader[]')
            for leader in leader_data:
                ProjectTeamLeader.objects.create(technical_form=technical_form, name=leader)

            # Save PTL Roles
            ptl_roles_data = request.POST.getlist('ptl_roles[]')
            for role in ptl_roles_data:
                PTLRoles.objects.create(technical_form=technical_form, role=role)

            # Save Project Team Members
            member_data = request.POST.getlist('project_team_member[]')
            for member in member_data:
                ProjectTeamMember.objects.create(technical_form=technical_form, name=member)

            # Save PTM Roles
            ptm_roles_data = request.POST.getlist('ptm_roles[]')
            for role in ptm_roles_data:
                PTMRoles.objects.create(technical_form=technical_form, role=role)

            # Save Project Status
            status_data = request.POST.getlist('project_status')
            for status in status_data:
                ProjectStatus.objects.create(technical_form=technical_form, status=status)

            return redirect('technical_table_view')


        else:
            print(form.errors)
    else:
        form = TechnicalFormForm()
    return render(request, 'technical/technical.html', {'form': form})


from django.shortcuts import render
from .models import TechnicalForm

def technical_table_view(request):
    technical_forms = TechnicalForm.objects.prefetch_related(
        'scope_of_work',
        'project_team_leaders',
        'ptl_roles',
        'project_team_members',
        'ptm_roles',
        'project_status'
    ).all()
    return render(request, 'technical/technical_list.html', {'forms': technical_forms})

