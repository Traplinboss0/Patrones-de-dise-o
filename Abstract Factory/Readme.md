# Abstract factory

## ¿Que es Abstract factory?
 Abstract factory(fabrica abstracta) es un patron de diseño que permite producir unas familias de objetos relacionados sin la necesidad de especificar sus clases concretas.

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution2.png?id%3D53975d6e4714c6f942633a879f7ac571)

En el anterior esquema podemos ver como es una fabrica abstracta en un diagrama de modelado UML , este ejemplo se baso en una interfaz de sillas y mesas las cuales se dividian en diferentes fabricas dependiendo de su forma. 

## ¿como se compone?
Lo primero que se debe hacer a la hora de realizar este patron de diseño es declara de forma explicita interfaces para cada producto que se encuentre y que pertenezca a diferentes familias,despues de esto se realizan todas la variantes de los productos. Para ello disponemos de:

**Productos Abstractos:** declaran interfaces para un grupo de productos diferentes pero relacionados que forman una familia de productos.

**Productos Concretos:** on implementaciones distintas de productos abstractos agrupados por variantes.

**Fábrica Abstracta:** declara un grupo de métodos para crear cada uno de los productos abstractos.

**Fábricas Concretas:** implementan métodos de creación de la fábrica abstracta. Cada fábrica concreta se corresponde con una variante específica de los productos y crea tan solo dichas variantes de los productos.

### Así se ve la estructura de Abstract factory

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure-indexed.png?id%3D6ae1c99cbd90cf58753c633624fb1a04)

