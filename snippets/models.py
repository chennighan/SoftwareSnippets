from django.db import models
from pygments import highlight
from pygments.lexers import HtmlLexer,JavascriptLexer
from pygments.formatters import HtmlFormatter
from django.utils import unittest

# Create your models here.
class Snippet(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	code = models.TextField()
	creation_date = models.DateTimeField()

	def code_formatted(self):
		return highlight(self.code, HtmlLexer(), HtmlFormatter())
		# return formatted code from pygments

class SnippetTest(unittest.TestCase):
    def code_formatted_test(self):
        self.assertEqual(self.lion.speak(), 'The lion says "roar"')
        self.assertEqual(self.cat.speak(), 'The cat says "meow"')