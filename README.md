# XLtoy: 
The ultimate toolkit for Microsoft Excel modelers. 

### The name
*XLtoy* it's a word pun that starts from *xt to py* concept, but the *p* seem superfluous here and *xlto(p)y* became 
XLtoy, more funny.

### Description
XLtoy framework can read, parse, diff, validate, manage changes and run out of the box complicated models written 
using Microsoft Excel. All features will be developed in the dev plan below.
I found that is too difficult, and often useless, to analyze an entire workbook, so main idea, here, is to 
identify a subset of areas of interest and focalize only on these, so with minimum changes to an existent sheet, 
the parser can handle it and produce usefull information. If you can apply some simple 
[ rules](https://raw.githubusercontent.com/glaucouri/xltoy/main/rules.md)
you are ready to go!

This is an example of a tipical forecasting model that can be well handled by xltoy.
![xlsample](https://github.com/glaucouri/xltoy/raw/main/img/simple_model.png?raw=true)
Green cells contain actual (or hystorical) values, model is developed in salmon and 
dragged (in yellow). 

### Installation
Up to now, xltoy is available only on github repo, so after clone: 

> python setup.py

After that, all features are accessible via *xltoy* cli command.

```
> xltoy --help

Usage: xltoy [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  collect
  diff

```

## The framework
The XLtoy Framework is composed of many subpackages, all of them are reachable via cli sub command.

* **xltoy.collector** : It read an excel workbook and extract all needed information, following rules described here. 
This means equations, named or anonymous exogenous data and parameters. 
Result can be represented as hierarchical yaml or json. This functionality solve problem related 
to *change management*, *versioning*, *model governance* and *diff* operation.

* **xltoy.parser** : It can parse all collected equation in order to understand for each all the dependencies, 
and transliterate each in a readable and working python code.
All relations between formulas are stored in a dependency graph in a key:value structure 
using the mnemonic name for each equation. This data structure allow us to do a topological analysis of entire
system of equations

## Time line
The framework will be finished in some steps, i want to share the release plane because 
with the release of first version i will need feedback, use cases and tester.  

#### Version 0.1: first working version:
* it define [working rules](https://raw.githubusercontent.com/glaucouri/xltoy/main/rules.md)
* fully testes with py3.6 to py3.8
* collector can read data,formulas and can show an entire workbook as yaml or json.
* **diff** works with data and formulas too, it can compare 2 workbook or a representation of it yaml or json.

#### Version 0.2: parser feature:
* parser can understand excel formula (probably not all syntax)
* in memory graph representation with all relation between equations.
* can find all predecessors and successors of a given equation.
* models can be exported as graph or python code.

#### Version 0.3: executor feature:
* data can be stored as pandas DataFrame
* models can be executed on external data. Binding feature.

#### Version X: big data feature:
* model can be distributed on a spark cluster and executed in order to work on big data
