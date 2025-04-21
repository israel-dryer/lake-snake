from steerinput import EncoderSteering
from lcddisplay import display


draw = display(30,40,"TESTING")
steering = EncoderSteering()

class RadioController:
    def __init__(self):
        self.InstrumentMode = "Applied Speed"
        
    def CurrentInstrument(self):
        print("Current Instrument")
    
    
    
    def CheckForInstrumentUpdate(self):
        if self.InstrumentMode == "Applied Speed":
            draw = display(20,30,"Applied Speed:" + str(steering.Encoder_Net_Rotation))
            
    def update(self):
        self.CheckForInstrumentUpdate()
        draw.DrawText()
        
radio = RadioController()
while True:
    radio.update()
    
        