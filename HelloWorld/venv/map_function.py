def even_or_odd(num):
  if num%2==0:
    return "The Number {} is Even".format(num)
  else:
    return "The Number {} is odd".format(num)
lst =[2,3,4,6,8,3,7,33,5,7,]
# x = even_or_odd(36)
# print(x)

list = list(map(even_or_odd, lst))
print(list)


