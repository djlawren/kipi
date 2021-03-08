
import subprocess
import time
import threading


class MinecraftServer():

    __process = None
    __lock = threading.Lock()

    def __init__(self):
        
        if MinecraftServer.__process != None:
            raise Exception("This is a singleton")

    @staticmethod
    def start_server():
        
        if MinecraftServer.__process == None:
            MinecraftServer.__lock.acquire()

            MinecraftServer.__process = subprocess.Popen(
                args=["java", "-Djava.net.preferIPv4Stack=true", "-Xmx2500M", "-Xms2500M", "-jar", "/home/pi/MinecraftServer1.16.5/paper-1.16.5-467.jar", "nogui"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            MinecraftServer.__lock.release()

            return True
        else:
            return False

    @staticmethod
    def kill_server():
        
        if MinecraftServer.__process == None:
            print("Server not running")
            return False

        MinecraftServer.__lock.acquire()
        MinecraftServer.__process.kill()

        while MinecraftServer.__process.returncode == None:
            print("Waiting for kill")
            time.sleep(1)
        
        MinecraftServer.__process = None
        MinecraftServer.__lock.release()

        return True

    @staticmethod
    def restart_server():

        MinecraftServer.kill_server()
        MinecraftServer.start_server()
