from machine import Pin, PWM, ADC
import time

#Setting up PWM pin
dir_a = PWM(Pin(17))
dir_a.freq(1000)
dir_a.duty_u16(0)

dir_b = PWM(Pin(16))
dir_b.freq(1000)
dir_b.duty_u16(0)

stby=Pin(18, Pin.OUT)
stby.value(1)

ball = ADC(Pin(27))
current = ADC(Pin(28))
a = 0
b = 0
t = 0

while True:
    balldet = ball.read_u16()
    print(balldet)
    if balldet < 10000:
        a = 1
        t = time.ticks_ms()
    if a == 1:
        currentdet = current.read_u16()
        print(currentdet)
        if currentdet > 60000:
            b = 1
        if t != 0 and abs(t - time.ticks_ms()) <= 10000:
            if b == 1:
                print("1")
                dir_a.duty_u16(30000)
                dir_b.duty_u16(0)
            else:
                print("2")
                dir_b.duty_u16(30000)
                dir_a.duty_u16(0)
        else:
            dir_a.duty_u16(0)
            dir_b.duty_u16(0)
    time.sleep(0.01)

                
            
    
