from luma.core.render import canvas
from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
class display:
    def __init__(self,posX , posY , text):
        self.posX = posX
        self.posY = posY
        self.text = text
        
    def DrawText(self):
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((self.posX, self.posY), self.text , fill="white")


            