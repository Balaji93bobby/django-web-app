from django.urls import path
from .views import CustomPasswordChangeView, UserDelete, UserUpdate 

urlpatterns = [
    path('password/change/', CustomPasswordChangeView.as_view(), name="account_change_password"),
    path('<int:pk>/delete', UserDelete.as_view(), name='user_confirm_delete'),
    path('<int:pk>/update', UserUpdate.as_view(), name='user_update'),
]