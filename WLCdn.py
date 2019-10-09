#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import fileinput
import sys

WLC_NGX_SERVER_NAME="ArvanCloud"
WLC_NGX_VAR="ARVANCLOUD"
WLC_NGX_ERR_PAGE_301='''
"<html><head>" CRLF
"<title>Moved Permanently (301)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Moved Permanently (301)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_302='''
"<html><head>" CRLF
"<title>Found (302)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Found (302)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_303='''
"<html><head>" CRLF
"<title>See Other (303)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>See Other (303)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_307='''
"<html><head>" CRLF
"<title>Temporary Redirect (307)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Temporary Redirect (307)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_308='''
"<html><head>" CRLF
"<title>Permanent Redirect (308)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Permanent Redirect (308)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_400='''
"<html><head>" CRLF
"<title>Bad Request (400)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Bad Request (400)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_401='''
"<html><head>" CRLF
"<title>Authorization Required (401)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Authorization Required (401)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_402='''
"<html><head>" CRLF
"<title>Payment Required (402)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Payment Required (402)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_403='''
"<html><head>" CRLF
"<title>Forbidden (403)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Forbidden (403)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_404='''
"<html><head>" CRLF
"<title>Not Found (404)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Not Found (404)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_405='''
"<html><head>" CRLF
"<title>Not Allowed (405)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Not Allowed (405)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_405='''
"<html><head>" CRLF
"<title>Not Allowed (405)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Not Allowed (405)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_406='''
"<html><head>" CRLF
"<title>Not Acceptable (406)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Not Acceptable (406)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_408='''
"<html><head>" CRLF
"<title>Request Time-out (408)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Request Time-out (408)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_409='''
"<html><head>" CRLF
"<title>Conflict (409)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Conflict (409)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_410='''
"<html><head>" CRLF
"<title>Gone (410)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Gone (410)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_411='''
"<html><head>" CRLF
"<title>Length Required (411)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Length Required (411)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_412='''
"<html><head>" CRLF
"<title>Precondition Failed (412)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Precondition Failed (412)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_413='''
"<html><head>" CRLF
"<title>Request Entity Too Large (413)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Request Entity Too Large (413)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_414='''
"<html><head>" CRLF
"<title>Request-URI Too Large (414)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Request-URI Too Large (414)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_415='''
"<html><head>" CRLF
"<title>Unsupported Media Type (415)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Unsupported Media Type (415)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_416='''
"<html><head>" CRLF
"<title>Requested Range Not Satisfiable (416)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Requested Range Not Satisfiable (416)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_421='''
"<html><head>" CRLF
"<title>Too Many Concurrent SMTP Connections (421)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Too Many Concurrent SMTP Connections (421)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_429='''
"<html><head>" CRLF
"<title>Too Many Requests (429)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Too Many Requests (429)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_494='''
"<html><head>" CRLF
"<title>Request Header Or Cookie Too Large (400)</title></head>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Bad Request (400)</h3>" CRLF
"<h3>Request Header Or Cookie Too Large</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_495='''
"<html><head>" CRLF
"<title>The SSL certificate error (400)</title></head>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Bad Request (400)</h3>" CRLF
"<h3>The SSL certificate error</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_496='''
"<html><head>" CRLF
"<title>No required SSL certificate was sent (400)</title></head>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Bad Request (400)</h3>" CRLF
"<h3>No required SSL certificate was sent</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_497='''
"<html><head>" CRLF
"<title>The plain HTTP request was sent to HTTPS port (400)</title></head>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Bad Request (400)</h3>" CRLF
"<h3>The plain HTTP request was sent to HTTPS port</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_500='''
"<html><head>" CRLF
"<title>Internal Server Error (500)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Internal Server Error (500)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_501='''
"<html><head>" CRLF
"<title>Not Implemented (501)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Not Implemented (501)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_502='''
"<html><head>" CRLF
"<title>Bad Gateway (502)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Bad Gateway (502)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_503='''
"<html><head>" CRLF
"<title>Service Temporarily Unavailable (503)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Service Temporarily Unavailable (503)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_504='''
"<html><head>" CRLF
"<title>Gateway Time-out (504)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Gateway Time-out (504)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_505='''
"<html><head>" CRLF
"<title>HTTP Version Not Supported (505)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>HTTP Version Not Supported (505)</h3>" CRLF
;
'''
WLC_NGX_ERR_PAGE_507='''
"<html><head>" CRLF
"<title>Insufficient Storage (507)</title>" CRLF
"<style>*{margin:0;padding:0;}body{background:#eee;color:#fff;}div{background:#007878;padding:70px;margin:50px 0;}h3{color:#ddd;}</style>" CRLF
"</head><body><div>" CRLF
"<h1>Arvan Cloud</h1>" CRLF
"<h3>Insufficient Storage (507)</h3>" CRLF
;
'''

def inplace_change(filename, old_string, new_string):
    for line in fileinput.input(filename, inplace=True):
        # inside this loop the STDOUT will be redirected to the file
        # the comma after each print statement is needed to avoid double line breaks
        print line.replace(old_string, new_string),

def initialize(white_label):
    if white_label == "dotin":
        print "initialized by dotin"

def main():
    if (len(sys.argv) > 1 ):
        initialize(sys.argv[1])

    inplace_change("src/http/ngx_http_header_filter_module.c", "%WLC_NGX_SERVER_NAME%", WLC_NGX_SERVER_NAME)

    inplace_change("src/core/nginx.h", "%WLC_NGX_VAR%", WLC_NGX_VAR)
    
    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_301%", WLC_NGX_ERR_PAGE_301)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_302%", WLC_NGX_ERR_PAGE_302)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_303%", WLC_NGX_ERR_PAGE_303)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_307%", WLC_NGX_ERR_PAGE_307)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_308%", WLC_NGX_ERR_PAGE_308)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_400%", WLC_NGX_ERR_PAGE_400)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_401%", WLC_NGX_ERR_PAGE_401)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_402%", WLC_NGX_ERR_PAGE_402)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_403%", WLC_NGX_ERR_PAGE_403)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_404%", WLC_NGX_ERR_PAGE_404)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_405%", WLC_NGX_ERR_PAGE_405)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_406%", WLC_NGX_ERR_PAGE_406)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_408%", WLC_NGX_ERR_PAGE_408)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_409%", WLC_NGX_ERR_PAGE_409)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_410%", WLC_NGX_ERR_PAGE_410)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_411%", WLC_NGX_ERR_PAGE_411)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_412%", WLC_NGX_ERR_PAGE_412)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_413%", WLC_NGX_ERR_PAGE_413)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_414%", WLC_NGX_ERR_PAGE_414)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_415%", WLC_NGX_ERR_PAGE_415)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_416%", WLC_NGX_ERR_PAGE_416)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_421%", WLC_NGX_ERR_PAGE_421)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_429%", WLC_NGX_ERR_PAGE_429)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_494%", WLC_NGX_ERR_PAGE_494)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_495%", WLC_NGX_ERR_PAGE_495)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_496%", WLC_NGX_ERR_PAGE_496)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_497%", WLC_NGX_ERR_PAGE_497)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_500%", WLC_NGX_ERR_PAGE_500)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_501%", WLC_NGX_ERR_PAGE_501)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_502%", WLC_NGX_ERR_PAGE_502)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_503%", WLC_NGX_ERR_PAGE_503)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_504%", WLC_NGX_ERR_PAGE_504)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_505%", WLC_NGX_ERR_PAGE_505)

    inplace_change("src/http/ngx_http_special_response.c", "%WLC_NGX_ERR_PAGE_507%", WLC_NGX_ERR_PAGE_507)



if __name__ == '__main__':
    main()
