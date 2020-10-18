# Informe

### 1. ¿Cuál fue su diseño inicial? ¿Cuánto pesaba? ¿Cómo eran los factores de utilización y las deformaciones?

En primera instancia, debido a la condición que limita el largo de las barras en el vano del puente a solo 6 metros, se decidió crear barras de de `5 [m]` de longitud. Al ser el primer diseño, se utilizó una estructura similar a la de la entrega 4, pero esta no considero las barras diagonales en la base de la estructura.
El largo de todas las barras se consideró igual, por lo que la altura del puente en primera instancia fue de `H= 4,33 [m]` (Calculado con el teorema de Pitágoras). El espesor de las barras se fijó igual para todas y tuvo un valor inicial de  `t= 5 [mm]`.

A continuación se presenta la estructura del diseño 1, la cual tuvo un peso de `P= 283.837,4099 [N]`.

![Gráfica_1_Estructura](https://user-images.githubusercontent.com/43649125/96386665-fb993d80-1172-11eb-80f8-c6391159d7c5.PNG)

Posteriormente se calcularon las tensiones correspondientes para cada combinación y se graficaron las deformaciones de la estructura. Recordar que las barras fueron graficadas en tonalidades, siendo rojo compresión y azul traccion. Junto a lo anterior se revisó la viabilidad del diseño con la función `chequear_diseño`. El requisito para aprobar el diseño propuesto debía cumplir:

![CodeCogsEqn](https://user-images.githubusercontent.com/43649125/96386731-72363b00-1173-11eb-94fe-dce5133550ff.gif)

A continuación se presentan los resultados del diseño número 1: 

![Gráfica_1_Tensiones_caso_1 4D](https://user-images.githubusercontent.com/43649125/96386670-ffc55b00-1172-11eb-92d4-44ba34eae0b5.PNG)

![Gráfica_1_Tensiones_caso_1 2D+1 6L](https://user-images.githubusercontent.com/43649125/96386669-ffc55b00-1172-11eb-901b-e82b571c391b.PNG)

Se observa que el primer diseño realizado no cumple con los requisitos mínimos de diseño. Este, al no ser un diseño viable, no permitio poder obtener sus factores de utilización correspondientes.
En un intento por corregir esto, se generó distintos casos en los que se vario uno o mas parametros de la estructura original. Para poder analizar los acmbios que generaban en ella
 
A continuación se presenta una tabla con la variacion de parametros en cada caso:

| Caso | Radio `[cm]`: | Espesor `[mm]` | Altura `[m]` | Largo `[m]` |
|--|--|--|--|--|
| 1 | 8 | 5 | 4,33 | 5 |
| 2 | 15 | 25 | 4,33 | 5 |
| 3 | 15 | 25 | 10 | 5 |
| 4 | 20 | 40 | 20 | 5 |
| 5 | 20 | 40 | 20 | 5,972 |

### Caso 2
Para este caso se aumentó el radio de la barra  a `15 [cm]` y su espesor a `25 [mm]`.

![Gráfica_2_Estructura](https://user-images.githubusercontent.com/43649125/96387003-94c95380-1175-11eb-82df-8d859a3645b9.PNG)

![Gráfica_2_Tensiones_caso_1 4D](https://user-images.githubusercontent.com/43649125/96387002-9430bd00-1175-11eb-93de-93ad1e124711.PNG)

![Gráfica_2_Tensiones_caso_1 2D+1 6L](https://user-images.githubusercontent.com/43649125/96387001-93982680-1175-11eb-8a51-b60c0875d3ab.PNG)


### Caso 3
Para este caso se aumentó la altura de la estructura a `10 [m]`.

![Gráfica_3_Estructura](https://user-images.githubusercontent.com/43649125/96387058-d823c200-1175-11eb-9255-b3168aaff6f5.PNG)

![Gráfica_3_Tensiones_caso_1 4D](https://user-images.githubusercontent.com/43649125/96387057-d823c200-1175-11eb-9324-53879f80e430.PNG)

![Gráfica_3_Tensiones_caso_1 2D+1 6L](https://user-images.githubusercontent.com/43649125/96387054-d78b2b80-1175-11eb-8a3b-a84ad41c9735.PNG)


### Caso 4
Para este caso se aumentó el radio de la barra  a `20 [cm]`, su espesor a `40 [mm]` y su altura a `20 [m]`.

![Gráfica_4_Estructura](https://user-images.githubusercontent.com/43649125/96387060-e40f8400-1175-11eb-8cd6-145901c7874f.PNG)

![Gráfica_4_Tensiones_caso_1 4D](https://user-images.githubusercontent.com/43649125/96387062-e540b100-1175-11eb-96f4-8f086f02a4a3.PNG)

![Gráfica_4_Tensiones_caso_1 2D+1 6L](https://user-images.githubusercontent.com/43649125/96387061-e4a81a80-1175-11eb-9b75-7f18e9f19e94.PNG)

#### Caso 5
Para este caso se mantuvieron los parámetros iguales que para el caso 4. Sin embargo, el largo de la barra se re calculo dividiendo el largo del puente por 36 (número de barras). El resultado a pesar de ser decimal (y por ende, no realista con las medidas existentes en el mercado) no cumplio con los requisitos. Por lo que no hubo que ajustar su valor a las solicitudes de la industria. 

![Gráfica_5_Estructura](https://user-images.githubusercontent.com/43649125/96387288-50d74e00-1177-11eb-8700-1e73d930bd1d.PNG)

![Gráfica_5_Tensiones_caso_1 4D](https://user-images.githubusercontent.com/43649125/96387290-52087b00-1177-11eb-8a89-251b23377653.PNG)

![Gráfica_5_Tensiones_caso_1 2D+1 6L](https://user-images.githubusercontent.com/43649125/96387289-52087b00-1177-11eb-90ab-65a575f8bab5.PNG)

