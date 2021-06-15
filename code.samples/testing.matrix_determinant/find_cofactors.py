# finding a determinant of a square matrix of given size
a2 = [[1,2],[-1,0]]
dim_a2 = (2,2)

a3 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
dim_a3 = (3, 3)

a4 = [[1, -2, 3, 4], [2, 3, 4, 5], [3, 4, -5, 6], [4, 5, 6, 7]]
dim_a4 = (4, 4)

a5 = [[1, -2, 3, 4, 5],
      [2, 3, 4, 5, 6],
      [3, 4, -5, 6, 7],
      [0, 5, 6, -7, 0],
      [0, 0, 7, 7, 1]]
dim_a5 = (5, 5)


def keep_finding_cofactors(dim: tuple, m: list): #, DEBUG=False):
    """
    recursively calcualte the determinant of a given square matrix
    """
    # BASE CASE,
    # ------------------------------------------------------------------------
    if dim == (1, 1):  # absolute base case
        return sum(m[0])


    # REDUCTION CASE, for all matrix of dim > 2
    row_limit, col_limit = dim
    cofactors = []
    for i in range(row_limit):
        row_factors = []
        for j in range(col_limit):
            dim_cf_m, cf_m = extract_cofactor_mx((i, j), dim, m)
            # if DEBUG:  # ----------------------------------------------------------
                # print(f" cofactor set #{j}:\
                    # \n\tfor x_ij= {m[i][j]}:\n\t dim= {dim_cf_m}\n\t Mij= {cf_m}\n")
            # # ---------------------------------------------------------------------
            row_factors += [((-1) ** (i + j)) * keep_finding_cofactors(dim_cf_m, cf_m)]
        cofactors += [row_factors]

    # if DEBUG:  # --------------------------------------------------------------
        # print(f"FINAL DETERTMINANT: {my_det}")
    # # -------------------------------------------------------------------------
    print("COFACTORS:")
    for row in cofactors:
        print(row)
    return cofactors


def extract_cofactor_mx(i_j: tuple, dim: tuple, m: list):
    """
    find the cofactor matrix for a given x_ij
    """
    r_lim, c_lim = dim
    i, j = i_j
    # cf_m = [[m[row][c] for c in range(c_lim) if c != j] for row in range(r_lim) if row != i]
    cf_m = []
    for row in range(r_lim):
        if row == i:
            continue
        cf_row = []
        for c in range(c_lim):
            if c == j:
                continue
            cf_row += [m[row][c]]
        cf_m += [cf_row]

    # print(f"DEBUG {cf_m}")
    for r in cf_m:
        print(r)
    dim_cf = (len(cf_m), len(cf_m[0]))
    return dim_cf, cf_m
