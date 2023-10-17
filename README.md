# Transpetro_YOLO
Repositório criado para armazenar os datasets utilizados além dos arquivos necessários para rodar o YOLO para o projeto em desenvolvimento para a empresa Transpetro.

## Resultados
A partir do dataset presente, utilizou-se YOLOv7. Os resultados obtidos foram:
|                  Name                 |   Train Size  |    Val Size    |   Precision   |    Recall     |      mAP      |
|  -----------------------------------  | ------------- | -------------- | ------------- | ------------- | ------------- |
|           POLI_2023/1st_test          |      192      |        53      |     45,1%     |     38,7%     |     35,3%     |
|           POLI_2023/2nd_test          |      346      |        86      |     85,0%     |     86,0%     |     **90,1%**     |
|        Guararema_05_06_23/1st_test    |      457      |       130      |     29,5%     |     43,6%     |     32,6%     |
|     Guararema_05_06_23/2nd_test/60m   |       45      |        13      |      9,6%     |      4,5%     |      1,4%     |
|     Guararema_05_06_23/2nd_test/70m   |      109      |        31      |     91,6%     |     45,5%     |     55,7%     |
|     Guararema_05_06_23/2nd_test/80m   |       38      |        11      |      3,5%     |      3,9%     |      3,7%     |
|     Guararema_05_06_23/2nd_test/90m   |       34      |         9      |      1,2%     |      2,5%     |      9,7%     |
|    Guararema_05_06_23/2nd_test/100m+  |      208      |        59      |     56,4%     |      0,1%     |      2,8%     |
|     Guararema_05_06_23/3rd_test/60m   |       85      |        24      |     83,7%     |     37,5%     |     43,3%     |
|     Guararema_05_06_23/3rd_test/70m   |      126      |        36      |     52,4%     |     38,3%     |     31,5%     |
|     Guararema_05_06_23/3rd_test/80m   |       70      |        20      |     90,5%     |     55,6%     |     59,4%     |
|     Guararema_05_06_23/3rd_test/90m   |       73      |        21      |     85,7%     |     38,9%     |     47,0%     |
|    Guararema_05_06_23/3rd_test/100m+  |      221      |        63      |     38,5%     |      4,4%     |      1,5%     |
|    Guararema_05_06_23/3rd_test/Geral  |      662      |       189      |     86,7%     |     80,9%     |     **85,6%**     |
|     Guararema_e_Arthur/1st_test/60m   |     1127      |       322      |     92,5%     |     13,3%     |     15,5%     |
|     Guararema_e_Arthur/1st_test/70m   |     1317      |       376      |     36,6%     |      8,5%     |      8,2%     |
|     Guararema_e_Arthur/1st_test/80m   |       77      |        22      |     91,5%     |       53%     |     59,4%     |
|     Guararema_e_Arthur/1st_test/90m   |       77      |        22      |     74,8%     |     31,3%     |       34%     |
|    Guararema_e_Arthur/1st_test/100m+  |      403      |       115      |     54,4%     |      4,2%     |      2,4%     |
|    Guararema_e_Arthur/1st_test/Geral  |     3002      |       857      |     38,4%     |       16%     |       14%     |
|    Guararema_e_Arthur/2nd_test/60m    |      396      |       113      |     93,2%     |     37,7%     |     43,1%     |
|    Guararema_e_Arthur/2nd_test/70m    |      225      |        64      |     78,2%     |     28,3%     |     23,2%     |
|   Guararema_e_Arthur/2nd_test/Geral   |      621      |       177      |      0,9%     |     14,8%     |     19,3%     |
|     Guararema_e_Arthur/3rd_test/60m   |      909      |       260      |     56,6%     |     45,4%     |     49,8%     |
|     Guararema_e_Arthur/3rd_test/70m   |     1271      |       363      |     93,5%     |     12,6%     |     18,2%     |
|     Guararema_e_Arthur/3rd_test/80m   |       62      |        17      |       96%     |     43,2%     |     46,7%     |
|     Guararema_e_Arthur/3rd_test/90m   |       56      |        16      |     90,8%     |     40,1%     |     43,6%     |
|    Guararema_e_Arthur/3rd_test/100m+  |      153      |        43      |     %     |      %     |      %     |
|    Guararema_e_Arthur/3rd_test/Geral  |     2452      |       700      |     29,3%     |       35%     |     27,6%     |
|    Guararema_e_Arthur/4th_test/60m    |      381      |       109      |     91,8%     |       51%     |     57,5%     |
|    Guararema_e_Arthur/4th_test/70m    |      225      |        64      |     %     |     %     |     %     |
|   Guararema_e_Arthur/4th_test/Geral   |      606      |       173      |      %     |     %     |     %     |

