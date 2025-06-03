#include "magnetometer.h"

  MagnetometerSensor::MagnetometerSensor() : mag(12345) {
  }
  bool MagnetometerSensor:: init(){
   if(!mag.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
     return false;
  }
    return true;
  }
float MagnetometerSensor::getX(){
    sensors_event_t event; 
    mag.getEvent(&event);
    return event.magnetic.x;
  }  
float MagnetometerSensor::getY(){
    sensors_event_t event; 
    mag.getEvent(&event);
    return event.magnetic.y;
  }  
float MagnetometerSensor::getZ(){
    sensors_event_t event; 
    mag.getEvent(&event);
    return event.magnetic.z;
  }
  float MagnetometerSensor::readAngle(){
    sensors_event_t event; mag.getEvent(&event);
    float declinationAngle = 0.0;
    float heading = atan2(event.magnetic.y, event.magnetic.x);
    heading += declinationAngle;
    if(heading < 0){
       heading += 2*PI;}
    if(heading > 2*PI){
       heading -= 2*PI;}
    float headingDegrees = heading * 180/M_PI; 
    return headingDegrees;
    }



 