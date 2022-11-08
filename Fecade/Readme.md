# Fecade

## ¿Que es Fecade?
Fecade es un patron de diseño que se encarga  de estructurar un entorno con el propocito de reducir la complejida, esto lo logra con la division de subsistemas, minimizando las comunicaciones y dependencias. 

Para poder integrar este patron de diseño se requiere de un pateron facahda cuando se necesite proporcionar una interfaz simple a un subsistema complejo. LAs fachadas son un punto de entrada a cada nivel fomentando un escenario para su aplicaion. 

## ¿Como se compone factory?
El patron de diseño fecade esta compuesto por una clase principal la cual se conoce como fachada y una o varias clases secundarias las cuales pueden ser modulos que implementan una funcionalidad,de esta manera la clase principal(Fecade) se encarga de reconocer que calse de subsistemas son responsables de determinadas peticiones, y a su vez delega y y cumple con objetos del subsistema. LAs subclases se encargan de implementar una funcionalidad del subsistema, a su vez que realizan el trabjo solicitado por la fachada. 

## Estructura

![Alt text](https://commons.wikimedia.org/wiki/File%3AFacade_UML_class_diagram.svg)

