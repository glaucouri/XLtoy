## xltoy tutorial

#### case1: data diff [positional]

In this example, we compare 2 workbook with only 1 data range each one. 
Working area is set only on numeric cells, so we can only do positional difference,
in this case we have add a new line, row 12 and changed a cell in position M7.

<img src=https://github.com/glaucouri/xltoy/img/data_sample1.png>
<img src=https://github.com/glaucouri/xltoy/img/data_sample1_diff.png>

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
  xltoy:
    datetime: 2020-11-27T17:43:30.051900 -> 2020-11-27T17:43:30.068501
    filename: data/data_sample1.xlsx -> data/data_sample1_diff.xlsx

