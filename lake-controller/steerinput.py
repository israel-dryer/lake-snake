from gpiozero import RotaryEncoder
steeringEncoder = RotaryEncoder(20,21)
class EncoderSteering:
    
    #Newer code is faster and doesnt have faulty readings
    def __init__(self):
        
        self.Encoder_Net_Rotation = 0
    def Rotated_CC(self):
        self.Encoder_Net_Rotation -= 10
    def Rotated_C(self):
        self.Encoder_Net_Rotation += 10
        
    def update(self):
        steeringEncoder.when_rotated_counter_clockwise=self.Rotated_CC
        steeringEncoder.when_rotated_clockwise=self.Rotated_C
