# Server

En este apartado se encontrará la funcionalidad del servidor

## Funcionamiento del servidor

El servidor se encargará de cargar cada vez que reciba una conexión, el archivo de datos actual, el cual contendrá los datos actuales con un ID, este será usado como un objeto, el cual contendrá datos el cual serán enviados con el objetivo de poder desempeñar un objetivo más ordenado.

## Datos del payload

- **code**: Representará un código de tarea, este código va a representar a la tarea, si la tarea actual no ha sido ejecutada por el cliente, se va a ejecutar _reps_ cantidad de veces.
- **reps**: Indicará la cantidad de veces que se va a ejecutar una tarea.
- **executor**: Un objeto que va a indicar qué es lo que se quiere que se ejecute, el cliente se encargará de ejecutarlo a su manera.

## Datos del executor

- **name**: Indica el nombre del ejecutor
- **code**: Indica el código del ejecutor
- **execution**: Indica los datos a ser ejecutados
- **description**: Establece un resumen **OPCIONAL** de la ejecución
- **postdata**: Establece parámetros adicionales en formato JSON
