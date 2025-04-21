class EncoderSteering:
    def __init__(self):
        
        self.Encoder_Net_Rotation = 0
        from gpiozero import Button
    
        # refer to "https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-pin-factory" and "https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.pins.pigpio.PiGPIOFactory" when making the boat wireless
     
        #ROTARY ENCODER
        #Gpiozero has a built-in encoder that may be easier and less messy
        self.pin_a = Button(20,pull_up=True)         # Rotary encoder pin A connected to GPIO20
        self.pin_b = Button(21,pull_up=True)         # Rotary encoder pin B connected to GPIO21

    

    def pin_a_rising(self):                    # Pin A event handler
        if self.pin_b.is_pressed: self.Encoder_Net_Rotation +=10  # pin A rising while A is active is a clockwise turn
        print(self.Encoder_Net_Rotation)

    def pin_b_rising(self):                    # Pin B event handler
        if self.pin_a.is_pressed: self.Encoder_Net_Rotation -=10   # pin B rising while A is active is a clockwise turn
        print(self.Encoder_Net_Rotation)

    def update(self):
        self.pin_a.when_pressed = self.pin_a_rising      # Register the event handler for pin A
        self.pin_b.when_pressed = self.pin_b_rising      # Register the event handler for pin B