#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    l = []
    ans = 0
    for i in range(0, list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
        except IndexError:
            ans = 0
            print("out of range")
        except TypeError:
            ans = 0
            print("wrong type")
        finally:
            pass
        l.append(ans)
    return (l)
