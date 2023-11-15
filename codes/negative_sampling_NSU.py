
import numpy as np
from typing import List, Tuple

TripleArray = np.ndarray

# Conversione della lista delle triple in array
def convert_in_array(triples: List[Tuple[int, int, int]]) -> TripleArray:
    return np.array(triples)

#Creazione della maschera delle triple che condividono head e relation simili a quelle da corrompere
def delete_peers_head(subset_triples: TripleArray, head: int, relation: int) -> np.ndarray:

    head = np.asarray(head)
    relation = np.asarray(relation)

    head_relation_mask = np.logical_or(subset_triples[:, 0] != head, subset_triples[:, 1] != relation)
    #negative_peers_head = subset_triples[head_relation_mask]

    tot_removed = np.sum(~head_relation_mask)
    print(f"Number of triples removed(head): {tot_removed}")


    return head_relation_mask


#Creazione della maschera delle triple che condividono tail e relation simili a quelle da corrompere
def delete_peers_tail(subset_triples: TripleArray, tail: int) -> np.ndarray:

    tail = np.asarray(tail)

    relation_tail_mask = subset_triples[:, 2] != tail
    #negative_peers_tail = subset_triples[relation_tail_mask]

    tot_removed = np.sum(~relation_tail_mask)
    print(f"Number of triples removed(tail): {tot_removed}")

    return relation_tail_mask


#Processo di selezione dei campioni negativi da inserire nella fase di addestramento
def selection_corruption_candidate_triples(triples: List[Tuple[int, int, int]],
                                           head: int, relation: int, tail: int, k: int) -> TripleArray:

    #triples = convert_in_array(triples)

    print(f"Start of peers' research...")

    #Selezione casuale di k triple dall'intero dataset
    random_rows = np.random.choice(triples.shape[0], size=k, replace=False)
    subset_triples = triples[random_rows]

    #creazione delle maschere
    head_relation_mask = delete_peers_head(subset_triples, head, relation)
    relation_tail_mask = delete_peers_tail(subset_triples, tail)
    print(f"...Created masks!")

    #creazione della maschera finale
    negative_mask = np.logical_and(head_relation_mask, relation_tail_mask)

    #selezione delle triple triple corrotte
    corrupt_triples = subset_triples[negative_mask]

    print(f"Triple corrupt created...!")
    return corrupt_triples