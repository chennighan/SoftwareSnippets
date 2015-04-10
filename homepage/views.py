from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from snippets.models import Snippet

# Create your views here.
def index(request):
	snippets = Snippet.objects.all()
	topSnippets = snippets[:4]

	context = {'snippets':topSnippets}
	return TemplateResponse(request, 'SoftwareSnippets/index.html', context)