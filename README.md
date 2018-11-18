# Pageinfo app
[![Build Status](https://travis-ci.org/zsolthajdu/django_pageinfo.svg?branch=master)](https://travis-ci.org/zsolthajdu/django_pageinfo)  [![Known Vulnerabilities](https://snyk.io/test/github/zsolthajdu/django_pageinfo/badge.svg)](https://snyk.io/test/github/zsolthajdu/django_pageinfo)

Very simple Django app, using the [Django Rest Framework](http://www.django-rest-framework.org), no models, no database.  

## GET request
The url parameter can be passed to the app in a GET request:  
 http://www.mydomain.com/pageinfo/?url=http://example.com  
 The obtained site information is returned in JSON format as described below in the paragraph about the POST request

## POST request
Takes a JSON formatted URL in a POST request and returns basic information, like title and description, that it obtained from the requested page.  
JSON POST request format :

```language=javascript
{
  'url' : 'http://www.example.com'
}
```
  
The information is returned in similar JSON format:

```lang=javascript
{ 
  'url'   :      "http://www.example.com", 
  'title' :      "The Obtained Page Title", 
  'description' : "The Obtained page description",
  'tags':        "Comma,separated,list,of,page,keywords" 
}
```

