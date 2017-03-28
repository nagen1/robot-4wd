from gpiozero import DistanceSensor

ultra = DistanceSensor(echo=40, trigger=38)
print(ultra.distance)

while True:
    print(ultra.distance)
