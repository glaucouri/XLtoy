## XLtoy tutorial 2:  collect formula, labels  
Here are some examples useful to understand use cases. All used files are 
available in this repository.  


#### collect formula from a simple model: Hybrid model
In the Sheet1 model range is set as *=Sheet1!D15:G15* 
so in this model we handle only 4 column, in the header,
range *=Sheet1!D13:G13* are set the labels respectively 
S, rf, VS, Vrf.
```
(xltoy)$ xltoy collect data/upload_HybridModel.xlsx --yaml
Sheet1:
  S: =D14+D14*(E15 -$E$10)*$D$6 + D14*$E$9*F14*SQRT($D$6)
  VS: =$E$11
  Vrf: =$E$11
  rf: =E14+$E$6*($E$7-E14)*$D$6+$E$8*G14*SQRT($D$6)
```


#### collect formula on anonymous model
This is an example of a common forecasting model that can be well handled by XLtoy.
![xlsample](https://github.com/glaucouri/xltoy/raw/main/img/simple_model.png?raw=true)
Green cells contain actual (or hystorical) values, model in salmon for the first calculated step,
and in yellow dragged cells, the rest of the model. As you can see in the outcome, 
no labels are provided in the input so the collector assign to each formula a label anon_1,2,3,..,n

```
(xltoy)$ xltoy collect data/anon_sheet.xlsx --yaml
WAR Found anonymous model Sheet1 : 11 anon labels assigned
Sheet1:
  anon_1: =(E3+D3)/2
  anon_10: =LOG(F11)
  anon_11: =LOG($F$11)
  anon_2: =(E4+D4)/2
  anon_3: =(E5+D5)/2
  anon_4: =(E6+D6)/2
  anon_5: =IF(D7,D7+E7,D7-E7)
  anon_6: =RAND()
  anon_7: =E9*0.023
  anon_8: =8
  anon_9: =12
```