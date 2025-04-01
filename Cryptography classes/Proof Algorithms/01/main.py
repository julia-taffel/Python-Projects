def euklide(a, b):
    if b == 0:
        return a
    else:
        return euklide(b, a % b)

def GCP(*numbers):
    if not numbers:
        return None
    result = numbers[0]
    for i in numbers[1:]:
        result = euklide(result, i)
    return result
    
a = 243
b = 108

print(f"GCP({a}, {b}) = {euklide(a, b)}")
      
numbers = [24, 36, 68]
print(f"GCP({numbers}) = {GCP(*numbers)}")
