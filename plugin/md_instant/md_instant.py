# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import sys
import os
import json
from markdown2 import markdown

import ws

markdown_options = ["tables", "code-friendly"]
current_dir = os.path.dirname(os.path.abspath(__file__))


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == '/':
            f = open(current_dir+'/index.html', 'r')
            data = f.read()
            data = bytes(data, "utf-8")
            self.wfile.write(data)
            f.close()
        try:
            f = open(self.path[1:], 'rb')
            self.wfile.write(f.read())
            f.close()
        except:
            pass


def sendall(data):
    #html = markdown('\n'.join(data), markdown_options)
    html = markdown('\n'.join(data), extras = markdown_options)
    threading.Thread(target=ws.sendall, args=(json.dumps(html),)).start()


def startbrowser():
    url = 'http://localhost:7000/'
    if sys.platform.startswith('darwin'):
        os.system('open -g %s &' % url)
    elif sys.platform.startswith('win'):
        os.system('start %s &'+url)
    else:
        os.system('xdg-open %s > /dev/null &' % url)

t_ws = None
t_server = None


def startserver():
    s = HTTPServer(('', 7000), MyHandler)
    s.serve_forever()


def stopserver():
    print('stop')
    t_ws._stop()
    t_server._stop()


def main():
    global t_server, t_ws
    t_ws = threading.Thread(target=ws.main)
    t_server = threading.Thread(target=startserver)
    t_ws.daemon = True
    t_server.daemon = True
    t_ws.start()
    print("t_ws Thread started target ws.main()")
    t_server.start()
    print("t_server Thread started target startserver 7000 server")
