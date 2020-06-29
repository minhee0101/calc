import sys, os
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)))

from cgi import parse_qs
from template import html

def application(environ, start_response):
     d = parse_qs(environ['QUERY_STRING'])
     a = d.get('a', [''])[0]
     b = d.get('b', [''])[0]

     x=0
     y=0
     
<<<<<<< HEAD
     try:
         a, b = int(a), int(b)
         x=a+b
         y=a*b
     except ValueError:
=======
     if a.isdigit() and b.isdigit():
         a, b = int(a), int(b)
         x=a+b
         y=a*b
     else:
>>>>>>> 477b9fbee0cfb19a6c7cad94718ec54f5472e0d7
         x = -1
         y = -1
     response_body = html % {
             'x': x,
             'y': y,
     }
     start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
     ])
     return [response_body]
