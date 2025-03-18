from machine import Pin,I2C
from pi4ioe5v6408ztaex import PI4IOE5V6408
from gc9a01 import LCD_1inch28 
import time
        
# Initialize the I2C bus with the specified pins and frequency
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400_000)

# Create an instance of the PI4IOE5V6408 class with the I2C bus
io_expander = PI4IOE5V6408(i2c)

io_expander.write_pin(4, True)
time.sleep(1)
io_expander.write_pin(2, True)
time.sleep(1)

LCD = LCD_1inch28()
LCD.text("California Vision, Inc.",30,90,LCD.blue)
LCD.show()
LCD.write_text("California",40,120,2,LCD.red)
LCD.show()
LCD.write_text("Vision",70,140,2,LCD.red)
LCD.show()
LCD.write_text("test",70,170,3,LCD.black)
LCD.show()
time.sleep(5)
    
while True:
    LCD.fill(LCD.red)
    LCD.show()
    time.sleep(1)
    LCD.fill(LCD.green)
    LCD.show()
    time.sleep(1)
    LCD.text("California Vision, Inc.",30,120,LCD.blue)
    LCD.show()
    LCD.write_text("test",90,150,3,LCD.red)
    LCD.show()
    time.sleep(2)
    LCD.fill(LCD.blue)
    LCD.show()
    time.sleep(1)
    
    LCD.text("California Vision, Inc.",30,90,LCD.green)
    LCD.show()
    LCD.write_text("California",40,120,2,LCD.red)
    LCD.show()
    LCD.write_text("Vision",70,140,2,LCD.red)
    LCD.show()
    LCD.write_text("test",70,170,3,LCD.black)
    LCD.show()
    time.sleep(2)
    
    LCD.fill(LCD.red)
    LCD.show()
    time.sleep(1)
    
    LCD.text("California Vision, Inc.",30,90,LCD.blue)
    LCD.show()
    LCD.write_text("California",40,120,2,LCD.black)
    LCD.show()
    LCD.write_text("Vision",70,140,2,LCD.white)
    LCD.show()
    LCD.write_text("test",70,170,3,LCD.red)
    LCD.show()
    time.sleep(2)
    
    """
    LCD.fill(LCD.red)
    LCD.show()
    time.sleep(1)
    LCD.write_text("California Vision, Inc.",30,90,LCD.green)
    LCD.show()
    LCD.write_text("California",40,120,2,LCD.blue)
    LCD.show()
    LCD.write_text("Vision",70,140,2,LCD.black)
    LCD.show()
    LCD.write_text("test",70,170,3,LCD.red)
    LCD.show()
    time.sleep(5)
    """