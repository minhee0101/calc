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
     
     if a.isdigit() and b.isdigit():
         a, b = int(a), int(b)
         x=a+b
         y=a*b
     else:
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
