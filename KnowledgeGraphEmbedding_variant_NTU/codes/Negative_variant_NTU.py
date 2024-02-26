import numpy as np


def set_data(data):
    return np.array(data)


def find_antisymmetric_triples(all_triples, triple):
    h, r, t = triple

    # Maschera per filtrare triple con h1 uguale a t, t1 uguale a h e r1 diverso da r
    mask_antisymmetric = np.logical_and.reduce((all_triples[:, 0] == t, all_triples[:, 2] == h, all_triples[:, 1] != r))
    mask_antisymetric = ~mask_antisymetric
    #filtered_antisymmetric_triples = all_triples[~mask_antisymmetric]
    filtered_antisymmetric_triples = all_triples[mask_antisymmetric]


    return filtered_antisymmetric_triples

def find_inverse_triples(all_triples, h, r, t):
    #h, r, t = triple

    # Maschera per filtrare triple con h1 uguale a t e t1 uguale a h
    mask_inverse = np.logical_and.reduce((all_triples[:, 0] == t, all_triples[:, 1] != r, all_triples[:, 2] == h))
    mask_inverse = ~mask_inverse
    #filtered_inverse_triples = all_triples[~mask_inverse]
    filtered_inverse_triples = all_triples[mask_inverse]

    return mask_inverse

def find_symmetric_triples(all_triples, h,r,t):
    #h, r, t = triple

    # Maschera per filtrare triple con h1 uguale a t, t1 uguale a h e r1 uguale a r
    mask_symmetric = np.logical_and.reduce((all_triples[:, 0] == t, all_triples[:, 1] == r, all_triples[:, 2] == h))
    #filtered_symmetric_triples = all_triples[~mask_symmetric]
    mask_symmetric = ~mask_symmetric

    filtered_symmetric_triples = all_triples[mask_symmetric]


    return mask_symmetric


def select_corruption_NTU(all_triples, head, relation, tail, k):
    random_rows = np.random.choice(all_triples.shape[0], size=k, replace=False)
    all_triples = all_triples[random_rows]

    head = np.asarray(head)
    relation = np.asarray(relation)
    tail = np.asarray(tail)

    #mask = np.logical_or.reduce((all_triples[:, 0] != head, all_triples[:, 1] != relation, all_triples[:, 2] != tail))

    '''

    mask = np.logical_and.reduce((all_triples[:, 0] != head, all_triples[:, 1] != relation))
    all_triples = all_triples[mask]

    mask = np.logical_and.reduce((all_triples[:, 1] != relation, all_triples[:, 2] != tail))
    all_triples = all_triples[mask]
    '''
    
    mask = np.logical_and.reduce((np.logical_and(all_triples[:, 0] != head, all_triples[:, 1] != relation),
                              np.logical_and(all_triples[:, 1] != relation, all_triples[:, 2] != tail)))

    all_triples = all_triples[mask]
    #print("Dimensione dopo la prima maschera:", all_triples.shape)
    
    
    mask_symmetric = find_symmetric_triples(all_triples, head,relation,tail)
    #print(f"Dimensione di della maschera {mask_symmetric.shape}")
    negative_triple = all_triples[mask_symmetric]
    #print("Dimensione dopo la maschera simmetrica:", negative_triple.shape)
    
    
    mask_inverse = find_inverse_triples(all_triples, head,relation,tail)
    negative_triple = all_triples[mask_inverse]
    #print("Dimensione dopo la maschera inversa:", negative_triple.shape)
    

    '''
    mask = find_composed_triple(all_triples, head, relation, tail)
    negative_triple = negative_triple[~mask]'''



    return negative_triple
