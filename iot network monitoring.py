import socket
import threading
import json
import time
from collections import defaultdict

# Server configuration
HOST = '127.0.0.1'  # Localhost for simulation; change to your IP for network
PORT = 65432        # Port to listen on
devices_data = defaultdict(dict)  # Store data per device

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            report = json.loads(data.decode('utf-8'))
            device_id = report['device_id']
            devices_data[device_id] = report
            print(f"Received report from {device_id}")
        except Exception as e:
            print(f"Error: {e}")
            break
    conn.close()

def display_dashboard():
    while True:
        time.sleep(15)  # Update every 15 seconds
        print("\n--- Network Monitoring Dashboard ---")
        for device_id, data in devices_data.items():
            print(f"Device {device_id}:")
            print(f"  Health - CPU: {data['cpu']}% | Memory: {data['memory']}% | Uptime: {data['uptime']}s")
            print(f"  Data Flow - Packets Sent: {data['packets_sent']} | Bandwidth: {data['bandwidth']} KB/s")
        print("------------------------------------\n")

# Start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Monitor server listening on {HOST}:{PORT}")

# Dashboard thread
threading.Thread(target=display_dashboard, daemon=True).start()

# Accept connections
while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()