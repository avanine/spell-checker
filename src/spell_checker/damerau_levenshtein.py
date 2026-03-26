class DamerauLevenshtein:

    def create_matrix(self, m, n):
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            matrix[i][0] = i
        for j in range(n):
            matrix[0][j] = j

        return matrix

    def distance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        matrix = self.create_matrix(m + 1, n + 1)

        # Käydään läpi matriisin jokainen solu ja lasketaan etäisyys
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                letters_distance = 0 if word1[i - 1] == word2[j - 1] else 1

                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,   # Kirjaimen poistaminen (deletion)
                    matrix[i][j - 1] + 1,   # Kirjaimen lisääminen (insertion)
                    matrix[i - 1][j - 1] + letters_distance # Kirjaimen korvaaminen (substitution)
                )

                # Transpositio (kahden peräkkäisen merkin vaihtaminen)
                # Jos kaksi peräkkäistä merkkiä ovat samat molemmissa sanoissa
                # mutta eri järjestyksessä, vaihto onnistuu yhdellä operaatiolla
                if i > 1 and j > 1 and word1[i-1] == word2[j-2] and word1[i-2] == word2[j-1]:
                    matrix[i][j] = min(matrix[i][j], matrix[i-2][j-2] + 1)

        return matrix[m][n]
