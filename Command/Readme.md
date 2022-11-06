# Command

# ¿Que es Command?
Command es un patron de diseño el cual se basa en el principio de separa responsabilidades. Divide la aplicacion en capas entre la interfaz grafica de usuario y otra capa logica, POr ejemplo: La interfaz grafica de usuario se encargara de mostrar una bonita imagen al usuairo mientras que la capa logica se encargara del trabajo detras de todo esto.

![](https://refactoring.guru/images/patterns/diagrams/command/solution1-es.png)

El patrón Command sugiere que los objetos GUI no envíen estas solicitudes directamente. En lugar de ello, debes extraer todos los detalles de la solicitud, como el objeto que está siendo invocado, el nombre del método y la lista de argumentos, y ponerlos dentro de una clase comando separada con un único método que activa esta solicitud.

# ¿Como se compone?
El patron Command se compone de diferentes clases las cuales cada una tiene funciones diferentes, las clases son: 

**Clase Emisora:** Es responsable de inicializar todas las solicitudes esta clase generalmente tiene  un campo para almacenar referencias de objetos

**Interfaz Comando:** generalmente declara un metodo para la ejecucion de un comando 

**Comando Concretos:** Son comandos que implementan diferente tipos de solicitudes, debe contener la instrucciones para ejectar un metodo en un objeto receptor

**Clase Receptora:** Esta clase contiene una parte de la logica de negocio, casi cualquier objeto que actue como receptor. 

### Así es la estructura de Command

![](https://refactoring.guru/images/patterns/diagrams/command/example.png)




