class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        length = len(image)
        width = len(image[0])
        start = image[sr][sc]
        visited = [[0] * width for _ in range(length)]
        self.dfs(image, sr, sc, newColor, visited, start)       
        return image


    def dfs(self, image, i, j, newColor, visited, start):
        if(i < 0 or i > len(image) - 1 or j < 0 or j > len(image[0]) - 1 or visited[i][j] or image[i][j] != start):
            return
        
        image[i][j] = newColor
        visited[i][j] = 1
        self.dfs(image, i, j + 1, newColor, visited, start)
        self.dfs(image, i + 1, j, newColor, visited, start)
        self.dfs(image, i - 1, j, newColor, visited, start)
        self.dfs(image, i, j - 1, newColor, visited, start)