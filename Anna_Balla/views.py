from django.shortcuts import render, HttpResponse
from .main import main
# Create your views here.

def home(request):
    return render(request,'home.html')


def chat(request):
    query = request.GET.get('query', '')
    print(f"Received query: {query}")  # Debugging output
    content = main(query)
    return render(request, 'chat.html', {'content': content})


