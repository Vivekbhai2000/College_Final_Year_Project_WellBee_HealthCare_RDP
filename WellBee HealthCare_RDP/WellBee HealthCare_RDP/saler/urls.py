from django.urls import path
from . import views

urlpatterns = [
        path('', views.dashboard, name = 'dashboard'),
		path('home/', views.index, name = 'saler_home'),
        path('seller_signup/', views.seller_signup, name="seller_signup"),
        path('doctor_signup/', views.doctor_signup, name="doctor_signup"),
        path('petctscan_booking/', views.petctscan_booking, name="petctscan_booking"),
        path('ambulance_booking/', views.ambulance_booking, name="ambulance_booking"),
    	path('account_settings/', views.account_settings, name="saler_account_settings"),
    	path('add_product/', views.add_product, name="add_product"),
    	path('view_products/', views.view_products, name="view_products"),
    	path('plus_element_cart/', views.plus_element_cart),
    	path('minus_element_cart/', views.minus_element_cart),
    	path('add_to_cart/', views.add_to_cart),
    	path('delete_from_cart/', views.delete_from_cart),
        path('cart/', views.mycart, name="cart"),
    	path('MyOrders/', views.MyOrders, name="seller_orders"),
    	path("products/<str:catg>", views.view_all, name="saler_products_view_all"),
    	path("product/<int:prod_id>", views.productView, name="SalerProductView"),
    	path("checkout/", views.checkout, name = "checkout") 


	]