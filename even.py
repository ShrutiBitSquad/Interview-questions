startpoint = int(input("Enter starting point: "))
endpoint = int(input("Enter ending point: "))
even_numbers = lambda x: x % 2 == 0, range(startpoint,endpoint)
print(list(even_numbers))

nums = list(map(str,input("Enter a number: ").split(',')))
print(nums)
def alphagenerators(s):
    def sortalpha(word):
        split_word = word.split()[0].lower()
        return split_word

    sorted_list = sorted(s,key = sortalpha)

    for i in sorted_list:
        yield i

s  = ['applE', 'CaT', 'Dog', 'bAll', 'Mango', 'zEbra', 'grapes', 'TigEr']
sl = []
gen = alphagenerators(s)
for i in gen:
    sl.append(i)
print(sl)