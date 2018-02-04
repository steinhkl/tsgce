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
        #print ("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.data_string = self.data_string.decode("utf-8")
        #print (self.data_string)
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
        #print (query_d)
        #print (query_d['sentence'])
        #print (query_d['sentence'][0])
        sentence = query_d['sentence'][0]


        print (sentence)
        result1 = start.main(sentence)
        #result1 = {'userInput': 'this is a test sentence.', 'ngrams': [{'length': 3, 'ngram': [{'error_at': 1, 'ngram': ['is', 'a', 'test']}, {'error_at': 2, 'ngram': ['a', 'test', 'sentence']}, {'error_at': 3, 'ngram': ['test', 'sentence']}]}], 'tagged': [('this', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('test', 'NN'), ('sentence', 'NN'), ('.', '.')], 'forms': [{'sentence': 'this be a test sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this am a test sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this are a test sentence.', 'parsehits': 1, 'APIhits': '0'}, {'sentence': 'this is a test sentence.', 'parsehits': 16700, 'APIhits': '2100'}, {'sentence': 'this are a test sentence.', 'parsehits': 1, 'APIhits': '0'}, {'sentence': 'this being a test sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this was a test sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this were a test sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this was a test sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this were a test sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this been a test sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this a test is sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this is a sentence test.', 'parsehits': 1, 'APIhits': '0'}, {'sentence': 'this a test is sentence.', 'parsehits': 0, 'APIhits': '0'}, {'sentence': 'this is a test sentence.', 'parsehits': 16700, 'APIhits': '2100'}, {'sentence': 'this a is test sentence.', 'parsehits': 3, 'APIhits': '0'}]}
        print (result1)


        self.wfile.write(json.dumps(result1).encode())

        return


def run(server_class=HTTPServer, handler_class=S, port=8099):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    print ('Server started on Port', port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
