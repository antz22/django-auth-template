from django.urls import path, include

from core import views

urlpatterns = [
    path('get-example-models/', views.ExampleModelsList.as_view()),
    path('create-example-model/', views.create_example_model),
]