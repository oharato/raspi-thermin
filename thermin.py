from time import sleep
from pythonosc import osc_message_builder , udp_client
from gpiozero import DistanceSensor
import my_func
sensor = DistanceSensor(echo=17, trigger=4)
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
while True:
	pitch = 60 + my_func.step(sensor.distance, 0.06, 0.03, 12)
	sender.send_message('/play_this', pitch)
	sleep(0.5)

