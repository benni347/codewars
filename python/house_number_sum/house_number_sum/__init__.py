def house_numbers_sum(inp):
    sum_var = 0
    for i in range(len(inp)):
        if inp[i] == 0:
            return sum_var

        sum_var += inp[i]

# Not my solution, but best practice:
# def house_numbers_sum(inp):
#     return sum(inp[:inp.index(0)])
