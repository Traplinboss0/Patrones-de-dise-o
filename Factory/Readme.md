# Factory 

## ¿En que consiste el metodo Factory?
El metodo factory es un patron de diseño creacional que se encarga de resolver el problema de crear objetos sin especificar como tal sus clases concretas.

El patron factory se basa en un metodo que se emplea para crear objetos , en lugar de realizar un constructor, las subclases se encargan de sobrescribir el metodo para cambiar las clases de los objetos. 

![Alt text](https://miro.medium.com/max/720/1%2AIJyuZBehvK5V-CwB1ha_Xg.png)

Como podemos ver en el anterior ejemplo para instanciar un objeto similar a uno ya creado elaboramos un metodo fabrica que  nos devuelve objetos similares denominados productos. 

## ¿Como se compone Factory?
El patron de diseño factory se compone de diferentes clases y subclases los cuales nos ayudaran a la elaboracion de un constructor. 

Se compone de una clase constructora, metodos definiidos y otros abstractos dedicados a las contruccion de objetos que nos ayudaran con los subtipos de un tipo determinado 

## Estructura


![](https://sourcemaking.com/files/v2/content/patterns/Factory_Method.png)

