def application(environ,start_response):
    status = '200 OK'
    html = b'<html>\n' \
           b'<body>\n' \
           b' Hooray, mod_wsgi is working\n' \
           b'</body>\n' \
           b'</html>\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]
