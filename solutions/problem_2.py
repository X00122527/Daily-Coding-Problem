# def productOfAllDoubleLoop(arr):
#     lista = []
#     for i in range(len(arr)):
#         total = 1
#         for j in range(len(arr)):
#             if (i != j):
#                 total *= arr[j]
#
#         lista.append(total)
#
#     return lista

# def getProduct(arr):
#     result = 1
#     for i in arr:
#         result *= i
#     return result
#
#
# def productNoDivision(arr):
#     lista = []
#     for i in range(len(arr)):
#         temp = list(arr[:i] + arr[i + 1:])
#         lista.append(getProduct(temp))
#
#     return lista



def getFactors(arr):
    product = 1
    output_list = []
    for dig in arr:
        product *= dig

    for i in range(len(arr)):
        output_list.append(int(product / arr[i]))

    return output_list


if __name__ == '__main__':
    assert getFactors([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert getFactors([3, 2, 1]) == [2, 3, 6]
