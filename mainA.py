#-----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------FUNCIONES------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------
#SUSCRIPTOR RECIBE MENSAJES 
def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'boton_1' and msg == b'prender':
    led.value(1)
    #print('ESP32B prendio el led')
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

#FUNCION QUE ESTABLECE CONEXION CON EL BROKER def connect_and_subscribe():   global client_id, mqtt_server, topic_sub   client = MQTTClient(client_id, mqtt_server)   client.set_callback(sub_cb)   client.connect()   client.subscribe(topic_sub)   print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))   return client #EN CASO DE DESCONEXION O QUE NO SE PUEDE CONECTAR  def restart_and_reconnect():   print('Failed to connect to MQTT broker. Reconnecting...')   time.sleep(10)   machine.reset()
#-----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------PROGRAMA-------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#INTENTA LA CONEXION CON EL BROKER
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()
  
#EJECUTA EL PROGRAMA
i=0
while True:
  #LED.value(1)
  try:
    client.check_msg()

    msg=b'NO'

    if boton_1.value()==1:
      msg =b'Se encendio el boton_1'
      i=1
      led.value(0)
      #MENSAJES
    if boton_2.value()==1:
      msg=b'Se encendio el boton_2'
      led.value(0)
      i=1
    if boton_3.value()==1:
      msg=b'Se encendio el boton_3'
      led.value(0)
      i=1
      #PUBLICACIONES
    if i==1:
      client.publish(topic_pub, msg)
      i=0
      sleep(0.1)

  except OSError as e:
    restart_and_reconnect()





