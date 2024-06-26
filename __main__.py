import platform
import time
from pywifi import PyWiFi

def get_signal_strength(interface):
    wifi = PyWiFi()
    iface = wifi.interfaces()[interface]
    iface.scan()
    time.sleep(2)  # Wait for scanning to complete
    networks = iface.scan_results()
    output = "["
    for network in networks:
        close = "},"
        if network == networks[-1]:
            close = "}"
        output = output + "{" + "\"SSID\":" + f"\"{network.ssid}\"," + "\"BSSID\":" + \
            f"\"{network.bssid[:-1]}\"," + "\"RSSIdBm\":" + f"{network.signal}" + close
    output += "]"

    print(output)

if __name__ == "__main__":
    if platform.system() == "Windows":
        interface_index = 0  # Change this to the index of your WiFi interface
        get_signal_strength(interface_index)
    else:
        print("Unsupported platform!")
