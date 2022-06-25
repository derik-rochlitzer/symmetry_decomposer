import numpy as np
from files.point_groups import *


def _convert_to_list(input_rep):
    """
    Convert the string of numbers of the input reducible representation into
    a list. Also, check if the numbers are valid.

    Parameters
    ----------
    input_rep: str
        String with the numbers split by spaces.
    
    Returns
    -------
    list
        List with the numbers of the reducible representation.
    """
    input_rep = input_rep.split()
    if len(input_rep) == 0:
        raise ValueError("Empty input representation!")
    try:
        input_rep = [int(num) for num in input_rep]
    except ValueError:
        raise ValueError("Non-integer reducible representation!")
    if all(num == 0 for num in input_rep):
        raise ValueError("Null reducible representation!")
    return input_rep
    

def _assemble_group_matrix(group):
    """
    Construct the matrix that has the irreducible representations of the group
    as columns.

    Parameters
    ----------
    group: dict
        Dictonary containing the irreducible representations of the group.
    
    Returns
    -------
    np.array
        Group matrix.
    """
    dim = len(group)
    group_matrix = np.empty((dim, dim))
    for i, irrep in enumerate(group):
        group_matrix[:, i] = group[irrep]
    return group_matrix


def _calc_coefs(input_rep, group_matrix):
    """
    Calculate the decomposition coefficients of the given representation. Also,
    check if they are integers.

    Parameters
    ----------
    input_rep: list
        List with the representation to decompose.
    group_matrix: np.array
        Matrix with the irreducible representations of the group as columns.
    
    Returns
    -------
    np.array
        Array with the calculated integer coefficients.
    """
    coefs = np.linalg.solve(group_matrix, input_rep)
    for coef in coefs:
        if int(coef) != coef:
            raise ValueError("Non-integer coeficient obtained!")
    return coefs.astype(int)


def _assign_irreps_to_coefs(coefs, group):
    """
    Get the string with the coefficient and the corresponding irreducible
    representation symbol.

    Parameters
    ----------
    coefs: np.array
        Given decomposition coefficients.
    group: dict
        Dictonary containing the irreducible representations of the
        corresponding group.

    Returns
    -------
    list
        List with coeficient + irreducible representation strings.
    """
    irreps = []
    for i, irrep in enumerate(group):
        coef = coefs[i]
        if coef < 0:
            raise ValueError("Negative coeficient obtained!")
        if coef != 0:
            irrep_str = str(coef) + irrep
            irreps.append(irrep_str)
    return irreps    


def decompose(input_rep, input_group):
    """
    Decompose a given reducible representation into the corresponding 
    irreducible ones.

    Parameters
    ----------
    input_rep: str
        String with the numbers of the reducible representation split by spaces.
    input_group: str
        Label of the corresponding symmetry point group.
    
    Returns
    -------
    str
        String with the decomposition of the reducible representation.
    """
    input_rep = _convert_to_list(input_rep)
    group = globals()[input_group]
    if len(input_rep) != len(group):
        raise ValueError("Input representation doesn't match the group!")
    group_matrix = _assemble_group_matrix(group)
    coefs = _calc_coefs(input_rep, group_matrix)
    irreps = _assign_irreps_to_coefs(coefs, group)
    return " + ".join(irreps)
