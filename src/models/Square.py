class Square:
    def __init__(self, a, b, c, d):
        square_points = [a, b, c, d]
        self.top_border = max(square_points, key=lambda p: p[0])
        self.bottom_border = min(square_points, key=lambda p: p[0])
        self.right_border = max(square_points, key=lambda p: p[1])
        self.left_border = min(square_points, key=lambda p: p[1])
