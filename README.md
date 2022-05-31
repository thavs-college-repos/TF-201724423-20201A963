# TF-U201724423
Complejidad Algorítmica | Trabajo Final

## Enunciado
Construir nuestro propio “Waze”, es decir un sistema que nos permita encontrar la ruta más
corta entre 2 puntos en una ciudad. La ciudad estará representada por un grafo previamente 
construido que representa una ciudad o una porción o distritos de una ciudad grande como Lima.


El conjunto de datos que se trabajará representa una sección equivalente a 1500 cuadras, más o 
menos como se muestra en la sección a continuación.

Los datos a trabajar se adjuntan en los siguientes archivos:
Lima-calles.csv Este archivo contiene por fila la información de cada calle de la ciudad de Lima con 
los siguientes tres datos: 
* ID de la calle
* El nombre de la calle 
* La cantidad de intersecciones que contiene esa calle

Lima-intersecciones.csv Este archivo contiene información de cada intersección por calle. 
Contempla los siguientes datos:
* ID del registro, 
* ID de la calle, 
* IDs de origen y destino de la intersección, 
* el origen y destino de la intersección, 
* La distancia en Km, 
* La velocidad en Km/h, 
* el costo, 
* el costo inverso 
* las coordenadas de la intersección.


## Especificación del Trabajo Final
El trabajo final evalúa outcome específico del curso: “Responsabilidad y ética profesional”, por lo 
que los estudiantes deberán evidenciar su competencia en dicho outcome, para ello se le 
proporciona de manera detallada los ítems que deberá cumplir, organizados en hitos semanales.
Se evalúa la capacidad de uso de herramientas para la planificación del trabajo, gestión del avance, 
versión de código fuente, manejo de documentación, para esto se utilizará GitHub.
### Hito 0:
* Realizar un grafo a partir de una lista de adyacencia construida con los datos procedentes del 
conjunto de datos contenidos en los archivos: Lima-calles.csv y Lima-intersecciones.csv.
Conseguido el Hito 0, con el grafo obtenido, se deberá completar el sistema de búsqueda de rutas, 
para ello, es necesario agregar la siguiente información al grafo de la ciudad generada:
* Latitud y Longitud de cada intersección.
* Peso de cada arista, la cual estará en función de la longitud (calculada en función a la latitud 
y longitud aproximada), y un factor de tráfico.
* El factor de tráfico será un factor que cambiará según la hora del día, por lo que se
debe incluir la posibilidad de configurar la hora del día. Por ejemplo, si la hora es 11:00
am, el tráfico en ciertas calles será bajo, por lo que el peso de las aristas 
correspondientes, será un valor pequeño también. Mientras que si son las 7:00 pm, el 
tráfico en dichas calles será alto, por lo que el peso de las aristas, será alto. Queda a
criterio de cada grupo cómo se diseña e implementa dicho factor de tráfico.
