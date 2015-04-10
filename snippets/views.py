from django.http import Http404
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import View
from snippets.models import Snippet
from django.views.decorators.http import require_http_methods
from datetime import datetime
from django.db import models

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

@require_http_methods(["GET", "POST"])
def snippet_new(request):
	if request.method == 'POST':
		# Process Form Input
		title = request.POST.get('title', False)
		desc = request.POST.get('description', False)
		code = request.POST.get('code', False)
		language = request.POST.get('language', False)

		#Save created snippet
		snippet = Snippet()
		snippet.title = title
		snippet.description = desc
		snippet.code = code
		snippet.language = language
		snippet.creation_date = datetime.now()
		snippet.save()
		
		return redirect('snippets:list')
	elif request.method == 'GET':
		return TemplateResponse(request, 'snippets/snippet_new.html', {})