// Señales Digitales

int BA = 36;
int BP = 35;

int LED1 = 26;
int LED2 = 27;
int LED3 = 14;

// Señales internas
int X0 = 0;
int X1 = 0;

int M0 = 0;

int Y0 = 0;
int Y1 = 0;
int Y2 = 0;



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
  pinMode(LED3, OUTPUT);
  Serial.begin(115200);

  TON[0].tiempo = (unsigned long) 12000;
  TON[1].tiempo = (unsigned long) 3000;
  TON[2].tiempo = (unsigned long) 6000;
  
}

void loop() {

  M0 = (X0 || M0) && !X1;
  
  TON[0].entrada = M0 && !TON[2].salida;    // Señal de entrada al TON
  actualizarTON(0);

  TON[1].entrada = M0 && TON[0].salida;    // Señal de entrada al TON
  actualizarTON(1);

  TON[2].entrada = M0 && TON[1].salida;    // Señal de entrada al TON
  actualizarTON(2);

  
  Y0 = M0 && !TON[0].salida;
  
  Y1 = M0 && TON[0].salida && !TON[1].salida;
  
  Y2 = M0 && TON[1].salida;

  // Lectura de entradas y escritura de salidas
  X0 = digitalRead(BA);
  X1 = digitalRead(BP);

  digitalWrite(LED1, Y0);
  digitalWrite(LED2, Y1);
  digitalWrite(LED3, Y2);

  Serial.printf("R  %d A  %d V  %d\n", Y0, Y1, Y2);
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
