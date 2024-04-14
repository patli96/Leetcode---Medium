class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()

        positive_numbers = [i for i in nums if i > 0]
        positive_numbers_set = set(positive_numbers)
        negative_numbers = [i for i in nums if i < 0]
        negative_numbers_set = set(negative_numbers)
        zeros = [i for i in nums if i == 0]

        # with 0s
        if len(zeros) > 0:
            if len(zeros) >= 3:
                result.add((0, 0, 0))
            for i in positive_numbers:
                if -1 * i in negative_numbers:
                    result.add((-1 * i, 0, i))
        
        if len(negative_numbers) == 0 or len(positive_numbers) == 0:
            return result
        
        # one positive number and two negative numbers
        for j in range(len(negative_numbers)):
            for k in range(j + 1, len(negative_numbers)):
                if (negative_numbers[j] + negative_numbers[k]) * -1 in positive_numbers_set:
                    result.add(
                        tuple(
                            sorted(
                                [
                                    negative_numbers[j],
                                    negative_numbers[k],
                                    (negative_numbers[j] + negative_numbers[k]) * -1
                                ]
                            )
                        )
                    )
        
        # one negative number and two positive numbers
        for j in range(len(positive_numbers)):
            for k in range(j + 1, len(positive_numbers)):
                if (positive_numbers[j] + positive_numbers[k]) * -1 in negative_numbers_set:
                    result.add(
                        tuple(
                            sorted(
                                [
                                    (positive_numbers[j] + positive_numbers[k]) * -1,
                                    positive_numbers[j],
                                    positive_numbers[k]
                                ]
                            )
                        )
                    )
    
        return [list(i) for i in result]

