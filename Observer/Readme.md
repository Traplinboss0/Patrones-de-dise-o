# Observer

## ¿Que es el patron Observer?
Este patron de diseño que permite dinfinir un mecanismo para notificar a varios objetos sobre cualquier movimiento o evento que suceda con el objeto que esta en observacion. 

El patron observer se debe implementar como un mecanismo de suscripcion, puesto que esta es su funcion, manrtener objetos informados de los estados que se realizan con el objeto observado. 

## ¿Como se comnpone?
 El patron esta compueto por diferentes clases cada una con una funcion especifica, en este caso abarcaremos cada una de las clase para determinar las funciones que tienen. 

 **El Notificador:** Esta clase se encarga de enviar eventos de interes a otros objeto, dichos eventos suceden cuando el objeto observado cambia su estado o ejecuta algunos comportamientos.

 **Interfasz Suscriptora:** Esta se encarga de declarar la interfaz de notificacion, en la mayor parte de los casos consiste en un metodo conocido como actializar, el metodo tiene varios valores quepermiten al notificador pasar detalles de eventos.

 **Cliente** Esta clase se encarga de crear objetos ya sean tipo notificador o tipo suscriptor, despues registra a los suscriptores para actualizaciones al notificador.

 ## Estructura

 ![Alt text](https://refactoring.guru/images/patterns/diagrams/observer/structure-indexed.png)
 
