import time
import gpiod
from gpiod.line import Direction, Value

# Variables físicas
LED = 17
BOTON1 = 14
BOTON2 = 15

#Variables Virtuales
X0 = False
X1 = False

Y = False

M = False

chip = gpiod.Chip("/dev/gpiochip0")
request = chip.request_lines(
    consumer="prueba led",
    config={
        # Entrada digital
        BOTON1: gpiod.LineSettings(direction=Direction.INPUT),
        BOTON2: gpiod.LineSettings(direction=Direction.INPUT),

        # Salida digital
        LED: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE)
    }
)
try:
    while True:
        # Mapeo de variables
        X0 = True if request.get_value(BOTON1) == Value.ACTIVE else Value.INACTIVE
        X1 = True if request.get_value(BOTON2) == Value.ACTIVE else Value.INACTIVE

        request.set_value(LED, Value.ACTIVE if Y == True else Value.INACTIVE)

        # Programa
        Y = (X0 or Y) and not X1

        # request.set_value(LED, Value.INACTIVE)
        # time.sleep(1)
        # request.set_value(LED, Value.ACTIVE)
        # time.sleep(1)

        # boton = request.get_value(BOTON1)
        # print(boton, boton.value)
        time.sleep(0.1)

except KeyboardInterrupt:
    print ("El usuario termino el programa")
finally:
    request.release()
    chip.close()
