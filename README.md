# About
If you've ever developed software you'll know what a pain it can be to find certain code you want to recycle such as what file and project it was in. With Software Snippets you'll be able to save your snippets with multiple fields such as title, description, and keywords, to easily be searched for when you need them next. With one click copy and paste, your productivity will increase, and you won't have to waste your brain power thinking about needless things such as file locations, etc. 

#Installation
You'll need  
-Python v2.7.x   : Documentation: https://docs.python.org/2/  
-Django v1.8.x   : Documentation:  https://ocs.djangoproject.com/en/1.8/  
-Pygments v2.0.x : Documentation: http://pygments.org/docs/  
  
Once you've installed and pulled the project you'll need to do a few house keeping tasks:  
-You'll need to create a super user to access the admin interface:  
<code>$python manage.py createsuperuser</code>  
  
-You'll need to set up your database and migrate data (for now using sqlite):  
<code>$python manage.py migrate</code>  
  
  
-You should now be able to start your server:  
<code>$python manage.py runserver</code>  
