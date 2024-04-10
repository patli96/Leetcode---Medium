class Solution:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        super_ugly_primes = [1]
        super_ugly_primes_set = set([1])
        prime_idx_dict = {i: -1 for i in primes}
        
        if n <= len(super_ugly_primes) - 1:
            return super_ugly_primes[n]

        while len(super_ugly_primes) < n:
            next_number_list = [
                i * super_ugly_primes[prime_idx_dict[i] + 1]
                for i in primes
            ]
            next_number = min(next_number_list)
            prime_to_update = primes[next_number_list.index(next_number)]
            if next_number in super_ugly_primes_set:
                prime_idx_dict[prime_to_update] += 1
                continue
            
            super_ugly_primes.append(next_number)
            super_ugly_primes_set.add(next_number)
            prime_idx_dict[prime_to_update] += 1

        return super_ugly_primes[-1]
            
            
