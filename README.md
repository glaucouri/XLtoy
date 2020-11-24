# XLtoy: 
The ultimate *excel to python* framework. 

### The name
*XLtoy* it's a word pun that starts from *xt to py* concept, but the *p* seem superfluous here and *xlto(p)y* became XLtoy, more funny.

### Description
XLtoy framework can read, parse, diff, validate, manage changes and run out of the box complicated models written using Microsoft Excel. 
Main idea here to do identify a subset of interesting cells and focalize only on these, so 
with minimum changes to an existent sheet, the parser can handle all involved data.

![xlsample](https://github.com/glaucouri/xltoy/raw/main/img/simple_model.png?raw=true)


### Installation
Up to now xltoy is available only on github repo, so after clone: 

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
The XLtoy Framework is composed of many subpackages, all of them are reachable via cli subcommands.

* **xltoy.collector** : It read a subset of an excel workbook and extract all needed information. This means equations, 
named or anonimous, relation between formulas and after that, 
all equations are stored in a dependency graph in a key:value structure using the mnemonic name for each equation.
Result can be rappresented as hierarchical yaml or json or using the graph itself. This functionality solve problem related 
to *change management*, *versioning* and *model governance* and *diff* operation.

* **xltoy.parser** : It can parse all collected equation in order to understand for each all the dependancies, 
and transliterate each in a readable and working python code. 

## Time line
The framework will be finished in some steps, i want to share the release plane because 
starting with first release i will need feedback, use cases and tester.  

#### Version 0.1: first working version:
* it define working rules
* fully testes with py3.6 to py3.8
* collector can read data,formulas and can show an entire workbook as yaml or json.
* **diff** works with data and formulas too, it can compare 2 workbook or a representation of it yaml or json.  
