import paho.mqtt.client as mqtt

listapot=[]

def mqttllamada():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set('Edu','minina')
    client.connect("185.209.193.64", 11883, 60)
    client.loop_start()

def mqttrecibido():
    mqttllamada()
    global listapot
    print(listapot)
    return listapot

def on_message(client, userdata, msg):
    
    global listapot
    dato=msg.payload
    dato=dato.decode()
    dato=int(dato)
    print(dato)
    listapot.append(dato)
    client.loop_stop()


def on_connect(client, userdata, rc, properties=None):
    client.subscribe("Potencia")



if __name__ == "__main__":
    pass
else:
    mqttrecibido()




