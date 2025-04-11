from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.views.decorators.http import require_GET


# API to get CSRF token and set the cookie
@ensure_csrf_cookie
@require_GET
def get_csrf(request):
    return JsonResponse({'message': 'CSRF cookie set'})


# Note API – requires authentication
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-timestamp')
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


# Signup view – uses Django's default user form
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect('/api/notes/')  # Optional: redirect to notes view
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
