def complete_bracelet(lst):
    """
    copied from 
    https://edabit.com/challenge/aMTXfakahQ45oZbJP
    solution to complete braclet challenge question
    :param lst: list of integers
    """
    s = ''.join([str(n) for n in lst])
    return any(len(s) % i == 0 and s[:i]*2 in s for i in range(2, len(lst)))
