# Informe

### 1. ¿Cuál fue su diseño inicial? ¿Cuánto pesaba? ¿Cómo eran los factores de utilización y las deformaciones?

En primera instancia, debido a la condición que limita el largo de las barras en el vano del puente a solo 6 metros, se decidió crear barras de de `5 [m]` de longitud. Al ser el primer diseño, se utilizó una estructura similar a la de la entrega 4, pero esta no considero las barras diagonales en la base de la estructura.
El largo de todas las barras se consideró igual, por lo que la altura del puente en primera instancia fue de `H = 4,33 [m]` (Calculado con el teorema de Pitágoras). El espesor de las barras se fijó igual para todas y tuvo un valor inicial de  `t = 5 [mm]`.
A continuación se presenta la estructura del diseño 1, la cual tuvo un peso de `P = 283.837,4099 [N]`.

![Gráfica_1_Estructura](https://user-images.githubusercontent.com/43649125/96386665-fb993d80-1172-11eb-80f8-c6391159d7c5.PNG)

Posteriormente se calcularon las tensiones correspondientes para cada combinación y se graficaron las deformaciones de la estructura. Recordar que las barras fueron graficadas en tonalidades, siendo rojo compresión y azul traccion. Junto a lo anterior se revisó la viabilidad del diseño con la función `chequear_diseño`. El requisito para aprobar el diseño propuesto debía cumplir:

![CodeCogsEqn](https://user-images.githubusercontent.com/43649125/96386731-72363b00-1173-11eb-94fe-dce5133550ff.gif)

A continuación se presentan los resultados del diseño número 1:
 
#### Tensiones caso 1 Combinación 1

![Gráfica_1_Tensiones_caso_1 4D](https://user-images.githubusercontent.com/43649125/96386670-ffc55b00-1172-11eb-92d4-44ba34eae0b5.PNG)

#### Tensiones caso 1 Combinación 2

![Gráfica_1_Tensiones_caso_1 2D+1 6L](https://user-images.githubusercontent.com/43649125/96386669-ffc55b00-1172-11eb-901b-e82b571c391b.PNG)


| Caso | Radio `[cm]`: | Espesor `[mm]` | Altura `[m]` | Largo `[m]` |
|--|--|--|--|--|
| 1 | 8 | 5 | 4,33 | 5 |
| 2 | 15 | 25 | 4,33 | 5 |
| 3 | 15 | 25 | 10 | 5 |
| 4 | 20 | 40 | 20 | 5 |
| 5 | 20 | 40 | 10 | 5,972 |
