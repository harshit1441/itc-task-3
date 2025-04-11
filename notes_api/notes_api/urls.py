from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from notes.views import signup_view, get_csrf  # ✅ Import directly from notes.views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', include('notes.urls')),
    path('api/csrf/', get_csrf, name='csrf'),  # ✅ Correct view reference

    # Auth endpoints
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('signup/', signup_view, name='signup'),
]

