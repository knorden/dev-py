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


def keep_finding_det(dim: tuple, m: list, DEBUG=False):
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
    # given the formula: det[A] = xij * (-1)^(i+j) * det[Mij]
    #
    # for simplicity's sake, always choose first row for combination.

    col_limit = dim[1]
    i = 0  # fixed row index for the top row
    all_dets = []
    if DEBUG:  # --------------------------------------------------------------
        print(f"""GIVEN MATRIX: {m}\n TOP_ROW: {m[i]}\n""")
    # -------------------------------------------------------------------------
    for j in range(col_limit):
        dim_minor , minor = extract_minor_matrix((i, j), dim, m)
        if DEBUG:  # ----------------------------------------------------------
            print(f" cofactor set #{j}:\n\t\
                    for x_ij= {m[i][j]}:\n\t\
                    dim= {dim_minor}\n\t Mij= {minor}\n")
        # ---------------------------------------------------------------------
        all_dets += \
            [m[i][j] * ((-1) ** (i + j)) * keep_finding_det(dim_minor, minor)]

    my_det = sum(all_dets)
    if DEBUG:  # --------------------------------------------------------------
        print(f"FINAL DETERTMINANT: {my_det}")
    # -------------------------------------------------------------------------
    return my_det


def find_cfm(dim: tuple, m: list, DEBUG=False):
    row_limit, col_limit = dim

    cfm = []
    for i in range(row_limit):
        cfr = []
        for j in range(col_limit):
            dim_minor, minor = extract_minor_matrix((i, j), dim, m)
            cfr += [(-1) ** (i + j) * keep_finding_det(dim_minor, minor)]
        cfm += [cfr]

    if DEBUG:
        for row in cfm:
            print(row)
    return cfm


def extract_minor_matrix(i_j: tuple, dim: tuple, m: list):
    """
    find the Minor Matrix
    """
    r_lim, c_lim = dim
    i, j = i_j
    cfm = [[m[r][c] for c in range(c_lim) if c != j] for r in range(r_lim) if r != i]
    dim_cfm = (len(cfm), len(cfm[0]))
    return dim_cfm, cfm


# def extract_cofactor_mx(ij: tuple, dim: tuple, m: list):
    # r_lim, c_lim = dim
    # i, j = ij
    # cf_m = []
    # for r in range(1, r_lim):
        # cf_m_row = []
        # for c in range(c_lim):
            # if c == j:
                # continue
            # else:
                # cf_m_row.append(m[r][c])
        # cf_m.append(cf_m_row)
    # dim_cf = (len(cf_m), len(cf_m[0]))
    # return dim_cf, cf_m

if __name__ == "__main__":
    print(f"module {__name__} explicitly called")
