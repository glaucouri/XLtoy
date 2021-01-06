## xltoy tutorial

#### case1: data diff [positional absolute]

In this example, we compare 2 workbook with only 1 data range each one. 
Working area is set only on numeric cells, so we can do positional difference.
In second workbook we have add a new line, row 12 corresponding to VAR_9 
and changed a cell in position M7.

![xlsample](https://github.com/glaucouri/xltoy/raw/main/img/data_sample1.png?raw=true)
![xlsample](https://github.com/glaucouri/xltoy/raw/main/img/data_sample1_diff.png?raw=true)

```
(xltoy)$ xltoy diff data/data_sample1.xlsx data/data_sample1_diff.xlsx
add:
  D12: 0.0005004366657703548
  E12: 0.000547121974635698
  F12: 0.0005295198569146752
  G12: 0.0005072172479631228
  H12: 0.0005379024723558388
  I12: 0.0005430174783953075
  J12: 0.0005689182087171011
  K12: 0.0005538596087349697
  L12: 0.0005297508191981888
  M12: 0.0005409815166305603
  N12: 0.0005876844243079103
  O12: 0.0006204197757602877
  P12: 0.0006232399068120899
  Q12: 0.0007001965787723482
  R12: 0.0007432987416372932
  S12: 0.0007323677326847715
change:
  data_sample:
    M7: 905509 -> 905510
```

#### case2: data diff [positional relative]

First workbook is from case1
In second workbook range was moved to another position 

![xlsample](https://github.com/glaucouri/xltoy/raw/main/img/data_sample1_relative.png?raw=true)

```
(xltoy)$ xltoy diff data/data_sample1.xlsx  data/data_sample1_relative.xlsx  --relative

<no output>
```

So in relative mode, no difference found



#### case 3: huge data diff (>3M cells) 

This exercise was done using data from *https://data.world/* a free datasources provider.

[data source](https://tinyurl.com/ybhqd8g9)

It contains >3M cells.

**Procedure in 5 steps:** 
1. Download [Air_Quality_Measures_on_the_National_Environmental_Health_Tracking_Network.csv](https://query.data.world/s/aci46g2wmbpn5egnve7nj3aikoqw2m)
2. Set the **data working area** and save the file as *Air_Quality.xlsx*
3. Now this file was considered as the referrer file so we can store it in an 
   efficient representation using *xltoy collect*
4. Make some changes, add and remove cells are allowed too. and save this version as *Air_Quality2.xlsx*
5. Use *xltoy diff* to find differences.

in practice:

1. `wget https://query.data.world/s/aci46g2wmbpn5egnve7nj3aikoqw2m  -O Air_Quality.csv`
2. `(excel) <open with Excel and set data range>`
3. `xltoy collect Air_Quality.xlsx --data --json -vvv > Air_Quality.json`
   ![xlsample](https://github.com/glaucouri/xltoy/raw/main/img/data_collect.gif?raw=true)
   * --data, to exclude eventually formulas.
   * --json, we want output in JSON format.
   * -vvv (triple v) means log in higher verbosity:DEBUG.
   
   
4. `(excel) <Simulate some change in a new file>` 
5. `xltoy diff Air_Quality.json Air_Quality2.xlsx --timeit -vvv`
   ![xlsample](https://github.com/glaucouri/xltoy/raw/main/img/data_diff.gif?raw=true)
   * json Vs xlsx to see different parsing times.
   * --timeit, to print out the execution time.
   * -vvv (triple v) means log in higher verbosity:DEBUG.


at the point 4) I've changed 2 cells randomly and the result og point 5) was:

```
change:
  Air_Quality:
    H146162: Wood -> Iron
    N218636: 0 -> 1
```

It means, that *change* was found in sheet *Air_Quality*
two cells involved: *H146162* and *N218636*

It took:

- about 7 secs. to open file in Excel
- 35 sec. to do the snapshoot in json format
- 1.5 sec. to load json file
- diff costs less than 1sec.

