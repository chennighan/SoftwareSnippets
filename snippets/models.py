from django.db import models
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer, get_all_lexers
from pygments.formatters import HtmlFormatter
from django.utils import unittest

# Create your models here.
class Snippet(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	code = models.TextField()
	language = models.CharField(max_length=128)
	creation_date = models.DateTimeField()

	def __unicode__(self):
		return self.language

	def code_formatted(self):
		return highlight(self.code, get_lexer_by_name(self.language), HtmlFormatter())
		# return formatted code from pygments