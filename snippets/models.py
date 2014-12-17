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

class AnimalTestCase(unittest.TestCase):
    def setUp(self):
        self.lion = Animal.objects.create(name="lion", sound="roar")
        self.cat = Animal.objects.create(name="cat", sound="meow")

    def testSpeaking(self):
        self.assertEqual(self.lion.speak(), 'The lion says "roar"')
        self.assertEqual(self.cat.speak(), 'The cat says "meow"')