def print_pattern(n):
  for i in range(n):
    for j in range(i + 1):
      print("*", end=" ")
    print()

print_pattern(5)
