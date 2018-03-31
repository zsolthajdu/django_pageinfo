# Pageinfo app

Very simple Django app, using the [Django Rest Framework](http://www.django-rest-framework.org), no models, no database.  

## GET request
The url parameter can be passed to the app in a GET request:  
 http://www.mydomain.com/pageinfo/?url=http://example.com  
 The obtained site information is returned in JSON format as described below in the paragraph about the POST request

 ## POST request
Takes a JSON formatted URL in a POST request and returns basic information, like title and description, that it obtained from the requested page.  
JSON POST request format :

```
{
  'url' : 'http://www.example.com'
}
```
  
The information is returned in similar JSON format:

```
{ 
  'url'   : "http://www.example.com", 
  'title' : "The Obtained Page Title", 
  'desc'  : "The Obtained page description",
  'keywords': "Comma,separated,list,of,page,keywords" 
}
```

