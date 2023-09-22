class Solution:
    def isMatch(self, s='aaaaaaaaaaaaab', p="a*a*a*a*a*a*a*a*a*c"):
        memory = {}

        def test(s_index, p_index):
            if (s_index, p_index) in memory:
                return memory[(s_index, p_index)]

            s_index_end = s_index >= len(s)
            p_index_end = p_index >= len(p)
            next_star = p_index+1 < len(p) and p[p_index+1] == '*'

            if s_index_end:
                if p_index_end:
                    return True
                elif next_star:
                    memory[(s_index, p_index)] = test(s_index, p_index+2)
                    return memory[(s_index, p_index)]
                else:
                    memory[(s_index, p_index)] = False
                    return memory[(s_index, p_index)]

            if p_index_end:
                return False

            match = s[s_index] == p[p_index] or p[p_index] == '.'

            if next_star and match:
                print('1. ', next_star, match)
                memory[(s_index, p_index)] = test(
                    s_index+1, p_index) or test(s_index, p_index+2)
            elif next_star and match == False:
                print('2. ', next_star, match)
                memory[(s_index, p_index)] = test(s_index, p_index+2)
            elif next_star == False and match == True:
                print('3. ', next_star, match)
                memory[(s_index, p_index)] = test(s_index+1, p_index+1)
            elif next_star == False and match == False:
                print('4. ', next_star, match)
                memory[(s_index, p_index)] = False
            return memory[(s_index, p_index)]

        return test(0, 0)


solution = Solution()
print(solution.isMatch())
