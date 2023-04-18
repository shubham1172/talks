from http.server import BaseHTTPRequestHandler, HTTPServer
import json

subscriptions = [
    {
        "pubsubname": "pubsub",
        "topic": "examples",
        "route": "/messages/examples"
    }
]


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/dapr/subscribe':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            subscriptionsJson = json.dumps(subscriptions)
            self.wfile.write(bytes(subscriptionsJson, 'utf-8'))
        else:
            self.send_error(404, 'Not Found')

    def do_POST(self):
        if self.path == '/messages/examples':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            print('Received example:', post_data, flush=True)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "SUCCESS"}')
        else:
            self.send_error(404, 'Not Found')


if __name__ == '__main__':
    host = 'localhost'
    port = 3000
    httpd = HTTPServer((host, port), MyHandler)
    print(f'Server running on http://{host}:{port}/')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped.")
