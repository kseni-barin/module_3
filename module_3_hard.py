data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum = 0

def calculate_structure_sum(*args):
    global sum
    for element in args:
        if isinstance(element, list):
            calculate_structure_sum(*element)
        elif isinstance(element, dict):
            calculate_structure_sum(list(element.items()))
        elif isinstance(element, tuple):
            calculate_structure_sum(*element)
        elif isinstance(element, set):
            calculate_structure_sum(*element)
        elif isinstance(element, int):
            sum += element
        elif isinstance(element, str):
            sum += len(element)
    return sum


result = calculate_structure_sum(data_structure)
print(result)
