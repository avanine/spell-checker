class DamerauLevenshtein:

    def create_matrix(self, m, n):       
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            matrix[i][0] = i
        for j in range(n):
            matrix[0][j] = j

        return matrix

    def distance(self, word1, word2):
        m = len(word1) + 1
        n = len(word2) + 1
        matrix = self.create_matrix(m, n)
        
        return 0