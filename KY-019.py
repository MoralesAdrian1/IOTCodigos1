from machine import Pin, I2C
import ssd1306
import time

# Configuración de la pantalla OLED
i2c = I2C(-1, scl=Pin(12), sda=Pin(14))  # Configura la comunicación I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c) # Inicializa la pantalla OLED

# Pin del relé
PIN_RELE = Pin(2, Pin.OUT)  # Configura el pin del relé como salida

# Función para mostrar el estado del relé en la pantalla OLED
def mostrar_estado_rele(estado):
    oled.fill(0)  # Borra la pantalla
    oled.text("Relé: " + estado, 0, 0)  # Muestra el estado del relé
    oled.show()  # Actualiza la pantalla

# Ciclo principal
while True:
    # Enciende el relé
    PIN_RELE.on()
    mostrar_estado_rele("Encendido")
    time.sleep(2)  # Espera 2 segundos
    
    # Apaga el relé
    PIN_RELE.off()
    mostrar_estado_rele("Apagado")
    time.sleep(2)  # Espera 2 segundos