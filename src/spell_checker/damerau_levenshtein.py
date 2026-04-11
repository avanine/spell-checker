"""Damerau-Levenshtein-etäisyyden laskeminen."""

class DamerauLevenshtein:
    """Laskee kahden sanan välisen Damerau-Levenshtein-etäisyyden."""
    def create_matrix(self, m, n):
        """Luo ja alustaa etäisyysmatriisin."""
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            matrix[i][0] = i
        for j in range(n):
            matrix[0][j] = j

        return matrix

    def distance(self, word1, word2):
        """Laskee kahden sanan välisen etäisyyden."""
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

    def compute_row(self, word, char, prev_char, previous_row, two_rows_back):
        """Laskee yhden rivin DL-matriisista.

        Args:
            word: haettava sana (käyttäjän syöte)
            char: nykyinen merkki (trien solmu)
            prev_char: edellinen merkki triessä (transpositiota varten)
            previous_row: edellinen rivi DL-matriisista
            two_rows_back: sitä edellinen rivi (transpositiota varten)
        """
        columns = len(word) + 1
        current_row = [previous_row[0] + 1]

        for j in range(1, columns):
            cost = 0 if word[j - 1] == char else 1

            current_row.append(min(
                current_row[j - 1] + 1,
                previous_row[j] + 1,
                previous_row[j - 1] + cost
            ))

            if two_rows_back is not None and j > 1 and prev_char is not None:
                if word[j - 1] == prev_char and word[j - 2] == char:
                    current_row[j] = min(current_row[j], two_rows_back[j - 2] + 1)

        return current_row
