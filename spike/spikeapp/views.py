from django.shortcuts import render
from .models import User

# Create your views here.
def user_view(request):
    users = User.objects.all()
    return render(request, 'spikeapp/user-view.html', {'user': users})