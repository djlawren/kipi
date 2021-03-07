
import subprocess
import time
import threading

class MinecraftProcess():

    __process = None
    __lock = threading.Lock()

    def __init__(self):
        
        if MinecraftProcess.__process != None:
            raise Exception("This is a singleton")
        else:

            MinecraftProcess.__lock.acquire()

            MinecraftProcess.__process = subprocess.Popen(
                args=["java", "-Djava.net.preferIPv4Stack=true", "-Xmx2500M", "-Xms2500M", "-jar", "paper-1.16.5-467.jar", "nogui"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            MinecraftProcess.__lock.release()

    @staticmethod
    def start_server():
        
        if MinecraftProcess.__process == None:
            MinecraftProcess()

            return True
        else:
            return False

    @staticmethod
    def kill_server():
        
        if MinecraftProcess.__process == None:
            print("Server not running")
            return

        MinecraftProcess.__lock.acquire()
        MinecraftProcess.__process.kill()

        while MinecraftProcess.__process.returncode == None:
            print("Waiting for kill")
            time.sleep(1)
        
        MinecraftProcess.__process = None
        MinecraftProcess.__lock.release()

    @staticmethod
    def restart_server():

        MinecraftProcess.kill_server()
        MinecraftProcess.start_server()
