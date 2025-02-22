# https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
# https://www.django-rest-framework.org/
# https://www.django-rest-framework.org/tutorial/quickstart/

# Serialization:
# https://www.django-rest-framework.org/tutorial/1-serialization/https://www.django-rest-framework.org/tutorial/1-serialization/
# https://www.django-rest-framework.org/api-guide/serializers/
from rest_framework import serializers
from mybusiness.models import *
from web3sports.models import *

# Meta Class: 
# https://www.youtube.com/watch?v=NAQEj-c2CI8
# https://stackoverflow.com/questions/60500597/what-is-the-purpose-of-the-class-meta-in-django

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'age', 'team']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # corresponds to related_name in MyUser model.
    #created_businesses = serializers.PrimaryKeyRelatedField(many=True,queryset=MyBusiness.objects.all())
    created_businesses = serializers.HyperlinkedRelatedField(view_name='mybusiness-detail',read_only=True, many=True)
    #my_businesses = serializers.PrimaryKeyRelatedField(many=True, queryset=Business_User.objects.all())
    my_businesses = serializers.HyperlinkedRelatedField(view_name='business_user-detail',read_only=True, many=True)
    class Meta:
        model = MyUser
        fields = ['id','first_name','last_name','url', 'username', 'email', 'groups','created_businesses','my_businesses']
        #fields = '__all__'

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['id','status_name', 'description']

class ProvinceStateSerializer(serializers.HyperlinkedModelSerializer):
    #country = CountrySerializer(read_only=True)
    class Meta:
        model = ProvinceState
        fields = ['id','province_state_name', 'province_state_code', 'country']

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    # provinces_states has to be a related_name in the ProvinceState model's country foreingn key field.
    provinces_states = ProvinceStateSerializer(many=True, read_only=True)
    #provinces_states = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id','country_name', 'country_code','provinces_states']

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    #province_state = ProvinceStateSerializer(read_only=True)
    #country = CountrySerializer(read_only=True)
    class Meta:
        model = Address
        fields = ['id','unit_number', 'street_address','city','province_state','country','postal_code','address_type','description']


class AddressTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressType
        fields = ['id', 'address_type_name', 'description']

class ClientAddressSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta:
        model = ClientAddress
        fields = ['id', 'address','client', 'description']

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'gender_name', 'gender_code', 'description']

class EmailTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailType
        fields = ['email_type_name','description']
        
class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ['clients','email','email_type','is_primary','is_active','notes']

class PhoneTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhoneType
        fields =['id','phone_type_name','description']

class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    # https://stackoverflow.com/questions/33182092/django-rest-framework-serializing-many-to-many-field
    #clients = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=True)
    #phone_type = PhoneTypeSerializer(read_only=True)
    class Meta:
        model = Phone
        fields = ['id','clients', 'area_code','phone_number','phone_type','is_primary','is_active','is_archived','notes']
# >>> print(repr(serializer))
# ClientSerializer():
#     id = IntegerField(label='ID', read_only=True)
#     first_name = CharField(max_length=64)
#     middle_name = CharField(allow_blank=True, allow_null=True, max_length=64, required=False)
#     last_name = CharField(max_length=64)
#     birthdate = DateField()
#     sin = CharField(max_length=64)
#     gender = PrimaryKeyRelatedField(queryset=Gender.objects.all())
#     created_by = PrimaryKeyRelatedField(queryset=MyUser.objects.all())
#     created_date = DateTimeField()
#     modified_date = DateTimeField()
# >>> male = Gender(gender_name ='Male',description='Not a girl',gender_code='M')
# >>> male.save()
# >>> female = Gender(gender_name ='Female',description='Not a boy',gender_code='F')
# >>> female.sve()
# >>> me = MyUser.objects.all()[0]
# >>> foo = Client(first_name='Foo', middle_name='Dan', last_name='Bar', birthdate=parse_date('2022-12-01'), gender=male, created_by=me, created_date=parse_date('2022-12-01'), modified_date=parse_date('2022-12-01'))
# >>> foo.save()
# >>> from mybusiness.models import Client
# >>> from myapi.serializers import ClientSerializer
# >>> c = Client.objects.all()[0]
# >>> s = ClientSerializer(c)
# >>> s.data
# {'id': 1, 'first_name': 'Foo', 'middle_name': 'Dan', 'birthdate': '2022-12-01', 'last_name': 'Bar', 'sin': '', 'gender': 1, 'created_by': 1, 'created_date': '2022-12-01T00:00:00Z', 'modified_date': '2022-12-01T00:00:00Z'}
# >>> 
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    #client_addresses = ClientAddressSerializer(many=True, read_only=True)
    client_addresses = ClientAddressSerializer(many=True, read_only=True)
    #gender = GenderSerializer(read_only=True)
    phone_list = PhoneSerializer(read_only=True, many=True)

    class Meta:
        model = Client
        fields = ['phone_list','id' ,'first_name', 'middle_name','birthdate', 'last_name','sin','gender','client_addresses','created_by','created_date','modified_date']


class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = ['id','business_type_name', 'description']
    


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'product_type_name', 'description']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_type = ProductTypeSerializer()
    class Meta:
        model = Product
        fields = ['id','product_name','product_type', 'description']

class BusinessStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessStatus
        fields = ['id', 'status_name', 'description']

class BusinessUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUserRole
        fields = ['id', 'user_role_name', 'description']

class ComplianceEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceEntity
        fields = ['id', 'compliance_entity_name', 'description']

class BusinessComplianceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessComplianceEntity
        fields = ['id', 'compliance_entity', 'business', 'notes']
                         
class CollaboratorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaboratorStatus
        fields = ['id', 'status_name', 'description']

class CollaboratorPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaboratorPosition
        fields = ['id', 'position_name', 'description']

class BusinessUserSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()
    #user_role = BusinessUserRoleSerializer()
    class Meta:
        model = Business_User
        fields = ['id','business', 'user', 'split', 'user_role', 'notes', 'created_by', 'created_date', 'modified_date', 'collaborator_status', 'collaborator_position', 'cfc_code']

class InsurancePlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsurancePlan
        fields = ['id','insurance_plan_name','insurance_plan_code', 'description']

class InsuranceProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsuranceProvider
        fields = ['id','insurance_provider_name','description']


class InsurancePlaneTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsurancePlanType
        fields = ['id','insurnace_plan_type_name','insurance_plan_type_code', 'description']

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['id','document_name', 'description']

class BusinessDocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Business_Document
        fields = ['id','business', 'document', 'notes', 'is_submitted','url']

class MedicalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medical
        fields = ['id', 'medical_name', 'description']

class BusinessMedicalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Business_Medical
        fields = ['id','business', 'medical', 'notes', 'status']

class InsuranceApplicationSerializer(serializers.HyperlinkedModelSerializer):
    # provider = InsuranceProviderSerializer()
    # Cannot have below two lines as it will cause error when posting. 
    #applicant_address = AddressSerializer()
    #applicant_phone = PhoneSerializer()
    class Meta:
        model = InsuranceApplication
        fields = ['id','insured_client', 'business','product','provider','plan_type','plan','face_amount','planned_premium', 'insured_client_address','insured_client_phone', 'created_date','modified_date']

class BusinessInsuranceSerializer(serializers.HyperlinkedModelSerializer):
    insurance_application = InsuranceApplicationSerializer()
    class Meta:
        model = BusinessInsurance
        fields = ['id','business','insurance_plan','insurance_application', 'policy_number', 'notes','created_by','created_date','modified_date']

# Serializer for File Upload
# based on https://blog.vivekshukla.xyz/uploading-file-using-api-django-rest-framework/
# curl -X POST -F "file=@/Users/eugenelin/mylog.txt" -F "remark=foobar" http://127.0.0.1:8000/file/upload/ > result.html
from .models import File

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file','remark','timestamp','user','original_filename', 'business')

class MyBusinessSerializer(serializers.HyperlinkedModelSerializer):
    # Need to display policy number from related BusinessInsurance if available.
    #created_by = serializers.ReadOnlyField(source='created_by.username')
    created_by = UserSerializer(read_only=True)
    #business_insurance = serializers.PrimaryKeyRelatedField(many=True, queryset=BusinessInsurance.objects.all())
    #business_insurance = serializers.HyperlinkedRelatedField(view_name = 'businessinsurance-detail', many=True, read_only=True )
    # For some reason, setting many=False below gives error
    business_insurance = BusinessInsuranceSerializer(many=True, read_only=True)    #policy_number = business_insurance.policy_number
    #status = BusinessStatusSerializer(read_only=True)
    #status = BusinessStatusSerializer() # NOT NULL constraint failed: mybusiness_mybusiness.status_id
    #client = ClientSerializer(read_only=True)
    # set above read_only will cause "NOT NULL constraint failed: mybusiness_mybusiness.client_id"
    # having it in the serilaizer will require a dictionary for the field
    # comment out it for now hopefully will allow posting with just a URL to the client resource.
    # However, by commenting it out, the GET result will only display a URL for the client resource rather than the JSON.
    # MyBusiness.js page uses it to display the cleint name. <- Need to fix this.
    related_users = BusinessUserSerializer(many=True, read_only=True) # Advisors
    business_type = BusinessTypeSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    #Uncomment below to allow deserialize to an object rather than just a URL to the object
    insurance_application = InsuranceApplicationSerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)
    class Meta:
        model = MyBusiness 
        fields = ['id','files','insurance_application','id','business_type','product','client','status','projected_FYC','settled_FYC','application_date','settled_date','application_location','applicant_client_address','applicant_client_phone','created_by', 'created_date', 'modified_date', 'highlighted','business_insurance','related_users'] 

class BusinessSupervisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessSupervisor
        fields = ['id','business','supervisor','notes']

class BusinessApprovalSerializer(MyBusinessSerializer):

    files = FileSerializer(many=True, read_only=True)
    class Meta:
        model = MyBusiness
        fields = ['insurance_application','id','files','business_type','product','client','status','projected_FYC','settled_FYC','application_date','settled_date','application_location','created_by', 'created_date', 'modified_date', 'highlighted','business_insurance','related_users'] 

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    related_business =  MyBusinessSerializer()
    from_user = UserSerializer()
    to_user = UserSerializer()
    class Meta:
        model = Notification
        fields = ['id','read','from_user','to_user','related_business','message_text','message_code','created_date', 'broadcast_group']

class UserNotificationSerializer(serializers.HyperlinkedModelSerializer):
    notification = NotificationSerializer()
    class Meta:
        model = UserNotification
        fields = ['id','user','notification','read','created_date']

class BusinessDeclinedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessDeclined
        fields = ['id','business','notes','is_resolved','created_date']
