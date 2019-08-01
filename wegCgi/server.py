#!/usr/bin/python3
# -*- coding: utf-8 -*-
from http.server import HTTPServer, CGIHTTPRequestHandler

#端口号
port = 8000
#使用http.server模块开启一个web服务
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
