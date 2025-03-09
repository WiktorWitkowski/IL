```
SELECT
    N,
    CASE
        WHEN P IS NULL THEN 'root'
        WHEN N NOT IN (SELECT P FROM tree WHERE P IS NOT NULL) THEN 'leaf'
        ELSE 'inner'
    END AS type
FROM
    tree;
```

Logika:
1. Jesli wierzchołek N ma null w kolumnie przodków to oznacza, że nie ma przodka czyli jest rootem
2. Kazdy wierzchołek N ktory nie jest w kolumnie P - czyli nie jest przodkiem - jest liściem
3. Pozostałe są w takim razie węzłami (inner / node)