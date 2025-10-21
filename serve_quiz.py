#!/usr/bin/env python3
"""
Simple HTTP server to serve the SnowPro quiz with external JSON loading.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

def start_server():
    """Start a local HTTP server to serve the quiz files."""
    PORT = 8000
    
    # Change to the directory containing the quiz files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create a custom handler that sets CORS headers
    class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", PORT), CORSHTTPRequestHandler) as httpd:
            print(f"🚀 SnowPro Quiz Server started!")
            print(f"📱 Server running at: http://localhost:{PORT}")
            print(f"🎯 Quiz URL: http://localhost:{PORT}/quiz_standalone.html")
            print(f"📁 Serving files from: {os.getcwd()}")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("-" * 50)
            
            # Automatically open the quiz in the default browser
            webbrowser.open(f'http://localhost:{PORT}/quiz_standalone.html')
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Trying port {PORT + 1}...")
            start_server_with_port(PORT + 1)
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)

def start_server_with_port(port):
    """Start server with a specific port."""
    class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", port), CORSHTTPRequestHandler) as httpd:
            print(f"🚀 SnowPro Quiz Server started!")
            print(f"📱 Server running at: http://localhost:{port}")
            print(f"🎯 Quiz URL: http://localhost:{port}/quiz_standalone.html")
            print(f"📁 Serving files from: {os.getcwd()}")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("-" * 50)
            
            webbrowser.open(f'http://localhost:{port}/quiz_standalone.html')
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()
