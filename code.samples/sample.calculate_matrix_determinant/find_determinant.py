# finding a determinant of a square matrix of given size
aaa = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
dim_aaa = (3, 3)

a4 = [[1, -2, 3, 4], [2, 3, 4, 5], [3, 4, -5, 6], [4, 5, 6, 7]]
dim_a4 = (4, 4)

a5 = [[1, -2, 3, 4, 5],
      [2, 3, 4, 5, 6],
      [3, 4, -5, 6, 7],
      [0, 5, 6, -7, 0],
      [0, 0, 7, 7, 1]]
dim_a5 = (5, 5)


def keep_finding_det(dim: tuple, m: list): #, DEBUG=False):
    """
    recursively calcualte the determinant of a given square matrix
    """
    # BASE CASE,
    # ------------------------------------------------------------------------
    if dim == (1, 1):  # absolute base case
        return sum(m[0])

    # if dim == (2, 2):  # hardcoded base case
        # return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])

    # REDUCTION CASE, for all matrix of dim > 2
    # ------------------------------------------------------------------------
    # iterate through the top row, find cofactor sets and det. for each xij
    # given the formula: det[M] = xij * (-1)^(i+j) * det[Mij]
    #
    # for simplicity's sake, always choose first row for combination.

    col_limit = dim[1]
    i = 0  # fixed row index for the top row
    all_dets = []
    # if DEBUG:  # --------------------------------------------------------------
        # print(f"""GIVEN MATRIX: {m}\n TOP_ROW: {m[i]}\n""")
    # # -------------------------------------------------------------------------
    for j in range(col_limit):
        dim_cf_m, cf_m = extract_cofactor_mx((i, j), dim, m)
        # if DEBUG:  # ----------------------------------------------------------
            # print(f" cofactor set #{j}:\
                  # \n\tfor x_ij= {m[i][j]}:\n\t dim= {dim_cf_m}\n\t Mij= {cf_m}\n")
        # # ---------------------------------------------------------------------
        all_dets += \
            [m[i][j] * ((-1) ** (i + j)) * keep_finding_det(dim_cf_m, cf_m)]

    my_det = sum(all_dets)
    # if DEBUG:  # --------------------------------------------------------------
        # print(f"FINAL DETERTMINANT: {my_det}")
    # # -------------------------------------------------------------------------
    return my_det


def extract_cofactor_mx(ij: tuple, dim: tuple, m: list):
    r_lim, c_lim = dim
    i, j = ij
    cf_m = []
    for row in range(1, r_lim):
        cf_m_row = []
        for c in range(c_lim):
            if c == j:
                continue
            else:
                cf_m_row.append(m[row][c])
        cf_m.append(cf_m_row)
    dim_cf = (len(cf_m), len(cf_m[0]))
    return dim_cf, cf_m