## Folders
* [POLI_2023/1st_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/POLI_2023/1st_test) possui o dataset e resultado do experimento feito com algumas imagens coletadas em 1 dia de vôo pelo campus da USP de São Paulo, na região do Butantã. Somente foi anotado carros.

* [POLI_2023/2nd_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/POLI_2023/2nd_test) possui o dataset e resultado do experimento feito com todas imagens coletadas em 1 dia de vôo pelo campus da USP de São Paulo, na região do Butantã. Somente foi anotado os carros das imagens coletadas.

* [Guararema_05_06_23/1st_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/Guararema_05_06_23/1st_test) possui o dataset e resultado do experimento feito com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa em diversas altitudes, de 60m a 120m. A partir dess*, os dados coletados foram anotados utilizando 4 labels diferentes: pessoas, carros, caminhões e motocicletas.

* [Guararema_05_06_23/2nd_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/Guararema_05_06_23/2nd_test) possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros.

* [Guararema_05_06_23/3rd_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/Guararema_05_06_23/3rd_test) possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa, e da região do Rio das Ostras (RJ). Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros.

* [Guararema_e_Arthur/1st_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/Guararema_e_Arthur/1st_test) possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa, da região do Rio das Ostras (RJ) e algumas imagens capturadas em Arthur Nogueira. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros. Com esse último conjunto de dados, a quantidade de imagens de 60m e 70m aumentou mais de 13x. A quantidade de dados gerados a mais para altitudes maiores de 70m não é tão significante. É importante comentar também que, a partir desses dados, existe também a classificação de animais em algumas imagens, totalizando 5 objetos diferentes.

* [Guararema_e_Arthur/2nd_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/Guararema_e_Arthur/2nd_test) possui o dataset e resultado dos experimentos feitos com algumas imagens capturadas em Arthur Nogueira. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros e 70 metros. É importante comentar também que, a partir desses dados, existe também a classificação de animais em algumas imagens, totalizando 5 objetos diferentes (pessoas, carros, caminhões, motocicletas e animais). O dataset desse teste possui uma colorização das imagens térmicas, deixando os pontos mais quentes com tons mais fortes de vermelho.

* [Guararema_e_Arthur/3rd_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/Guararema_e_Arthur/3rd_test) possui o dataset e resultado dos experimentos feitos com algumas imagens capturadas em 1 dia de vôo pela região de Guararema, perto da região da empresa e em Arthur Nogueira. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros e 70 metros. É importante comentar também que, a partir desses dados, existe também a classificação de animais em algumas imagens, totalizando 5 objetos diferentes (pessoas, carros, caminhões, motocicletas e animais). Como os resultados do teste anterior foram bem abaixo do esperado, realizou-se uma nova anotação dos dados de Arthur Nogueira, deixando de anotar alguns frames que possuíam objetos cortados ou frames muito tremidos.

* [Guararema_e_Arthur/4th_test](https://github.com/GabrielaVidal7/transpetro_YOLO/tree/main/Guararema_e_Arthur/4th_test) possui o dataset e resultado dos experimentos feitos com algumas imagens capturadas em Arthur Nogueira. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros e 70 metros. É importante comentar também que, a partir desses dados, existe também a classificação de animais em algumas imagens, totalizando 5 objetos diferentes (pessoas, carros, caminhões, motocicletas e animais). O dataset desse teste possui uma colorização das imagens térmicas, deixando os pontos mais quentes com tons mais fortes de vermelho. Como os resultados do teste anterior foram bem abaixo do esperado, realizou-se uma nova anotação dos dados de Arthur Nogueira, deixando de anotar alguns frames que possuíam objetos cortados ou frames muito tremidos.