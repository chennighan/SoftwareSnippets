from django.http import Http404
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import View
from snippets.models import Snippet

def snippet_detail(request,snippet_pk):
	try:
		snippet = Snippet.objects.get(id=snippet_pk)
	except:
		raise Http404
	context = {'snippet':snippet}
	return TemplateResponse(request, 'snippets/snippet_detail.html', context)

def snippet_list(request):
	snippets = Snippet.objects.all()
	context = {'snippets':snippets}
	return TemplateResponse(request, 'snippets/snippet_list.html', context)