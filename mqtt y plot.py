
from matplotlib.animation import FuncAnimation
import mqttsuscrib as mq
import matplotlib.pyplot as plt

plt.style.use('dark_background')

def animate(i):   
    plt.cla()
    plt.plot(mq.mqttrecibido(),label='Potencia consumida casa')
    plt.legend(loc='upper left')
    plt.tight_layout()



ani = FuncAnimation(plt.gcf(), animate, interval=5000)

plt.tight_layout()
plt.show()
