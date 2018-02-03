# Pageinfo app

Very simple Django app, using the [Django Rest Framework](http://www.django-rest-framework.org), no models, no database.
Takes incoming JSON formatted URLs in a POST request and returns basic information, like title and description, that it obtained from the requested page.
JSON POST request format :

{
  'url' : 'http://www.example.com'
  'title' : 'Default Title String',
  'desc' : 'Default description string',
  'keywords' : 'default,comma,separated,tag,list'
}
  
The information is returned in the same JSON format:

{
  'url'   : "http://SomePage.com",
  'title' : "The Obtained Page Title",
  'desc'  : "The Obtained page description",
  'keywords': "Comma separated list of page keyword or default" 
}


