# Prototype 

## ¿Que es el Prototype?
El patron de diseño prototype tiene como proposito copiar onjetos ya existentes con la funcion de que el codigo no dependa de sus clases.

El patron prototype en su funcionamiento delegaa un pproceso de cloanacion a objetos propios que estan siendo clonados. El patron declara una interfa comun para todos los objetos que se pueden clonar, dicha interfaz nos permite clonar un objeto sin la necesidad de acoplar el codigo a la clase perteneciente de ese objeto. 

## ¿Como se compone Prototype?
Este patron de diseño dispone de tres clases fundamentales para su correcto funcionamiento dicahs clases son: 

**Prototipo:** Esta clase se encarga de declarar los metodos de clonacion, en la mayoria de estos casos se trata de un metodo conocido como clonar

***Prototipo concreto** Implementa el metodo de clonacion y se encarga de copiar informacion del objeto original, este metodo en algunas ocaciones gestiona algunos casos externos al proceso de clonacion 

**Cliente** Se encarga de producir una copia de cualquir objeto que continue con la interfaz del prototipo

## Estructura

![Alt text](https://refactoring.guru/images/patterns/diagrams/prototype/structure-indexed.png)
