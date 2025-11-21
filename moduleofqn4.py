def multiplication_table(n, limit):
    table = []
    for i in range(1, limit + 1):
        table.append(f"{n} x {i} = {n * i}")
    return table

# module that is used in qn4 for operation 