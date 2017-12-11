#!/usr/bin/env python

# A simple HTTP server that responds to POSTs by running a shell command
# Usage: python cgi_server.py &

import BaseHTTPServer
from subprocess import call

# Edit these values to control the server behavior
PORT    = 7000
COMMAND = "sleep"
ARGS    = "3"


# Define a request handler class that runs a command when it receives a POST
class RequestHandler (BaseHTTPServer.BaseHTTPRequestHandler):

    def do_POST(s):

        # Execute the command and prepare the POST response code.
        # Prints an error message to the console on failure.
        # This is a blocking function.  Use subprocess.Popen for non-blocking.
        status = call([COMMAND, ARGS])
        if status != 0:
            print "Command '{} {}' failed with code {}".format(COMMAND, ARGS, status)
            code = 500
        else:
            code = 200

        # Prepare and send the response header
        s.send_response(code)
        s.send_header("Content-type", "text/html")
        s.end_headers()

# Create and run the server
if __name__ == "__main__":
    httpd = BaseHTTPServer.HTTPServer(("", PORT), RequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
