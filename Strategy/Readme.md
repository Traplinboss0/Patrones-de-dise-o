# Estrategy

## ¿Que es el patron Strategy?
estrategy permite definir una familia de algoritmos, colocar cada algoritmo en una clase separada y hasta incluso hacer objetos intercambiables.

Este patron sugiere tomar calses que hacen cosas especificas y extraerlos algoritmos para ubicarlos en clases separadas llamadas estrategias. 

## ¿Como se compone Strategy?
estrategy se compone de tres clases las cuales realizan funciones cada una diferente que hacen que el patron strategy funcione. 

**Clase Contexto:** Esta clase se encarga de matener una referencia a ña estrategias concretas ademas de comunicar el onjeto.

**Interfaz estrategia** Se encarga de declarar un metodo que la clase contexto utilizara para llevar a cabo una estrategia

**Cliente:** Esta clase se encarga de cear un objeto de estrategia especifico. La clase contexto expone un modificador set que permitira a los clientes sustituir su estrategia durante el tiempo de ejecucion. 

## estructura

![Alt text](https://refactoring.guru/images/patterns/diagrams/strategy/structure-indexed.png)