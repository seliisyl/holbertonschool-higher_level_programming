#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)
    return result_list
