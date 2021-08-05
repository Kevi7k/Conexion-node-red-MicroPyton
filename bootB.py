import time
from time import sleep
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
from machine import Pin
import network
import esp
from machine import Pin
esp.osdebug(None)
import gc
gc.collect()
#CONEXION Y CLAVE DE INTERNET----------------------------------------------------------------
ssid = 'NETLIFE-C-B_EXT'
password = '0602092686'
#CONEXION AL BROKER, SIEMPRE USAR 'broker.emqx.io'--------------------------------------------
mqtt_server = 'broker.emqx.io'
client_id = ubinascii.hexlify(machine.unique_id())
#CREACION DE SUSCRIPTORES---------------------------------------------------------------------
topic_pub = b'boton_1'
#CREACION DE PUBLICADORES---------------------------------------------------------------------
topic_sub = b'boton_3'
#---------------------------------------------------------------------------------------------

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)
#CONEXION CON LA  RED------------------------------------------------------------------------
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())   

led_1=Pin(19,Pin.OUT)


led_2=Pin(18,Pin.OUT)


led_3=Pin(5,Pin.OUT)


boton_1=Pin(25,Pin.IN)




