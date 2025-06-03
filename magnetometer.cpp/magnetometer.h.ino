#ifndef MAGNETOMETER_H
#define MAGNETOMETER_H

#include <Adafruit_HMC5883_U.h>  
#include <Wire.h>
#include <Adafruit_Sensor.h>

class MagnetometerSensor {
  public:
    MagnetometerSensor();              
    bool init();
    float readAngle();  
    float getX();        
    float getY();        
    float getZ();        
  private:
    Adafruit_HMC5883_Unified mag;
};
#endif