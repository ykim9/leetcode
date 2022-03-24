class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ori_color = image[sr][sc]
        
        def fill(x, y):
            # 범위를 벗어나거나, 기존 색상과 동일하지 않은 경우 처리하지 않음
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != ori_color:
                return
            
            image[x][y] = newColor
            
            # 현재 위치에서 네 방향 처리
            fill(x - 1, y)
            fill(x + 1, y)
            fill(x, y - 1)
            fill(x, y + 1)
        
        # 기존 색과 바꿀 색이 동일한 경우, 변경하지 않음
        if ori_color == newColor:
            return image
        
        fill(sr, sc)
        return image
        