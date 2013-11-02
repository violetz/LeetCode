def water_amount(ls_height, ledge, redge):
    i_width = abs(redge - ledge)
    i_height = min(ls_height[ledge], ls_height[redge])
    return i_width * i_height

def max_container(ls_height):
    ledge = 0
    redge = len(ls_height) - 1
    max_water = water_amount(ls_height, ledge, redge)
    while True:
        while ledge < redge and ls_height[ledge] <= ls_height[redge]:
            max_water = max(water_amount(ls_height, ledge, redge), max_water)
            ledge += 1
            
        while ledge < redge and ls_height[ledge] >= ls_height[redge]:
            max_water = max(water_amount(ls_height, ledge, redge), max_water)
            redge -= 1
        if ledge >= redge:
            break

    return max_water
            
def direct_max_container(ls_height):
    max_water = 0
    for i in range(len(ls_height)):
        for j in range(i+1, len(ls_height)):
            max_water = max(water_amount(ls_height, i, j), max_water)
    return max_water

def max_container_test():
    import numpy.random as nprnd
    for i_test in range(1000):
        n = nprnd.randint(20)
        if n == 0:
            continue
        ls_height = list(nprnd.randint(10, size = n))
        print ls_height, max_container(ls_height)
        assert(max_container(ls_height) == direct_max_container(ls_height))

if __name__ == '__main__':
    max_container_test()
