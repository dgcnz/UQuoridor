# The Problem

+ Maximise oponent's `min_distance` while minimizing self `min-distance`
+ Minimizing `max_distance`?
+ `valid_wall_placements()` needs to maintain a connected component that includes at least one of the goal states. -> `[Wullf-Nielsen, 2012]`
+ Concept of *time* is important:
    + it is better (but more dangerous) to delay a trap in order to maximise its effect on the oponent's `min_path`
+ Player only can (or has to) consider the connected component that includes him when computing its `min_path`
+ _Minimum distance field_ : Directed graph mask vs node/edge cost
+ matrix per player
    + una barrera crea dos lados. el que tiene mínimo no se recalcula, el otro sí
    + cambian todos los que son mayores o iguales al infectado que no dependan del infectado (que el infectado sea el único menor que lo acompañe)
    + encontrar el más chiquito encontrado con uno no sucio
    + primero infectas a los no mínimos y luego comienzas a propagar desde el menor de los no mínimos hasta llegar al mayor de los no mínimos. si quiero propagar un infectado n y todos sus vecinos están infectados significa que otro infectado ya recalculó todo su lado, skip it.
    + CÓMO MEDIR HEURISTICA DE PARED: cuál es el cambio entre la más chiquita y la sugiuiente, entre esa y la siguiente, etc. (la suma de las diferencias entre todos los afectados iniciales)


