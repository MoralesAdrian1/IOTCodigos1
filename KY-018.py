from machine import Pin, SoftI2C, ADC
from time import sleep
import ssd1306

# Declarar pines para la interfaz I2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declarar objeto del tipo display OLED con la interfaz I2C
display = ssd1306.SSD1306_I2C(128, 64, i2c)

ledPin = Pin(15, Pin.OUT)
#sensor LDR
sensor = ADC(Pin(34))

sensor.atten(ADC.ATTN_11DB) #atenuación
sensor.width(ADC.WIDTH_12BIT) #resolución

def mostrar_datos_en_pantalla(dato):
    # Limpiar la pantalla
    display.fill(0)
    # Mostrar el dato en la pantalla OLED
    display.text("LDR: {}".format(dato), 0, 0, 1)
    display.show()

while True:
    dato = sensor.read()
    mostrar_datos_en_pantalla(dato)
    sleep(2)
    # Se enciende un led en 985
    # Se apaga a 853
    if dato > 853:
        ledPin.value(1)
    else:
        ledPin.value(0)
