# Computes the height of Skippy's nth jump
def skippy(n):
  if n == 1:
    return 100
  return (8 * skippy(n-1))/9 + 1

print (skippy(39))
print (skippy(40))
