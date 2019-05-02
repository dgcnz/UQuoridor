import math


def heuristic_cost_estimate(start, goal):
    return 0  #TODO FIX


def lowScore(dict_f):
    lowest_k = list(dict_f)[0]
    lowest_v = dict_f[list(dict_f)[0]]
    for k, v in dict_f:
        if v < lowest:
            lowest_k = k
    return lowest_k


def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.Keys:
        current = cameFrom[current]
        total_path.append(current)
    return total_path


def A_Star(start, goal):
    closedSet = set()

    openSet = {start}

    cameFrom = dict()

    gScore = dict()  #Init all to INF(math.inf)

    gScore[start] = 0

    fScore = dict()  #Init all to INF(math.inf)

    fScore[start] = heuristic_cost_estimate(start, goal)

    while not openSet.any():
        current = lowScore(fScore)
        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.remove(current)

        for neighbor in current:
            if neighbor in closedSet:
                continue

            tentative_gScore = gScore[current] + dist_between(
                current, neighbor)

            if neighbor not in openSet:
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue

            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(
                neighbor, goal)
