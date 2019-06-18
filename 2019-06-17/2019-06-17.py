liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3

def k_last(k, liste):
  liste.pop(-k)
  return liste

print(k_last(k, liste))