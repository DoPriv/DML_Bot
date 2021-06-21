from ppadb.client import Client as AdbClient


class ADB:
    connectionStatus = -1

    def __init__(self,name):
        # Default is "127.0.0.1" and 5037
        client = AdbClient(host="127.0.0.1", port=5037)
        device = client.device(name)

        try:
            self.connectionStatus = 0
            # Check if game is installed or not
            if (device.is_installed("com.gameloft.android.ANMP.GloftDOHM")):
                print("Starting the game !!")
                device.shell("monkey -p com.gameloft.android.ANMP.GloftDOHM 1")
            else:
                print("Game is not installed !!")
                self.connectionStatus = -1
        except:
            self.connectionStatus = -1
            print("Error Connecting to the Emulator!!")

    def getStatus(self):
        return self.connectionStatus
