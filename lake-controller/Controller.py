from steerinput import EncoderSteering
from lcddisplay import display

class RadioController:
    def __init__(self):
        #draw = display(30,40,"TESTING")
        self.InstrumentMode = "Applied Speed"
        
    def CurrentInstrument(self):
        print("Current Instrument")
    
    
    
    def CheckForInstrumentUpdate(self):
        if self.InstrumentMode == "Applied Speed":
            draw = display(20,30,"Applied Speed:" + str(steering.Encoder_Net_Rotation))
            draw.DrawText()
             
    def updateself(self):
        steering.update()
        self.CheckForInstrumentUpdate()
        

#Instancing all of the other scripts to update them
radio = RadioController()
steering = EncoderSteering()

while True:
    radio.updateself()
