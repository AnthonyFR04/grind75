class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        orig_color = image[sr][sc]

        def flood(image: list[list[int]], sr: int, sc: int, orig_color: int, new_color: int) -> list[list[int]]:
            if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != orig_color):
                return

            image[sr][sc] = new_color

            flood(image, sr + 1, sc, orig_color, new_color)
            flood(image, sr - 1, sc, orig_color, new_color)
            flood(image, sr, sc + 1, orig_color, new_color)
            flood(image, sr, sc - 1, orig_color, new_color)
        
        flood(image, sr, sc, orig_color, color)

        return image