from typing import Iterator, List , Optional

def get_positive_numbers(numbers: List[int]) -> Iterator[int]:
    for num in numbers:
        if num >= 0:
            yield num

print(list(get_positive_numbers([1,-1,-2,0,2,3,4])))

def calculate_average(numbers:List[int] , ignore_zeros:Optional[bool] = False)-> float :
    if ignore_zeros:
        numbers=list(filter(lambda x : x!=0 , numbers))
    return sum(numbers)/len(numbers)

print((calculate_average([4,3,-4,-9.2,0,6,0,0,0,0,0,15,6] , True))