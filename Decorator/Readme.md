# Decorator
## ¿Que es Decorator?
Decorator es un Patron de diseño estructural en cual permite añadir funcionalidades a objetos mediante encapsuladores que contienen funcionalidades 

### Se veria algo mas o menos así
![](https://refactoring.guru/images/patterns/content/decorator/decorator.png)

Cuando se tiene aque alterar la funcionalidad de un objeto es importante conocer la forma en la que se va a realizar puesto que existen diferentes formas de hacerlo, la manera mas efectiva de hacerlo es mediante la agregacion, de esta manera se puede sustituir un objeto vinculando a otro, esto se hace cabiando el comportamiento del contenedor durante su tiempo de ejecucion. 

El patron decorador funciana mediante la agragacion puesto que le preincipio de este se basa en un objeto el cual pueda vincularse a otro. 

## ¿Como se compone?
Command se compone de diferentes clases y interfaces para poder realizar los decoradores lo que compone este patron es: 

**El componente:** se encarga de declarar la interfaz para objetos.

**Componente Concreto:** se basa en una clase de objetos que definene el comportamiento basico, que los decoradores pueden alterar 

**Clase Decorador Base** Estaclase posee un campo para referenciar un objeto, el tipo de campo debe estar definido y declararse.

### Estructura del Patron Decorador
![](https://refactoring.guru/images/patterns/diagrams/decorator/example.png)



