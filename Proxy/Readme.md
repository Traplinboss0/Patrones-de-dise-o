# Proxy

## ¿Que es proxy?
El patron de diseño proxy tiene como proposito proporcionar un marcador o sustituto de posicion para otro objeto, este patron de diseño controla el acceso al objeto original. 

El patrn proxy suguiere crear una clase proxy que se encargue de actualizar y calalizar todas las peticiones de los clientes para concretar el servico y realizar todo el trabajo. 

![Alt text](https://refactoring.guru/images/patterns/diagrams/proxy/solution-es.png)


## ¿Como se compone el patron proxy?
el patron de diseño proxy consta de cuatro clases para poder funcionar. 

**Interfaz de Servicio:** Esta calse se encarga de declarar la nterfaz del servicio, el proxy debe seguir dicha interfaz para poder esconderse como objeto del servicio 

**Servicio:** Es una clase que proporciona logica de negodcio aplicable a la vez que util 

**Proxy:** Se basa en el capo de referencia que apunta a un objeto como un servicio, funciona cuando el proxy finaliza su procesamiento y pasa la solicitud al objeto de servicio.

**Cliente:** funciona con servicios y los proxies en la misma interfaz, se encarga de pasar un proxy a cualquier parte que espere un servicio 

# Estructura 

![Alt text](https://refactoring.guru/images/patterns/diagrams/proxy/structure-indexed.png)

