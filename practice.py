x = ["favor", "faith", "peace", "wisdom", "fizz"]
def fizz_count(x):
    count = 0
    for item in d:
        if item == "fizz":
            count = count + 1
    return count

d = ["cat", "fizz", "not", "over", "yet", "fizz"]
fizz = fizz_count(d)
print(fizz)
