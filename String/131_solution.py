class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def backtrack(p_substr, s, idx, partition, res):
            # print(f'BACKTRACKING:\tsub={p_substr}\tpartition={partition}')
            if idx + 1 < len(s):
                # print(f'backtrack({p_substr + s[idx+1]}, s, {idx+1}, {partition}, {res})')
                backtrack(p_substr + s[idx + 1], s, idx + 1, partition, res)
                if is_palindrome(p_substr):
                    # print(p_substr)
                    # print(f'backtrack({s[idx+1]}, s, {idx+1}, {partition}, {res})')
                    backtrack(s[idx + 1], s, idx + 1, partition + [p_substr], res)
            else:
                if is_palindrome(p_substr):
                    if partition + [p_substr] not in res:
                        res.append(partition + [p_substr])

        def is_palindrome(substr):
            if len(substr) == 1:
                return True
            if len(substr) % 2 == 0:
                if substr[0:int(len(substr) / 2)][::-1] == substr[int(len(substr) / 2):len(substr)]:
                    return True
            else:
                if substr[0:int(len(substr) / 2)][::-1] == substr[int(len(substr) / 2) + 1:len(substr)]:
                    return True
            return False

        backtrack(s[0], s, 0, [], res)

        return res