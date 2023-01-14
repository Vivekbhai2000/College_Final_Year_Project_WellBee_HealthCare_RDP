from .models import SalerDetail, Product,DoctorRegistration,Petctscandetail,Ambulance
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput): 
	input_type='date'

class SalerRegisterForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={}))
	username = forms.CharField(label=("Mobile Number"),widget=forms.TextInput(attrs={'oninput':'validate()'}))
	gst = forms.CharField(label=("GST Number"),widget=forms.TextInput(attrs={}))
	shop = forms.CharField(label=("Company/Shop Name"),widget=forms.TextInput(attrs={}))
	password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={}),)
	password2  = forms.CharField(label=("Confirm"), strip=False, widget=forms.PasswordInput(attrs={}),)
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password1', 'password2','gst', 'shop']

class DoctorRegisterForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={}))
	username = forms.CharField(label=("Mobile Number"),widget=forms.TextInput(attrs={'oninput':'validate()'}))
	#gst = forms.CharField(label=("GST Number"),widget=forms.TextInput(attrs={}))
	#shop = forms.CharField(label=("Company/Shop Name"),widget=forms.TextInput(attrs={})) 
	clinic_Address = forms.CharField(widget=forms.TextInput(attrs={})) 
	locality = forms.CharField(required =True)
	city = forms.CharField(required =True) 
	password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={}),)
	password2  = forms.CharField(label=("Confirm"), strip=False, widget=forms.PasswordInput(attrs={}),)
	class Meta:
		model = DoctorRegistration
		fields = ['first_name', 'last_name', 'username','clinic_Address','locality','pincode','city','state', 'letter_head','password1', 'password2']
class PetctscanForm(forms.ModelForm):
	username = forms.CharField(label=("Mobile Number"),widget=forms.TextInput(attrs={'oninput':'validate()'}))
	#gst = forms.CharField(label=("GST Number"),widget=forms.TextInput(attrs={}))
	#shop = forms.CharField(label=("Company/Shop Name"),widget=forms.TextInput(attrs={})) 
	residential_address = forms.CharField(widget=forms.TextInput(attrs={})) 
	city = forms.CharField(required =True) 
	patient_name = forms.CharField(required =True)  
	relative_name = forms.CharField(required =False)  
	relative_number = forms.CharField(max_length=10,required =False)  
	relation = forms.CharField(required =False)  
	appointment_date = forms.DateField(widget=DateInput,required= True)
	class Meta:
		model = Petctscandetail
		fields = ['username','residential_address','pincode','city','state','patient_name','relative_name','relative_number','relation','services','appointment_slot','appointment_date']


class AmbulanceBookingForm(forms.ModelForm):
	username = forms.CharField(label=("Mobile Number"),widget=forms.TextInput(attrs={'oninput':'validate()'}))
	residential_address = forms.CharField(widget=forms.TextInput(attrs={})) 
	city = forms.CharField(required =True)  
	
	class Meta:
		model = Ambulance
		fields = [ 'username','residential_address','pincode','city','state']

class SalerAddressForm(forms.ModelForm):
	shop_Address = forms.CharField(widget=forms.TextInput(attrs={}))
	locality = forms.CharField(required =True)
	city = forms.CharField(required =True)
	alternate_mobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Alternate Mobile No(optional)'}), required = False)
	landmark = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Landmark(optional)'}), required = False)
	class Meta:
		model = SalerDetail
		fields = [
			'mobile',
			'shop_Name',
			'alternate_mobile',
			'shop_Address',
			'pincode',
			'landmark',
			'locality',
			'city',
			'state',
		]
class UpdateSalerDetailForm(forms.ModelForm):
	class Meta:
		model = SalerDetail
		fields = [
			'photo',
			'mobile',
			'shop_Name',
			'gst_Number',
			'alternate_mobile',
			'shop_Address',
			'pincode',
			'landmark',
			'locality',
			'city',
			'state',
		]

class UpdateSalerAccountDetailForm(forms.ModelForm):
	class Meta:
		model = SalerDetail
		fields = [
			'account_Holder_Name',
			'account_Number',
			'ifsc_Code',
			]