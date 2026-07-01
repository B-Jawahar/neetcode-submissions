class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1

        while left<=right:
            tmp=left+(right-left)//2
            if matrix[tmp][0]==target:
                return True
            elif matrix[tmp][0]<target:
                if matrix[tmp][-1]==target:
                    return True
                elif matrix[tmp][-1]<target:
                    left=tmp+1
                else:
                    break
            else:
                right=tmp-1
        
        inleft=0
        inright=len(matrix[tmp])-1

        while inleft<=inright:
            intmp=inleft+(inright-inleft)//2
            if matrix[tmp][intmp]==target:
                return True
            elif matrix[tmp][inleft]<target:
                inleft=intmp+1
            else:
                inright=intmp-1
        return False