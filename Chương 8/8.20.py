def e_approx(x, n):

  approx = 1
  term = 1

  for i in range(1, n + 1):
    term *= x / i
    approx += term

  return approx

def main():
  x = float(input("Nhập x: "))
  n = 1000
  print("e^x ~", e_approx(x, n))

if __name__ == "__main__":
  main()