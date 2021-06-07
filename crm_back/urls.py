from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from student.views import StudentViewSet
from group.views import GroupViewSet, CourseListCreateView


# swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('group', GroupViewSet)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/docs/', schema_view.with_ui()),
   path('api/v1/', include('account.urls')),
   path('api/v1/', include('bill.urls')),
   path('api/v1/', include('group.urls')),
   path('api/v1/', include(router.urls)),
]
