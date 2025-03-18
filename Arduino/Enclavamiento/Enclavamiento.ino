// Señales Digitales

int BA = 36;
int BP = 35;

int LED1 = 26;
int LED2 = 27;

int X0 = 0;
int X1 = 0;

int M = 0;

int Y0 = 0;
int Y1 = 0;



// Temporizadores
#define  numeroDeTON 16
struct temporizador {
    byte entrada;
    byte salida;
    unsigned long tiempo;
    unsigned long tiempoActual;
} TON[numeroDeTON];
struct temporizadorAux {
    byte bandera;
    unsigned long tiempo_Aux1;
    unsigned long tiempo_Aux2;
} TON_Aux[numeroDeTON];

void actualizarTON (int);


void setup() {
  pinMode(BA, INPUT);
  pinMode(BP, INPUT);
  
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  Serial.begin(115200);

  TON[0].tiempo = (unsigned long) 5000;
  
}

void loop() {

  Y0 = (X0 || Y0) && !X1;
  
  TON[0].entrada = Y0;    // Señal de entrada al TON
  actualizarTON(0);
  
  Y1 = TON[0].salida;

  // Lectura de entradas y escritura de salidas
  X0 = digitalRead(BA);
  X1 = digitalRead(BP);

  digitalWrite(LED1, Y0);
  digitalWrite(LED2, Y1);
}



void actualizarTON (int i) {
     if (TON [i].entrada)
   {
        if (!TON_Aux[i].bandera) {
           TON_Aux[i].bandera = true;
           TON_Aux[i].tiempo_Aux1 = millis ();  
        }
        TON_Aux[i].tiempo_Aux2 = millis ();
        TON [i].tiempoActual = TON_Aux[i].tiempo_Aux2 - TON_Aux[i].tiempo_Aux1;

        if (TON [i].tiempoActual > TON [i].tiempo) {
            TON [i].salida = true;
        }
    } else {
        TON [i].salida = false;
        TON_Aux[i].bandera = false;
    }
}
