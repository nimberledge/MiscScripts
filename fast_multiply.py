from math import sqrt

prime_dict = {}
def is_prime(n):
    if n in prime_dict:
        return prime_dict[n]
    if n == 1:
        prime_dict[n] = False
        return False
    if n == 2:
        prime_dict[n] = True
        return True

    for i in range(3, int(sqrt(n)) + 1, 2):
        if i in prime_dict and not prime_dict[i]:
            continue
        if n % i == 0:
            prime_dict[n] = False
            return False
    prime_dict[n] = True
    return True

def find_smallest_factor(k):
    if is_prime(k):
        return 1
    if k % 2 == 0:
        return 2
    for i in range(3, int(sqrt(k))+1, 2):
        if k % i == 0:
            return i
    return -1

fm_table = {}
def fast_multiply_steps(n, path=[]):
    if n in fm_table:
        return fm_table[n]
    if n == 0:
        fm_table[0] = (0, [])
        return (0, path)
    if n == 1:
        fm_table[1] = (0, [])
        return (0, path)

    small_f = find_smallest_factor(n)
    if small_f == 1:
        step, path = fast_multiply_steps(n//2, path)
    big_f = n / small_f
    step1, path1 = fast_multiply_steps(big_f, path)
    step1 *= small_f
    step2, path2 = fast_multiply_steps(n // 2, path)
    if n % 2 == 0:
        step2 += 1
    else:
        step2 += 2

    if step1 < step2:
        fm_table[n] = (step1, path1.append(n))
    else:
        fm_table[n] = (step2, path2.append(n))
    return fm_table[n]

def main():
    print (fast_multiply_steps(15))

if __name__ == '__main__':
    main()
