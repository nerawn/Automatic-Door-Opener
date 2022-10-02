import network
from machine import Pin
from time import sleep
relay = Pin(2, Pin.OUT)
wifi = network.WLAN(network.AP_IF)
wifi.active(True)
wifi.config(essid='ESP', password='nera123456')
print(wifi.ifconfig())


def connect():
    connection = wifi.isconnected()
    wifi.active(True)

    while connection == True:
        relay.off()
        print("baglanti kuruldu")
        sleep(0.3)
        relay.on()
        sleep(5)
        wifi.active(False)
        sleep(30)
        break

    else:
        relay.on()
        print("baglanti kurulamadi")

    sleep(0.3)


while True:
    connect()
