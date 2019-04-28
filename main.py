import RPi.GPIO as GPIO
import time


def init_servo():
	GPIO.setmode(GPIO.BCM)

	gp_out = 12
	GPIO.setup(gp_out, GPIO.OUT)
	servo = GPIO.PWM(gp_out, 50)

	return servo


def tap(servo):
	servo.start(0.0)

	servo.ChangeDutyCycle(10.0)
	time.sleep(0.5)

	servo.ChangeDutyCycle(8.0)
	time.sleep(0.5)

	GPIO.cleanup()


if __name__ == "__main__":
	servo = init_servo()
	tap(servo)

