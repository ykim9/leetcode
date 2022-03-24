class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1) # 순열 비교용 Counter
        l = len(s1)
        matched = 0 # s2의 현재 window와 s1 일치 문자 수 
        
        for i, c in enumerate(s2):
            # 현재 글자가 counter에 있는지 확인하기 
            if c in counter:
                counter[c] -= 1
                if counter[c] == 0:
                    matched += 1
            
            #  현재 window 왼쪽 하나 이전 부분 처리하기
            if i >= l and s2[i - l] in counter:
                if counter[s2[i - l]] == 0:
                    matched -= 1
                counter[s2[i - l]] += 1
            
            # s1 character 가짓수와 s2 character의 가짓수가 일치하는 경우 True 
            if matched == len(counter):
                return True
        return False
                