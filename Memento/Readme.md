# Memento 

## ¿Que es el patron de diseño memento?
Memento es un patron de diseño el cual busca guardar y restaurar el estado previo de un objeto, esto con el fin de que no revele los detalles de su implementacion. 

Memento funciona se encarga de delagar instancias de objetos para que otros objetos distintos intenten copiar el estadio del objeto original. El patron sugiere almacenar una copia del estado del objeto en un objeto espacial el cual se denomina memento. Los  contenidos que poseemos en el memento nos son accesibles para nigun objeto que no sea el propirtario. 

![Alt text](https://refactoring.guru/images/patterns/diagrams/memento/problem1-es.png?id%3Da68a8b5d7acbd2851ac4a2475f7705c2)

## ¿Como esta Compuesto Memento?
memento se compone de una clase originadora, el memento y la clase cuidadora, cada uno realiza una funcion propia dentro del patron de diseño. 

**Clase originadora** Esta calse puede producir instancias asi como restaurar su estado con la ayuda de instancias.

**Memento** Es el onjeto que actua como instancia del estado el cual lo origino.

**Cuidadora** Se encarga de actuar cuando la clase originadora lo exija y restaura el estado. 


## Estructura
![Alt text](https://refactoring.guru/images/patterns/diagrams/memento/structure1-indexed.png?id%3Df79a8356b087ae6b004aec42b787ae2e)