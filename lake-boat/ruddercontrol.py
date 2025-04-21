class rudder:
    def __init__(self):
        ex['sudo','pigpiod']
        from gpiozero import AngularServo #Angular servo allows for exact degrees of rotation
        from gpiozero.pins.pigpio import PiGPIOFactory #A different pin factory for more precise measurment from the pot in the servo
        self.s = AngularServo(12, pin_factory = self.factory, min_angle=-100, max_angle=100)
        
        self.factory = PiGPIOFactory()
    
    def Move(self , rot):
        s.angle(rot)
    #"sudo pigpiod" to initialize the pigpio server
    
        
            