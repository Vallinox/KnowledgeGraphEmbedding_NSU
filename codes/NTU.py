from collections import defaultdict
import numpy as np

def getpeers(e, E, St):
    peers = set()

    if len(E[e])==0:
      return set(E.keys())

    for x, y in E[e].items():
        for value in y:
            peers.update(St[x][value])

    if len(peers) <=1:
      return set(E.keys())

    return peers


def getpeersHead(t, E, St):
    peers = set()

    if len(St[t])==0:
      return set(St.keys())

    for x, y in St[t].items():
        for value in y:
            peers.update(E[value][x])
    
    if len(peers) <=1:
      return set(St.keys())

    return peers

def get_negative_ranked(candidates, k):
    corrupt = np.array([])

    candidate_list = [(key, value) for key, value in candidates.items()]
    candidate_list.sort(key=lambda x: -x[1])
    corrupt = np.append(corrupt, [int(element[0][k]) for element in candidate_list]).astype(int)

    return corrupt


def search_negative_useful(e,r, Et, St, table_as_triples, k):
    peers = getpeers(e, Et, St)
    candidates = defaultdict(int)
    for p in peers:
        if p == e:
            continue
        #for x, values in Et[p].items():
            #for y in values:
        for y in Et[p][r]:
            if (e, r, y) in table_as_triples:
                continue

            candidates[(r, y)] += 1
    return get_negative_ranked(candidates, k)


def search_negative_head_useful(t,r, Et, St2,table_as_triples, k):
    peers = getpeersHead(t, Et, St2)
    candidates = defaultdict(int)
    for p in peers:
            if p == t:
                continue
            for y in St2[p][r]:

                if (y, r, t) in table_as_triples:
                    continue

                candidates[(y, r)] += 1
    return get_negative_ranked(candidates, k)

