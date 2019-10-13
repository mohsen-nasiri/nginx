#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import fileinput
import sys

flag = "arvan"

def read_to_var(var_name):
    ppath = "WLC/arvan/"
    if flag == "dotin" :
        ppath = "WLC/dotin/"

    path = ppath + var_name
    with open(path, 'r') as myfile:
        data = myfile.read().rstrip("\n")
    return data

def inplace_change(filename, var_name, new_string):
    old_string = "%" + var_name + "%"
    for line in fileinput.input(filename, inplace=True):
        # inside this loop the STDOUT will be redirected to the file
        # the comma after each print statement is needed to avoid double line breaks
        print line.replace(old_string, new_string),

def replace_var(file_name, var_name):
    new_string = read_to_var(var_name)
    inplace_change(file_name, var_name, new_string)


def main():
    if (len(sys.argv) > 1 ):
        global flag
        flag = sys.argv[1]

    replace_var("src/http/ngx_http_header_filter_module.c", "WLC_NGX_SERVER_NAME")

    replace_var("src/core/nginx.h", "WLC_NGX_VAR")
    
    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_301")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_302")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_303")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_307")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_308")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_400")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_401")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_402")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_403")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_404")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_405")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_406")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_408")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_409")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_410")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_411")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_412")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_413")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_414")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_415")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_416")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_421")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_429")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_494")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_495")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_496")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_497")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_500")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_501")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_502")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_503")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_504")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_505")

    replace_var("src/http/ngx_http_special_response.c", "WLC_NGX_ERR_PAGE_507")




if __name__ == '__main__':
    main()
