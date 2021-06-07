# finding a determinant of a square matrix of given size
import copy

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


def keep_finding_det(dim: tuple, m: list, DEBUG=False):
    """
    recursively calcualte the determinant of a given square matrix
    """
    # BASE CASE,
    # ------------------------------------------------------------------------
    if dim == (1, 1):  # absolute base case
        return sum(m[0])

    if dim == (2, 2):  # hardcoded base case
        det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        # if DEBUG:
            # for r in m:
                # print(r)
            # print(f"{det}")
        return det

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
    DEBUG = True
    for j in range(col_limit):
        dim_cf_m, cf_m = extract_minor_matrix((i, j), dim, m)
        # if DEBUG:  # ----------------------------------------------------------
            # print(f" cofactor set #{j}:\
                  # \n\tfor x_ij= {m[i][j]}:\n\t dim= {dim_cf_m}\n\t Mij= {cf_m}\n")
        # # ---------------------------------------------------------------------
        if DEBUG:
            d = keep_finding_det(dim_cf_m, cf_m, DEBUG)
            c = (-1) ** (i + j) * d
            print(f"det={d}")
            print(f"{i} + {j} == {i + j}")
            print(f"cofactor={c}")
            all_dets.append(c)
        else:
            all_dets += \
                [m[i][j] * ((-1) ** (i + j)) * keep_finding_det(dim_cf_m, cf_m)]

    my_det = sum(all_dets)

    # if DEBUG:  # --------------------------------------------------------------
        # print(f"FINAL DETERTMINANT: {my_det}")
    # # -------------------------------------------------------------------------
    return my_det


def extract_minor_matrix(i_j: tuple, dim: tuple, m: list):
    """
    find the Minor matrix
    """
    r_lim, c_lim = dim
    i, j = i_j
    minor = [[m[r][c] for c in range(c_lim) if c != j] for r in range(r_lim) if r != i]
    dim_minor = (len(minor), len(minor[0]))
    return dim_minor, minor 


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
# def find_cfm(dim: tuple, m: list, DEBUG=False):
    # """
    # find the Cofactor matrix
    # """
    # row_limit, col_limit = dim

    # cfm = []
    # for i in range(row_limit):
        # temp_m = copy.copy(m)
        # if i > 0 and i < row_limit - 1:
            # for k in reversed(range(i)):
                # row = copy.copy(temp_m[k])
                # temp_m[k] = temp_m[k-1]
                # temp_m[k-1] = row

        # cfr = []
        # for j in range(col_limit):
            # dim_minor, minor = extract_minor_matrix((i, j), dim, temp_m)
            # if DEBUG:
                # d = keep_finding_det(dim_minor, minor, DEBUG)
                # c = (-1) ** (i + j) * d
                # print(f"{d} {i + j} {c}")
                # cfr.append(c)
            # else:
                # cfr += [(-1) ** (i + j) * keep_finding_det(dim_minor, minor)]
        # cfm += [cfr]

    # # if DEBUG:  # --------------------------------------------------------------
        # # for row in cfm:
            # # print(row)
    # # # -------------------------------------------------------------------------
    # return cfm


if __name__ == "__main__":
    print(f"module {__name__} explicitly called")
