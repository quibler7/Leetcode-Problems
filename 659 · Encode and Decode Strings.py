class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
        

    def decode(self, str):
        res = []
        i = 0

        while i < len(str):
            j = i 
            while str[j] != '#':
                j += 1
            
            # now j is at '#' for encoded string '4#bubu'
            # everything from i to j without including j is length 
            # as we can see, so we will store it in length
            length = int(str[i:j])

            # in res array we will append string
            # string begins from j+1 and takes length chars
            res.append(str[j+1:j+1+length])

            # i will be set to start of new string
            i = j+1+length

            return res
