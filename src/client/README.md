# Cliente

Acá habrá el apartado del cliente, donde el dispositivo que lo contenga va a realizar una consulta cada 5 segundos al servidor principal.

# Cuenta con las siguientes herramientas:

- Updater: Un sistema que se encargará que el sistema SIEMPRE esté actualizado.

# El archivo de config

Este es un archivo que se usará para establecer la última tarea establecida para el cliente.

**Keys**:

- init: Una lista con tareas que se van a ejecutar apenas el cliente sea ejecutado
- last_update: Este contará con el código de la tarea última tarea que se ha realizado.
- pending: Una lista de tareas pendientes.
- dev: Un dato booleano que indica si está en modo developer o no (evitar actualizaciones innecesarias)
- code: Un código único creado para identificar a la maquina
