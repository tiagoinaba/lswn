import platform
import time
from pywifi import PyWiFi

def get_signal_strength(interface):
    wifi = PyWiFi()
    iface = wifi.interfaces()[interface]
    iface.scan()
    time.sleep(2)  # Wait for scanning to complete
    networks = iface.scan_results()
    for network in networks:
        print("SSID:", network.ssid, "BSSID:", network.bssid, "Signal Strength (dBm):", network.signal)

if __name__ == "__main__":
    if platform.system() == "Windows":
        interface_index = 0  # Change this to the index of your WiFi interface
        get_signal_strength(interface_index)
    elif platform.system() == "Linux":
        print("Unsupported platform!")
