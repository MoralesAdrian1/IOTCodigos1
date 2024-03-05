from machine import Pin, ADC, SoftI2C
from time import sleep
import ssd1306

# Declarar pines para la interfaz I2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declarar objeto del tipo display OLED con la interfaz I2C
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Definir los pines para los ADC
vrx = ADC(Pin(33))
vry = ADC(Pin(35))


vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

# Resolución a 4096 valores
vrx.width(ADC.WIDTH_12BIT)
vry.width(ADC.WIDTH_12BIT)

def mostrar_datos_en_pantalla(valorx, valory):
    # Limpiar la pantalla
    display.fill(0)
    # Mostrar los datos en la pantalla OLED
    display.text("Valor X: {}".format(valorx), 0, 0, 1)
    display.text("Valor Y: {}".format(valory), 0, 20, 1)
    display.show()

while True:
    valorx = vrx.read()
    valory = vry.read()
    mostrar_datos_en_pantalla(valorx, valory)
    sleep(0.1)
