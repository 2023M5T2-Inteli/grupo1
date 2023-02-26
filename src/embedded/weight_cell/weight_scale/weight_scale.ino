
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

  Serial.begin(115200); // Inicia monitor serial
  Serial.println("Inicializando a balança");

  // Inicia celula de carga passando os GPIO definidos
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);

  Serial.println("Configurando a balança");
  Serial.print("read: ");
  Serial.println(scale.read()); // Leitura bruta do sensor

  Serial.print("read average: ");
  Serial.println(scale.read_average(20)); // média do último número definido de leituras

  Serial.print("get value: ");
  Serial.println(scale.get_value(5)); // média do último número de definido de leitura menos a tara

  scale.set_scale(-1840); // número de calibração que deve ser obtido antes de passar o código

  Serial.print("get units: ");
  Serial.println(scale.get_units(5)); // média do último número definido de leituras menos o peso da tara dividido pelo fator de calibração

  scale.tare(); // faz a calibração da tara
}

void loop()
{
  Serial.print(" Leitura: ");
  Serial.println(scale.get_units()); // Mostra resultado obtido
  // Irá desligar e ligar o ADC para que novos resultados sejam mostrados a cada 5 segundos
  scale.power_down();
  delay(5000);
  scale.power_up();
}