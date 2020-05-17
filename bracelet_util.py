import random
DIGITS = 24
def complete_bracelet(lst):
    """
    copied from 
    https://edabit.com/challenge/aMTXfakahQ45oZbJP
    solution to complete braclet challenge question
    :param lst: list of integers
    """
    s = ''.join([str(n) for n in lst])
    return any(len(s) % i == 0 and s[:i]*2 in s for i in range(2, len(lst)))


def gen_possible_bracelet():
    """
    generates bracelet or not
    according to
    https://edabit.com/challenge/aMTXfakahQ45oZbJP
    :return: array of integers possibly
    meeting the definition defined in coding challenge
    we need some non-bracelets for coding
    """
    if random.random() > 0.5:
        # generate a bracelet
        # base pattern can be 1 to 12 digits
        pattern_int = random.randint(1,int(10**(DIGITS/2)))
        pattern_lst = [x for x in str(pattern_int)]
        result = pattern_lst.copy()
        while len(result + pattern_lst) <= DIGITS:
            result += pattern_lst
        # TODO maybe take this out if not
        # debugging to save time generating
        # data
        assert(complete_bracelet(result))
        # add a label of 1
        result += ['1']
        return result
    else:
        # generate an array of random integers
        # if it happens to be a bracelet add
        # one fo label, 0 otherwise
        pattern_int = random.randint(1,int(10**DIGITS))
        pattern_lst = [x for x in str(pattern_int)]
        pattern_lst += ['1'] if complete_bracelet(pattern_lst) else ['0']
        return pattern_lst
