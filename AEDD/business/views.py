from django.shortcuts import render, redirect
from .models import Graphic, Technical_staff,Meeting


def business_dashboard(request):
    return render(request, 'business/business_dashboard.html')

#enquiry/akash
from django.shortcuts import render, redirect
from .models import Meeting, Enquiry, Graphic, Technical_staff
from myapp.models import Client

def add_enquiry_form(request):
    if request.method == "POST":
        # Retrieve the selected Meeting instance
        meeting_id = request.POST.get("enquiry_ref_no")
        meeting = Meeting.objects.get(id=meeting_id)

        client_id = request.POST.get("client_id")
        client = Client.objects.get(id=client_id)

        # Create an Enquiry instance
        enquiry = Enquiry.objects.create(
            client=client,
            enquiry=meeting,
            trading_services=request.POST.get("trading_services"),
            design_and_development=request.POST.get("design_and_development"),
            software_design_and_dev_engineering_analysis=request.POST.get("software_design_and_dev_engineering_analysis"),
            manufacturing=request.POST.get("manufacturing"),
            fabrication=request.POST.get("fabrication"),
            additional_information=request.POST.get("additional_information"),
        )

        # Create Graphic instances
        graphic_designs = request.POST.getlist("graphic_design[]")
        for graphic_name in graphic_designs:
            if graphic_name.strip():  # Ignore empty inputs
                Graphic.objects.create(Graphic=graphic_name, enquiry=meeting)

        # Create Technical_staff instances
        technical_staffing = request.POST.getlist("technical_staffing[]")
        for technical_name in technical_staffing:
            if technical_name.strip():  # Ignore empty inputs
                Technical_staff.objects.create(technical=technical_name, enquiry=meeting)

        return redirect("enquiry_rfq_list")  # Replace with your success page or list view

    # Fetch all Meeting instances for the dropdown
    meetings = Meeting.objects.all()
    clients = Client.objects.all()
    return render(request, "business/enquiry/enquiry_rfq_form.html", {"meetings": meetings, "clients": clients})



# View to display the list of Graphic and Technical details
def enquiry_rfq_list(request):
    # Get the search term from query parameters
    search_query = request.GET.get('q', '')

    # Base queryset with related objects prefetching for optimized queries
    enquiries = Enquiry.objects.prefetch_related(
        'client',
        'enquiry__graphic_designs',
        'enquiry__technical_staffing'
    )

    # Apply filtering if a search query is provided
    if search_query:
        enquiries = enquiries.filter(
            enquiry__enquiry_ref_no__icontains=search_query
        )  # Adjusted to ensure the query matches the correct field.

    # Render the template with enquiries and the search query for input retention
    return render(
        request,
        'business/enquiry/enquiry_rfq_list.html',
        {'enquiries': enquiries, 'search_query': search_query}
    )



from .forms import QuotationForm, QuotationDetailsForm, PaymentTermForm, OtherTermForm
from .models import Quotation, QuotationDetails, PaymentTerm, OtherTerm
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect,get_object_or_404
from .forms import QuotationForm
from .models import Quotation, QuotationDetails, PaymentTerm, OtherTerm


