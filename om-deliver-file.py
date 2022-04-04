from sys import argv 
from psutil import process_iter
import os
import subprocess
from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server
import time
import _thread
# ===================================================

pathname = sys.argv[1]
running = "om-sharp.exe" in (p.name() for p in process_iter())

def open_om_sharp():
    subprocess.Popen('"C:/Program Files (x86)/om-sharp/om-sharp.exe"', shell=True)

def stop_server(arg1, arg2):
    print("Stopping server...")
    server.shutdown()

if running:
    client = udp_client.SimpleUDPClient("127.0.0.1", 3003)
    client.send_message("/file", pathname)
    time.sleep(1)

else:
    _thread.start_new_thread(open_om_sharp, ())
    receiver = udp_client.SimpleUDPClient("127.0.0.1", 3003)
    dispatcher = dispatcher.Dispatcher()
    server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 9000), dispatcher)
    dispatcher.map("/send", stop_server)
    server.serve_forever()
    client = udp_client.SimpleUDPClient("127.0.0.1", 3003)
    client.send_message("/file", pathname)
    time.sleep(1)