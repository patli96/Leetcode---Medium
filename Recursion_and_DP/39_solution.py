class Solution:

    def find_candidates(self, found_candidates: List[int], target: int) -> List[int]:
        for i in self.candidates:
            if i == target:
                self.result.append(sorted(found_candidates + [i]))
            if i > target:
                continue
            self.find_candidates(
                found_candidates=found_candidates + [i],
                target=target - i
            )

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        initial_candidates = [[i] for i in candidates if i < target]
        self.result = [[i] for i in candidates if i == target]
        print(initial_candidates)
        for found_candidates in initial_candidates:
            self.find_candidates(
                found_candidates=found_candidates,
                target=target - found_candidates[0]
            )
        return list(
            [list(i) for i in set([tuple(i) for i in self.result if i])]
        )

