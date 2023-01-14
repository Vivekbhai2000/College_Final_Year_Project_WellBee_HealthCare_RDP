from django.db import models
from django.contrib.auth.models import User
from PIL import Image 
from django.utils import timezone
from datetime import datetime 
import django.utils.timezone

class SalerDetail(models.Model):
	SEX_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
	STATE_CHOICES = (
		("Andaman & Nicobar Islands",'Andaman & Nicobar Islands'),
		("Andhra Pradesh",'Andhra Pradesh'),
		("Arunachal Pradesh",'Arunachal Pradesh'),
		("Assam",'Assam'),
		("Bihar",'Bihar'),
		("Chandigarh",'Chandigarh'),
		("Chhattisgarh",'Chhattisgarh'),
		("Dadra & Nagar Haveli",'Dadra & Nagar Haveli'),
		("Daman and Diu",'Daman and Diu'),
		("Delhi",'Delhi'),
		("Goa",'Goa'),
		("Gujarat",'Gujarat'),
		("Haryana",'Haryana'),
		("Himachal Pradesh",'Himachal Pradesh'),
		("Jammu & Kashmir",'Jammu & Kashmir'),
		("Jharkhand",'Jharkhand'),
		("Karnataka",'Karnataka'),
		("Kerala",'Kerala'),
		("Lakshadweep",'Lakshadweep'),
		("Madhya Pradesh",'Madhya Pradesh'),
		("Maharashtra",'Maharashtra'),
		("Manipur",'Manipur'),
		("Meghalaya",'Meghalaya'),
		("Mizoram",'Mizoram'),
		("Nagaland",'Nagaland'),
		("Odisha",'Odisha'),
		("Puducherry",'Puducherry'),
		("Punjab",'Punjab'),
		("Rajasthan",'Rajasthan'),
		("Sikkim",'Sikkim'),
		("Tamil Nadu",'Tamil Nadu'),
		("Telangana",'Telangana'),
		("Tripura",'Tripura'),
		("Uttarakhand",'Uttarakhand'),
		("Uttar Pradesh",'Uttar Pradesh'),
		("West Bengal",'West Bengal'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
	photo = models.ImageField(default='default.png',upload_to='user_photos')
	mobile = models.CharField(max_length=10,null=True)
	gst_Number = models.CharField(max_length=15,null=True)
	shop_Name = models.CharField(max_length=500,null=True)
	alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
	shop_Address = models.TextField()
	pincode = models.CharField(max_length=6, null=True)
	landmark = models.CharField(max_length=500, null=True, blank=True)
	locality = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
	account_Holder_Name = models.CharField(max_length=50, null=True)
	account_Number = models.CharField(max_length=20, null=True)
	ifsc_Code = models.CharField(max_length=11, null=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.photo.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.photo.path)

class SellerSlider(models.Model):
	name = models.CharField(max_length=50, default = "", null=True)
	image = models.ImageField(upload_to='seller_slider_img')
	url = models.CharField(max_length=200, default = "#", null=True)

	def __str__(self):
		return f'{self.name}'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 1024 or img.width > 1024:
			output_size = (1024, 1024)
			img.thumbnail(output_size)
			img.save(self.image.path)


class category(models.Model):
	name = models.CharField(max_length=50, default="")
	sub_Categories  = models.TextField(default="")
	def __str__(self):
		return f'{self.name}'

class Product(models.Model):
	GST_CHOICES = (("0",'0'),("3",'3'),("5",'5'),("12",'12'),("18",'18'),("28",'28'))
	product_id = models.BigAutoField(primary_key=True)
	product_id2 = models.CharField(max_length=100,default='')
	shop = models.ForeignKey(User, on_delete=models.CASCADE,default='')
	product_name = models.CharField(max_length=100)
	category = models.ForeignKey(category, default="", verbose_name="Category", on_delete=models.SET_DEFAULT, null=True)
	subcategory = models.CharField(max_length=50, default="")
	price = models.IntegerField(default=0)
	price_not = models.IntegerField(default=999)
	desc = models.TextField()
	gst = models.CharField(default='0',max_length=3,choices=GST_CHOICES)
	pub_date = models.DateField(auto_now=True)
	image1 = models.ImageField(upload_to='products/images', default="",null=True)
	image2 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image3 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image4 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image5 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img1 = Image.open(self.image1.path)
		if img1.height > 1500 or img1.width > 1500:
			output_size = (1500, 1500)
			img1.thumbnail(output_size)
			img1.save(self.image1.path)
		if self.image2:
			img2 = Image.open(self.image2.path)
			if img2.height > 1500 or img2.width > 1500:
				output_size = (1500, 1500)
				img2.thumbnail(output_size)
				img2.save(self.image2.path)

		if self.image3:
			img3 = Image.open(self.image3.path)
			if img3.height > 1500 or img3.width > 1500:
				output_size = (1500, 1500)
				img3.thumbnail(output_size)
				img3.save(self.image3.path)

		if self.image4:
			img4 = Image.open(self.image4.path)
			if img4.height > 1500 or img4.width > 1500:
				output_size = (1500, 1500)
				img4.thumbnail(output_size)
				img4.save(self.image4.path)

		if self.image5:
			img5 = Image.open(self.image5.path)
			if img5.height > 1500 or img5.width > 1500:
				output_size = (1500, 1500)
				img5.thumbnail(output_size)
				img5.save(self.image5.path)
	def __str__(self):
		return f'{self.product_id}'

class ProductSize(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	size = models.CharField(max_length=20)
	quantity = models.IntegerField(default=0, null=True)

class ProductReview(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	review = models.TextField()
	time = models.DateTimeField(auto_now=True)

class WholeSaleProduct(models.Model):
	SEX_CHOICES = (("Male",'Male'),("Female",'Female'),("All",'All'))
	product_id = models.BigAutoField(primary_key=True)
	product_name = models.CharField(max_length=100)
	category = models.ForeignKey(category, default="", verbose_name="Category", on_delete=models.SET_DEFAULT)
	subcategory = models.CharField(max_length=50, default="")
	price = models.IntegerField(default=0)
	desc = models.TextField()
	size = models.TextField(verbose_name='Size Avialabe(Separated by Comma)')
	color = models.TextField(verbose_name='Enter Color Separated by Comma')
	min_Quantity = models.IntegerField(default=0, null=True)
	pub_date = models.DateField(auto_now=True)
	image1 = models.ImageField(upload_to='products/images', default="",null=True)
	image2 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image3 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image4 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)
	image5 = models.ImageField(upload_to='products/images', default="",null=True,blank=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img1 = Image.open(self.image1.path)
		if img1.height > 1500 or img1.width > 1500:
			output_size = (1500, 1500)
			img1.thumbnail(output_size)
			img1.save(self.image1.path)
		if self.image2:
			img2 = Image.open(self.image2.path)
			if img2.height > 1500 or img2.width > 1500:
				output_size = (1500, 1500)
				img2.thumbnail(output_size)
				img2.save(self.image2.path)

		if self.image3:
			img3 = Image.open(self.image3.path)
			if img3.height > 1500 or img3.width > 1500:
				output_size = (1500, 1500)
				img3.thumbnail(output_size)
				img3.save(self.image3.path)

		if self.image4:
			img4 = Image.open(self.image4.path)
			if img4.height > 1500 or img4.width > 1500:
				output_size = (1500, 1500)
				img4.thumbnail(output_size)
				img4.save(self.image4.path)

		if self.image5:
			img5 = Image.open(self.image5.path)
			if img5.height > 1500 or img5.width > 1500:
				output_size = (1500, 1500)
				img5.thumbnail(output_size)
				img5.save(self.image5.path)
	def __str__(self):
		return f'{self.product_id}'

class WholeSaleProductOrders(models.Model):
	STATUS_CHOICES = (("Accepted",'Accepted'),("Packed",'Packed'),("On The Way",'On The Way'),("Delivered",'Delivered'),("Cancel",'Cancel'))
	order_id = models.CharField(max_length=50,default='')
	user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
	products = models.CharField(max_length=50)
	status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='')

class dow(models.Model):
	product = models.OneToOneField(Product, default="", verbose_name="Product Id", on_delete=models.CASCADE, null=True)
	price = models.PositiveIntegerField()
	def __str__(self):
		return f'{self.product}'

class trend(models.Model):
	product = models.OneToOneField(Product, default="", on_delete=models.CASCADE, null=True)
	number = models.PositiveIntegerField()
	def __str__(self):
		return f'{self.product}'

class MyCart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product_id = models.CharField(max_length=100)
	number = models.PositiveIntegerField(default=0)

class Orders(models.Model):
	STATUS_CHOICES = (("Accepted",'Accepted'),("Packed",'Packed'),("On The Way",'On The Way'),("Delivered",'Delivered'),("Cancel",'Cancel')) 
	PAYSTATUS_CHOICES = (("Success",'Success'),("Failure",'Failure'),("Pending",'Pending'))
	ORDERTYPE_CHOICES = (("COD",'COD'),("Online Payment",'Online Payment'))
	order_id = models.CharField(max_length=70,default='')
	saler = models.CharField(max_length=100,default='wrappers@admin',)
	user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
	products = models.CharField(max_length=50)
	size = models.CharField(max_length=50,default='',null=True)
	status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='') 
	itemprice = models.CharField(default="0",max_length=10)  
	gstprice = models.CharField(default="0",max_length=10) 
	deliverycharge = models.CharField(default="0",max_length=10) 
	totalprice = models.CharField(default="0",max_length=10) 
	order_date = models.DateField(default=django.utils.timezone.now) 
	order_time=models.TimeField(default=django.utils.timezone.now) 
	order_type=models.CharField(max_length=15,choices=ORDERTYPE_CHOICES,default='COD')
	payment_status=models.CharField(max_length=15,choices=PAYSTATUS_CHOICES,default='Pending') 
	payment_failreason= models.TextField(default='No Reason') 
	orderslottime=models.CharField(default="0",max_length=20)  
	orderslotdate=models.DateField(default=django.utils.timezone.now)  
	reports =models.FileField(default='default.png',upload_to='user_reports')


class DoctorRegistration(models.Model):
	SEX_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
	STATE_CHOICES = (
		("Andaman & Nicobar Islands",'Andaman & Nicobar Islands'),
		("Andhra Pradesh",'Andhra Pradesh'),
		("Arunachal Pradesh",'Arunachal Pradesh'),
		("Assam",'Assam'),
		("Bihar",'Bihar'),
		("Chandigarh",'Chandigarh'),
		("Chhattisgarh",'Chhattisgarh'),
		("Dadra & Nagar Haveli",'Dadra & Nagar Haveli'),
		("Daman and Diu",'Daman and Diu'),
		("Delhi",'Delhi'),
		("Goa",'Goa'),
		("Gujarat",'Gujarat'),
		("Haryana",'Haryana'),
		("Himachal Pradesh",'Himachal Pradesh'),
		("Jammu & Kashmir",'Jammu & Kashmir'),
		("Jharkhand",'Jharkhand'),
		("Karnataka",'Karnataka'),
		("Kerala",'Kerala'),
		("Lakshadweep",'Lakshadweep'),
		("Madhya Pradesh",'Madhya Pradesh'),
		("Maharashtra",'Maharashtra'),
		("Manipur",'Manipur'),
		("Meghalaya",'Meghalaya'),
		("Mizoram",'Mizoram'),
		("Nagaland",'Nagaland'),
		("Odisha",'Odisha'),
		("Puducherry",'Puducherry'),
		("Punjab",'Punjab'),
		("Rajasthan",'Rajasthan'),
		("Sikkim",'Sikkim'),
		("Tamil Nadu",'Tamil Nadu'),
		("Telangana",'Telangana'),
		("Tripura",'Tripura'),
		("Uttarakhand",'Uttarakhand'),
		("Uttar Pradesh",'Uttar Pradesh'),
		("West Bengal",'West Bengal'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
	photo = models.ImageField(default='default.png',upload_to='doctor_photos')
	mobile = models.CharField(max_length=10,null=True)
	gst_Number = models.CharField(max_length=15,null=True)
	clinic_name = models.CharField(max_length=500,null=True)
	alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
	clinic_Address = models.TextField(null=True)
	pincode = models.CharField(max_length=6, null=True)
	landmark = models.CharField(max_length=500, null=True, blank=True)
	locality = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
	account_Holder_Name = models.CharField(max_length=50, null=True)
	account_Number = models.CharField(max_length=20, null=True)
	ifsc_Code = models.CharField(max_length=11, null=True) 
	letter_head=models.FileField(default='default.png',upload_to='doctor_letterhead')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.photo.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.photo.path)


class Petctscandetail(models.Model):
	LOCATION_CHOICES = (("BANGALORE",'BANGALORE'),("HYDERABAD",'HYDERABAD'),("NIC AURANGABAD",'NIC AURANGABAD'),("NIC BORIVALI",'NIC BORIVALI'),("NIC JAIPUR",'NIC JAIPUR'),("NIC NASHIK",'NIC NASHIK'),("NIC PRABHADEVI",'NIC PRABHADEVI'),("SHL DELHI",'SHL DELHI'),("SHL NAVIMUMBAI",'SHL NAVIMUMBAI')) 
	SERVICES_CHOICES = (("CTSCAN",'CTSCAN'),("FLUORIDE PET-CT BONE SCAN",'FLUORIDE PET-CT BONE SCAN'),("FDG WHOLE BODY PET-CT SCAN",'FDG WHOLE BODY PET-CT SCAN'))

	STATE_CHOICES = (
		("Andaman & Nicobar Islands",'Andaman & Nicobar Islands'),
		("Andhra Pradesh",'Andhra Pradesh'),
		("Arunachal Pradesh",'Arunachal Pradesh'),
		("Assam",'Assam'),
		("Bihar",'Bihar'),
		("Chandigarh",'Chandigarh'),
		("Chhattisgarh",'Chhattisgarh'),
		("Dadra & Nagar Haveli",'Dadra & Nagar Haveli'),
		("Daman and Diu",'Daman and Diu'),
		("Delhi",'Delhi'),
		("Goa",'Goa'),
		("Gujarat",'Gujarat'),
		("Haryana",'Haryana'),
		("Himachal Pradesh",'Himachal Pradesh'),
		("Jammu & Kashmir",'Jammu & Kashmir'),
		("Jharkhand",'Jharkhand'),
		("Karnataka",'Karnataka'),
		("Kerala",'Kerala'),
		("Lakshadweep",'Lakshadweep'),
		("Madhya Pradesh",'Madhya Pradesh'),
		("Maharashtra",'Maharashtra'),
		("Manipur",'Manipur'),
		("Meghalaya",'Meghalaya'),
		("Mizoram",'Mizoram'),
		("Nagaland",'Nagaland'),
		("Odisha",'Odisha'),
		("Puducherry",'Puducherry'),
		("Punjab",'Punjab'),
		("Rajasthan",'Rajasthan'),
		("Sikkim",'Sikkim'),
		("Tamil Nadu",'Tamil Nadu'),
		("Telangana",'Telangana'),
		("Tripura",'Tripura'),
		("Uttarakhand",'Uttarakhand'),
		("Uttar Pradesh",'Uttar Pradesh'),
		("West Bengal",'West Bengal'),
		) 
	SLOT_CHOICES = (("8:00AM-9:00AM",'8:00AM-9:00AM'),("9:00AM-10:00AM",'9:00AM-10:00AM'),("10:00AM-11:30AM",'10:00AM-11:30AM'),("6:00PM-7:00PM",'6:00PM-7:00PM'),("9:00PM-10:00PM",'9:00PM-10:00PM'))
	#user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
	#photo = models.ImageField(default='default.png',upload_to='user_photos')
	mobile = models.CharField(max_length=10,null=True)
	#gst_Number = models.CharField(max_length=15,null=True)
	#shop_Name = models.CharField(max_length=500,null=True)
	#alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
	residential_address = models.TextField()
	pincode = models.CharField(max_length=6, null=True)
	#landmark = models.CharField(max_length=500, null=True, blank=True)
	#locality = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
	#account_Holder_Name = models.CharField(max_length=50, null=True)
	#account_Number = models.CharField(max_length=20, null=True)
	#ifsc_Code = models.CharField(max_length=11, null=True) 
	patient_name= models.CharField(max_length=50,null=True) 
	relative_name= models.CharField(max_length=50,null=True) 
	relative_number= models.CharField(max_length=10,null=True)
	relation= models.CharField(max_length=30,null=True)
	services=models.CharField(max_length=50,choices=SERVICES_CHOICES, null=True)
	appointment_slot= models.CharField(max_length=30,choices=SLOT_CHOICES, null=True)
	appointment_date = models.DateField(null = True,blank=True)    

class Ambulance(models.Model):
	STATE_CHOICES = (
		("Andaman & Nicobar Islands",'Andaman & Nicobar Islands'),
		("Andhra Pradesh",'Andhra Pradesh'),
		("Arunachal Pradesh",'Arunachal Pradesh'),
		("Assam",'Assam'),
		("Bihar",'Bihar'),
		("Chandigarh",'Chandigarh'),
		("Chhattisgarh",'Chhattisgarh'),
		("Dadra & Nagar Haveli",'Dadra & Nagar Haveli'),
		("Daman and Diu",'Daman and Diu'),
		("Delhi",'Delhi'),
		("Goa",'Goa'),
		("Gujarat",'Gujarat'),
		("Haryana",'Haryana'),
		("Himachal Pradesh",'Himachal Pradesh'),
		("Jammu & Kashmir",'Jammu & Kashmir'),
		("Jharkhand",'Jharkhand'),
		("Karnataka",'Karnataka'),
		("Kerala",'Kerala'),
		("Lakshadweep",'Lakshadweep'),
		("Madhya Pradesh",'Madhya Pradesh'),
		("Maharashtra",'Maharashtra'),
		("Manipur",'Manipur'),
		("Meghalaya",'Meghalaya'),
		("Mizoram",'Mizoram'),
		("Nagaland",'Nagaland'),
		("Odisha",'Odisha'),
		("Puducherry",'Puducherry'),
		("Punjab",'Punjab'),
		("Rajasthan",'Rajasthan'),
		("Sikkim",'Sikkim'),
		("Tamil Nadu",'Tamil Nadu'),
		("Telangana",'Telangana'),
		("Tripura",'Tripura'),
		("Uttarakhand",'Uttarakhand'),
		("Uttar Pradesh",'Uttar Pradesh'),
		("West Bengal",'West Bengal'),
		) 
	mobile = models.CharField(max_length=10,null=True)
	residential_address = models.TextField()
	pincode = models.CharField(max_length=6, null=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
	ambulancebooked_date = models.DateField(default=django.utils.timezone.now) 
	ambulancebooked_time=models.TimeField(default=django.utils.timezone.now) 