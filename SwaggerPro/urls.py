"""SwaggerPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from Swaggerapp import views

from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

swagger_view = get_swagger_view(title='Employee API Details')
schema_view = get_swagger_view(title=' Swagger API for Employee')

swagger_docs = include_docs_urls(title='Swagger Documentation for Employee')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger_view/',schema_view),
    path('swagger_docs/',swagger_docs),

    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    #path('schemaapi/', get_schema_view(title="Emp Schema",description="API for all things …"), name='openapi-schema'),
    path('emps/',views.EmpListView.as_view()),
    path('emps/<int:pk>/',views.EmpDetailView.as_view()),
]