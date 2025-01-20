from django.shortcuts import render, redirect, get_object_or_404
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
from django.db.models import Q
def technical_table_view(request):
    search_query = request.GET.get('search', '')

    if search_query:
        technical_forms = TechnicalForm.objects.filter(
            Q(client__company_name__icontains=search_query) |  # Replace with the actual field name
            Q(project_no__icontains=search_query) |
            Q(project_plan__icontains=search_query)
        ).prefetch_related(
            'scope_of_work',
            'project_team_leaders',
            'ptl_roles',
            'project_team_members',
            'ptm_roles',
            'project_status'
        )
    else:
        technical_forms = TechnicalForm.objects.prefetch_related(
            'scope_of_work',
            'project_team_leaders',
            'ptl_roles',
            'project_team_members',
            'ptm_roles',
            'project_status'
        ).all()

    return render(request, 'technical/technical_list.html', {'forms': technical_forms})


from .forms import TechnicalFormEditForm

def edit_technical_form(request, form_id):
    technical_form = get_object_or_404(TechnicalForm, id=form_id)
    if request.method == 'POST':
        form = TechnicalFormEditForm(request.POST, instance=technical_form)
        if form.is_valid():
            form.save()
            return redirect('technical_table_view')  # Redirect to list view after saving
    else:
        form = TechnicalFormEditForm(instance=technical_form)
    return render(request, 'technical/edit_technical.html', {'form': form})

def view_technical_form(request, form_id):
    technical_form = get_object_or_404(TechnicalForm, id=form_id)
    return render(request, 'technical/view_technical.html', {'form': technical_form})

def delete_technical_form(request, form_id):
    technical_form = get_object_or_404(TechnicalForm, id=form_id)
    if request.method == 'POST':
        technical_form.delete()
        return redirect('technical_table_view')  # Redirect to list after deleting
    return render(request, 'technical/delete_technical.html', {'form': technical_form})

