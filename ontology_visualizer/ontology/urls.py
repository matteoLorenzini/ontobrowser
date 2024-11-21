from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('upload/', views.upload_ontology, name='upload_ontology'),
    path('load_existing_ontology/', views.load_existing_ontology, name='load_existing_ontology'),
    path('browse/', views.browse_ontology, name='browse_ontology'),
    path('class-details/', views.class_details, name='class_details'),
    path('property-details/', views.property_details, name='property_details'),
]