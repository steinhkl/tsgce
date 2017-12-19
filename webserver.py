#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import simplejson
import random
import start
import urllib
import cgi
import json

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Origin, Authorization, Accept, Client-Security-Token, Accept-Encoding")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>".encode())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print ("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.data_string = self.data_string.decode("utf-8")
        print (self.data_string)
        self.send_response(200)
        #self._set_headers()
        #self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Origin, Authorization, Accept, Client-Security-Token, Accept-Encoding")
        self.send_header('Content-Type', 'application/json')
        self.end_headers()


        query_d = urllib.parse.parse_qs(self.data_string)
        print (query_d)
        print (query_d['sentence'])
        print (query_d['sentence'][0])
        sentence = query_d['sentence'][0]

        #data = simplejson.loads(self.data_string)
        #with open("test123456.json", "w") as outfile:
        #    simplejson.dump(data, outfile)
        #print (self.data_string)
        print (sentence)
        #print ("{}").format(data)
        #result1 = start.main(sentence)
        print ('hello my name is what')
        #result1 = [('"This sentence is very hard."', 90300), ('"This sentence was very hard."', 9), ('"This sentence been very hard."', 0), ('"This sentence were very hard."', 0), ('"This sentence are very hard."', 0), ('"This sentence be very hard."', 0), ('"This sentence am very hard."', 0), ('"This sentence being very hard."', 0)]
        result1 = { "userinput": "The children sing a song.", "ngrams": [ [ { "error_in": "2", "ngram":[] } ] ], "tagged": [ { "word": "tag" }, { "word": "tag" } ], "forms": [ { "sentence": "The children sings a song", "tagged": [ { "word": "tag" }, { "word": "tag" } ], "googlehits": 8, "corporahits": 5 }, { "sentence": "The children sang a song", "tagged": [ { "word": "tag" }, { "word": "tag" } ], "googlehits": 2, "corporahits": 3 } ] }
        print (result1)

        #i need a valid json so i do it myself for now

        if type(result1) == list:
            print ('liste')
            result1 = '{' + result1 + '}'

        #self.wfile.write('{"testea":"test"}'.encode())
        self.wfile.write(json.dumps(result1).encode())
        #self.wfile.write('{"name":"John", "age":31, "city":"New York" }'.encode())

        #self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        #return ['test test']
        return

    def do_OPTIONS(self):
        #self._set_headers()
        print ("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.data_string = self.data_string.decode("utf-8")
        print (self.data_string)
        self.send_response(200)
        #self._set_headers()
        #self.send_header("Content-type", "text/html")
        #self.send_header("Access-Control-Allow-Origin", "*")
        #self.send_header("Access-Control-Allow-Credentials", "true")
        #self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        #self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Origin, Authorization, Accept, Client-Security-Token, Accept-Encoding")
        #self.send_header('Content-Type', 'application/json')
        #self.end_headers()


        query_d = urllib.parse.parse_qs(self.data_string)
        print (query_d)
        print (query_d['sentence'])
        print (query_d['sentence'][0])
        sentence = query_d['sentence'][0]

        #data = simplejson.loads(self.data_string)
        #with open("test123456.json", "w") as outfile:
        #    simplejson.dump(data, outfile)
        #print (self.data_string)
        print (sentence)
        #print ("{}").format(data)
        #result1 = start.main(sentence)
        print ('hello my name is what')
        #result1 = [('"This sentence is very hard."', 90300), ('"This sentence was very hard."', 9), ('"This sentence been very hard."', 0), ('"This sentence were very hard."', 0), ('"This sentence are very hard."', 0), ('"This sentence be very hard."', 0), ('"This sentence am very hard."', 0), ('"This sentence being very hard."', 0)]
        result1 = { "userinput": "The children sing a song.", "ngrams": [ [ { "error_in": "2", "ngram":[] } ] ], "tagged": [ { "word": "tag" }, { "word": "tag" } ], "forms": [ { "sentence": "The children sings a song", "tagged": [ { "word": "tag" }, { "word": "tag" } ], "googlehits": 8, "corporahits": 5 }, { "sentence": "The children sang a song", "tagged": [ { "word": "tag" }, { "word": "tag" } ], "googlehits": 2, "corporahits": 3 } ] }
        print (result1)

        #i need a valid json so i do it myself for now

        if type(result1) == list:
            print ('liste')
            result1 = '{' + result1 + '}'


        self.wfile.write(json.dumps(result1).encode())
        #self.wfile.write('{"name":"John", "age":31, "city":"New York" }'.encode())

        #self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        #return ['test test']
        return

def run(server_class=HTTPServer, handler_class=S, port=8099):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
