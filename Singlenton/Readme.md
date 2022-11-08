# Singleton

## ¿Que es singleton?
Singleton es un patron de diseño que tiene como proposito permitir asegurar que cada calse tenga una unica instancia ademas de proporcinar un punto de acceso global a dicha instancia. 

La mayoria de implementaciones de este patron tienen pasos que se deben segui, entre estos podemos encontrar que debemos hacer privado el constructor por defecto para evitar la iteracion con otros objetos que utilien el operador. En el segundo paso temenos que crear un metodo de creacion estatico que va actuar como constructor.

## ¿Como se compone singleton?
SIngleton se compone de una unica calse para poderse llevar a cabo en esta caso la clase se denomin singleton.

**Clase Singleton:** Esta es la unica clase del patron y se encarga de declarar un metodo estatico que devolvera una instacia de la propia clase. El constructor de singletn debe estar oculto del codigo del cliente. 

## Estructura

![Alt text](https://refactoring.guru/images/patterns/diagrams/singleton/structure-es-indexed.png)

