// Calibração da celula de carga

// Bibliotecas necessárias
#include <Arduino.h>
#include "HX711.h"

// GPIO utilizada para conectar o amplificar HX711
const int LOADCELL_DOUT_PIN = 16;
const int LOADCELL_SCK_PIN = 4;

// Instância da biblioteca HX711
HX711 scale;

void setup()
{

  // Inicia monitor serial
  Serial.begin(115200);
  // Inicia celula de carga passando os GPIO antes definidos
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
}

void loop()
{

  if (scale.is_ready())
  {                    // Verifica a conexão com HX711
    scale.set_scale(); // Mede a escala
    Serial.println("Tare... remove any weights from the scale.");
    delay(10000);
    scale.tare(); // Realiza calibragem da balança
    Serial.println("Tare done...");
    Serial.print("Place a known weight on the scale...");
    delay(10000);
    long reading = scale.get_units(10);
    get_units // obtém a média do último número definido de leituras menos o peso da tara dividido pelo fator de calibração
        Serial.print("Result: ");
    Serial.println(reading);
  }
  else
  {
    Serial.println("HX711 not found.");
  }
  delay(1000);
}