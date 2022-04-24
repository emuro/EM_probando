def is_prime(num):
    '''Calculates whether num is a prime number,
    if it is return True otherwise return Flase'''

    try:
        int(num)
    except ValueError:
        raise ValueError("Ops. Input must be a positive integer")
    if int(num) != num or num < 0:
        raise ValueError("Ops. Input must be a positive integer")

    # SPECIALCASE: These are special cases that are not primes
    if num in [0, 1]: return False

    primes_to_remove = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in primes_to_remove:
        if num == prime: return True
        elif num % prime == 0: return False

    # Look for a factor
    limit = int(num**(0.5))+1
    for multiple in range(30, int(num**(0.5))+1, 30):
        for k in [1, 7, 11, 13, 19, 23, 29]:
            # If there is a factor
            if num % (multiple+k) == 0:
                # Its not a prime number
                return False
    return True



if __name__ == '__main__':

    N_MAX=100000
    print("n:", "\t", "num", "\t", "is_prime", "\t", "prime_count", "\t", ",prime_percent")
    p_count=0
    p_perc=0

    if 0: # metodo de fer
        for n in range(2,N_MAX+1):
            fer_num=1
            for i in range(2,n+1):
                fer_num += 2*i
            result=is_prime(fer_num)
            if result:
                p_count+=1
            p_perc=p_count*100/(n-1)

            if(n<=100 or n==200 or n==300 or n==400 or n%10000==0):
                print(n, "\t", fer_num, "\t", is_prime(fer_num), "\t", p_count, "\t", p_perc)

    if 1: # enteros a saco
        for n in range(2,N_MAX+1):
            fer_num=n
            result=is_prime(fer_num)
            if result:
                p_count+=1
            p_perc=p_count*100/(n-1)

            if (n<=100 or n==200 or n==300 or n==400 or n%10000==0):
                print(n,"\t",fer_num,"\t",is_prime(fer_num),"\t",p_count,"\t",p_perc)