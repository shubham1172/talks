from http.server import BaseHTTPRequestHandler, HTTPServer
import json

subscriptions = [
    {
        "pubsubname": "pubsub",
        "topic": "bulk-examples",
        "route": "/messages/examples",
        "bulkSubscribe": {
            "enabled": True
        }
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
            json_data = json.loads(post_data)
            print(f'Received {len(json_data["entries"])} entries', flush=True)

            # Prepare a response
            response = {
                "statuses": []
            }

            # Iterate over entries
            for entry in json_data["entries"]:
                print(f'EntryID: {entry["entryId"]}', flush=True)
                print(f'Event: {entry["event"]}', flush=True)
                print("\n\n", flush=True)

                # Mark as success
                response['statuses'].append({
                    "entryId": entry["entryId"],
                    "status": "SUCCESS"
                })

            print("Sending response", json.dumps(response), flush=True)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(response), 'utf-8'))
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
