#!/usr/bin/env python3
import http.server
import socketserver
import os

# Set the port - use environment variable for deployment, fallback to 5000 for dev
PORT = int(os.getenv("PORT", 5000))
HOST = "0.0.0.0"  # Bind to all interfaces to work with Replit's proxy

# Change to the directory containing the HTML files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add cache control headers to prevent caching issues in Replit
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Server running at http://{HOST}:{PORT}/")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever()