class Wall:
    def __init__(self, length, height, brick_length, brick_height):
        self.length = length
        self.height = height
        self.brick_length = brick_length
        self.brick_height = brick_height
    
    def calculate_brick_count(self):
        bricks_per_row = self.length // self.brick_length
        rows = self.height // self.brick_height
        bricks_needed = bricks_per_row * rows
        return bricks_needed
    
wall1 = Wall(10, 3, 0.2, 0.1)
wall2 = Wall(8, 2.5, 0.25, 0.1)

print(f"The number of bricks needed for Wall 1 is {wall1.calculate_brick_count()}.")
print(f"The number of bricks needed for Wall 2 is {wall2.calculate_brick_count()}.")
