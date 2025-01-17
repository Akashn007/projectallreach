from rest_framework import serializers
from .models import Graphic,Technical_staff

class GraphicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graphic
        fields = ('__all__')

class TechnicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technical_staff
        fields = ('__all__')

from rest_framework import serializers
from .models import Quotation, QuotationDetails, PaymentTerm, OtherTerm

class QuotationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationDetails
        fields = ['description', 'hsn_code', 'qty', 'cost_per_qty', 'amount']

class PaymentTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTerm
        fields = ['term']

class OtherTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherTerm
        fields = ['term']

class QuotationSerializer(serializers.ModelSerializer):
    details = QuotationDetailsSerializer(many=True)
    payment_terms = PaymentTermSerializer(many=True)
    other_terms = OtherTermSerializer(many=True)

    class Meta:
        model = Quotation
        fields = ['quotation_no', 'quotation_date', 'company_name', 'company_address', 'company_gst_no',
                  'gst', 'total_amount', 'quotation_validity', 'gst_number', 'pan_number', 'delivery_schedule',
                  'additional_info', 'details', 'payment_terms', 'other_terms']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        payment_terms_data = validated_data.pop('payment_terms')
        other_terms_data = validated_data.pop('other_terms')

        quotation = Quotation.objects.create(**validated_data)

        for detail_data in details_data:
            QuotationDetails.objects.create(quotation=quotation, **detail_data)

        for payment_term_data in payment_terms_data:
            PaymentTerm.objects.create(quotation=quotation, **payment_term_data)

        for other_term_data in other_terms_data:
            OtherTerm.objects.create(quotation=quotation, **other_term_data)

        return quotation

#meeting/anusha
from rest_framework import serializers
from .models import Meeting, MeetingAttendee

class MeetingAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingAttendee
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    attendees = MeetingAttendeeSerializer(many=True)

    class Meta:
        model = Meeting
        fields = '__all__'

    def create(self, validated_data):
        attendees_data = validated_data.pop('attendees')
        meeting = Meeting.objects.create(**validated_data)
        for attendee_data in attendees_data:
            attendee, _ = MeetingAttendee.objects.get_or_create(**attendee_data)
            meeting.attendees.add(attendee)
        return meeting


#work_order/sindhu
from rest_framework import serializers
from .models import WorkOrder

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ['id', 'po_number', 'date', 'scope_of_work']
