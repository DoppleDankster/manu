# Les Types de bases (aka les scalaires): int, float, str, bool

## Affectation

1)  Créer une variable 
```python
un_int = 5
un_float = 1.5
une_string = "coucou"
un_bool = True  # ou False
```

2) Quand la conversion est possible, on peut faire nouveau_type(variable)

:warning: attention à la perte d'information

`un_float_en_int = int(un_float)`

3)pour afficher une variable on peut utiliser print()
`print(un_int)`

3') print() accepte un nombre infini de paramètres séparés par une virgule
`print(un_int, un_float, une_string)`



## les opération mathématiques appliquées aux différents types

1) somme de deux int comme en maths tradi
`a = 5 + 3` -> 8
2) somme de deux float comme en maths tradi
`b = 5.2 + 3.2` -> 8.4
3) somme d'un int et d'un float comme en maths tradi
`c = 5 + 3.2` -> 8.2
4) somme d'un int/float avec une string
 
:warning: attention, la string à un comportement spécial
la concaténation avec un int ne fonctionne pas et occasionne un type error
les deux types sont incompatibles

5) la concaténation de deux string par contre fonctionne et les "colles"
`d = "il fait" + " beau"` -> "il faut beau"

## Pour connaître la liste des fonctions supportées par un objet
`dir(<nom_de_l'object>)`

