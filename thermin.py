from time import sleep
from pythonosc import osc_message_builder , udp_client
from gpiozero import DistanceSensor
sensor = DistanceSensor(echo=17, trigger=4)
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
while True:
	# near 0.06  far 0.03
	pitch = 60 * sensor.distance * 30
	sender.send_message('/play_this', pitch)
	sleep(0.5)

