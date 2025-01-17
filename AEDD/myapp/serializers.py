from rest_framework import serializers
from .models import Client, ClientAddress, ClientContact, ClientEmail, ContactPersonNumber, ContactPersonEmail

class ClientSerializer(serializers.ModelSerializer):
    addresses = serializers.StringRelatedField(many=True)
    company_contacts = serializers.StringRelatedField(many=True)
    company_emails = serializers.StringRelatedField(many=True)
    contact_person_numbers = serializers.StringRelatedField(many=True)
    contact_person_emails = serializers.StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = '__all__'


class ClientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddress
        fields = '__all__'


class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = '__all__'


class ClientEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientEmail
        fields = '__all__'


class ContactPersonNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPersonNumber
        fields = '__all__'


class ContactPersonEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPersonEmail
        fields = '__all__'


# client_followup
from rest_framework import serializers
from .models import FollowUp

class FollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '_all_'

#e_diary_creation
from rest_framework import serializers
from .models import EDiary

class EDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EDiary
        fields = '__all__'

#enquiry
from rest_framework import serializers
from .models import Enquiry
class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'
        