# XLtoy: 
simply? the ultimate *excel to python* framework. 

## XLtoy: the name
*XLtoy* it's a word pun that starts from *xt to py* concept, but the *p* seem superfluous here and *xlto(p)y* became XLtoy, more funny.

## XLtoy: description
XLtoy framework can read, parse, diff, validate, manage changes and run out of the box complicated models written using Microsoft Excel. 
Main idea here to do minimum changes to an existent sheet to permit the parser to handle all data. 

## XLtoy: convention

## XLtoy: the framework
The XLtoy Framework is composed of many subpackages.

* **xltoy.collector** : It read a subset of an excel workbook and extract all needed information. This means equations, 
named or anonimous, relation between formulas and after that, 
all equations are stored in a dependency graph in a key:value structure using the mnemonic name for each equation.
Result can be rappresented as hierarchical yaml or json or using the graph itself. This functionality solve problem related 
to *change management*, *versioning* and *model governance* and *diff* operation.

* **xltoy.parser** : It can read and understand all collected equation in order to understand for each all the dependancies, 
and transliterate each in a readable and 

* **xltoy.orchestrator** : This create a graph that fully contain the collected equations.

* **xltoy.validator** :

* **xltoy.executor** :

## XLtoy: Time line