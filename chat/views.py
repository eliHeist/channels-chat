from django.shortcuts import render
from django.views import View

# Create your views here.
class LobbyView(View):
    def get(self, request):
        template_name = 'chat/lobby.html'
        return render(request, template_name)