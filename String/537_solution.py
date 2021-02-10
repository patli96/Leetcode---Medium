class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:

        def extract_num(complex_num):
            a = ''
            b = ''
            operator = ''
            flag = 1
            idx = 0

            if complex_num[0] == '-':
                flag = -1
                idx = 1

            while complex_num[idx].isnumeric():
                a += complex_num[idx]
                idx += 1
            while not complex_num[idx].isnumeric():
                operator += complex_num[idx]
                idx += 1
            while complex_num[idx].isnumeric():
                b += complex_num[idx]
                idx += 1

            if operator == '+-':
                return flag * int(a), -int(b)
            else:
                return flag * int(a), int(b)

        a1, a2 = extract_num(a)
        b1, b2 = extract_num(b)

        return str(a1 * b1 + a2 * b2 * -1) + '+' + str(a1 * b2 + a2 * b1) + 'i'  