def create_quotation(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        
        if form.is_valid():
            # Save the main quotation
            quotation = form.save()

            # Process dynamic pricing details
            descriptions = request.POST.getlist('description[]')
            hsn_codes = request.POST.getlist('hsn_code[]')
            quantities = request.POST.getlist('qty[]')
            costs_per_qty = request.POST.getlist('cost_per_qty[]')

            for i in range(len(descriptions)):
                try:
                    QuotationDetails.objects.create(
                        quotation=quotation,
                        description=descriptions[i],
                        hsn_code=hsn_codes[i],
                        qty=int(quantities[i]),
                        cost_per_qty=float(costs_per_qty[i])
                    )
                except (ValueError, IndexError) as e:
                    print(f"Error processing pricing item {i}: {e}")

            # Process payment terms
            payment_terms = request.POST.getlist('payment_terms[]')
            for term in payment_terms:
                if term.strip():  # Ensure the term is not empty
                    PaymentTerm.objects.create(quotation=quotation, term=term)

            # Process other terms
            other_terms = request.POST.getlist('other_terms[]')
            for term in other_terms:
                if term.strip():  # Ensure the term is not empty
                    OtherTerm.objects.create(quotation=quotation, term=term)

            return redirect('quotation_list')  # Redirect to the list of quotations
    else:
        form = QuotationForm()
        meetings = Meeting.objects.all()

    return render(request, 'business/quotation/quotation_form.html', {'form': form, 'meetings': meetings})


# View to list all quotations
def quotation_list(request):
    search_query = request.GET.get('q', '')  # Capture search query from the GET parameters

    # Filter quotations based on search query
    if search_query:
        quotations = Quotation.objects.filter(quotation_no__icontains=search_query)  # Example: search by quotation number
    else:
        quotations = Quotation.objects.all()

    meetings = Meeting.objects.all()
    quotationdetails = QuotationDetails.objects.all()
    payment_terms = PaymentTerm.objects.all()
    other_terms = OtherTerm.objects.all()

    return render(request, 'business/quotation/quotation_list.html', {
        'quotations': quotations,
        'quotationdetails': quotationdetails,
        'payment_terms': payment_terms,
        'other_terms': other_terms,
        'meetings': meetings,
        'search_query': search_query
    })
def view_details(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    return render(request, 'business/quotation/quotation_view.html', {'quotation': quotation})

def edit_quotation(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)

    if request.method == 'POST':
        form = QuotationForm(request.POST, instance=quotation)
        if form.is_valid():
            form.save()
            return redirect('view_details', quotation_id=quotation.id)
    else:
        form = QuotationForm(instance=quotation)

    return render(request, 'business/quotation/edit_quotation.html', {'form': form, 'quotation': quotation})

def delete_quotation(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)

    if request.method == 'POST':
        quotation.delete()
        return redirect('quotation_list')

    return render(request, 'business/quotation/delete_quotation.html', {'quotation': quotation})


#meeting/anusha
from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from .forms import MeetingForm,AttendeeForm
from .models import Meeting, MeetingAttendee

from django.shortcuts import render
from .models import Meeting

def filter_meetings_by_ref_no(query):
    """
    Filters meetings based on the enquiry reference number.
    :param query: The search query string.
    :return: A queryset of filtered meetings.
    """
    if query:
        return Meeting.objects.select_related('client').filter(enquiry_ref_no__icontains=query)
    return Meeting.objects.select_related('client').all()

def meeting_list(request):
    # Get the search query from the GET request
    query = request.GET.get('search', '')

    # Use the filter function to get the filtered meetings
    meetings = filter_meetings_by_ref_no(query)

    # Render the results in the template
    return render(request, 'business/meeting/meeting_list.html', {
        'meetings': meetings,
        'query': query,  # Pass the search query back to the template
    })



def create_meeting(request):
    if request.method == 'POST':
        # Instantiate the form with POST data
        meeting_form = MeetingForm(request.POST)

        # Check if the meeting form is valid before proceeding
        if meeting_form.is_valid():
            # Save the meeting form and get the instance
            meeting = meeting_form.save()

            # Handle the attendees (get data from POST request)
            attendees_data = request.POST.getlist('attendee_names[]')
            emails_data = request.POST.getlist('attendee_emails[]')
            designations_data = request.POST.getlist('attendee_designations[]')
            contact_numbers_data = request.POST.getlist('attendee_contact_numbers[]')

            # Create MeetingAttendee instances and associate them with the meeting
            attendees = []
            for i in range(len(attendees_data)):
                attendee = MeetingAttendee.objects.create(
                    name=attendees_data[i],
                    email=emails_data[i],
                    designation=designations_data[i],
                    contact_number=contact_numbers_data[i]
                )
                attendees.append(attendee)

            # Add all attendees to the meeting
            meeting.attendees.add(*attendees)

            # After saving, redirect to the meeting list page
            return redirect('meeting_list')  # Adjust this to match your URL name
        else:
            # If form is invalid, print form errors to the console
            print(meeting_form.errors)

    else:
        meeting_form = MeetingForm()
    clients = Client.objects.all()

    # If GET or form invalid, render the form again
    return render(request, 'business/meeting/meeting_form.html', {'form': meeting_form,'clients': clients})

def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    return render(request, 'business/meeting/meeting_detail.html', {'meeting': meeting})

def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('meeting_list')
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'business/meeting/edit.html', {'form': form})

def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        meeting.delete()
        return redirect('meeting_list')
    return render(request, 'business/meeting/delete.html', {'meeting': meeting})


#work_order/sindhu
from django.shortcuts import render, get_object_or_404, redirect
from .models import WorkOrder
from .forms import WorkOrderForm

# List view for displaying all work orders
def work_order_list(request):
    work_orders = WorkOrder.objects.all()
    return render(request, 'business/work_order/work_order_list.html', {'work_orders': work_orders})

# Create or Edit Work Order view
def work_order_details(request, pk=None):
    if pk:
        # If pk is provided, we're editing an existing WorkOrder
        work_order = get_object_or_404(WorkOrder, pk=pk)
    else:
        # Otherwise, we're creating a new WorkOrder
        work_order = None

    if request.method == 'POST':
        form = WorkOrderForm(request.POST, request.FILES, instance=work_order)
        if form.is_valid():
            form.save()
            return redirect('work_order_list')  # Redirect to the list view or any other view after saving
    else:
        form = WorkOrderForm(instance=work_order)

    return render(request, 'business/work_order/work_order_details.html', {'form': form})


def work_order_view(request, pk):
    # Retrieve the WorkOrder object by pk, or return 404 if not found
    work_order = get_object_or_404(WorkOrder, pk=pk)

    # Render the 'work_order_detail.html' template and pass the work order object
    return render(request, 'business/work_order/view_detail.html', {'work_order': work_order})

def work_order_edit(request, pk):
    # Get the WorkOrder object by pk, or return 404 if not found
    work_order = get_object_or_404(WorkOrder, pk=pk)

    # If it's a POST request, we process the form data
    if request.method == 'POST':
        form = WorkOrderForm(request.POST, request.FILES, instance=work_order)
        if form.is_valid():
            form.save()
            return redirect('work_order_detail', pk=work_order.pk)  # Redirect to the detail page after saving
    else:
        form = WorkOrderForm(instance=work_order)

    # Render the form in the template
    return render(request, 'business/work_order/edit.html', {'form': form, 'work_order': work_order})

def work_order_delete(request, pk):
    # Get the WorkOrder object by pk, or return 404 if not found
    work_order = get_object_or_404(WorkOrder, pk=pk)

    # If it's a POST request, delete the work order
    if request.method == 'POST':
        work_order.delete()
        return redirect('work_order_list')  # Redirect to the work order list after deleting

    # Render the confirmation template for DELETE request
    return render(request, 'business/work_order/delete.html', {'work_order': work_order})
