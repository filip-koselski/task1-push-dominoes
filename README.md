# Task 1

Domino cubes are represented in the form of string, which consists of the following characters:

* | - the domino cube stands unaffected
* R - the domino cube falls to the right side
* L - the domino cube falls over to the left side


The task is to write an algorithm that determines a new literal containing the above characters after X iterations, during which changes in neighboring cubes occur X is an input parameter. For example, for the input string:

```||RR||L||RL|```

Applying 1 iteration of the algorithm should produce a result:

```||RRRLL||RL|```

Additionally:

The task is to write backward algorithm showing what the string of domino cubes looked like before applying X iterations of the algorithm from the first part of the task. For example, for the input string:

```||RRRRLLL|RRRR|```
Zastosowanie 2 iteracji algorytmu wstecznego powinno dać wynik:

```||RR||||L|RR|||```


```task1.py``` contains solution of the task and can be run with following parameters: ```python task1.py input_string mode X``` where:
* ```input_string``` - a domino chain of the string type containing at least 2 domino cubes (exemplary chain: ```'||RR||L||RL|'```)
* ```mode``` - ```'f'``` - forward iteration or ```'b'``` - backward iteration over chain
* ```X``` - number of iterations over chain > 0
* ```-h``` - help (optional argument)
