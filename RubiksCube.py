# class requires declaration of row and column dimensions
class RubiksCube3DArray:
    def __init__(self, rows=3, columns=3, custom_cube=None):
        """Creates a Rubik's Cube of desired dimensions, or allows to pass in a scrambled state."""
        self.rows = rows
        self.columns = columns
        
        # if condition to check if user wants to pass in scrambled state for custom cube
        if custom_cube:
            self.cube = custom_cube
        else:
            # Initialize cube with 6 faces, resized based on number of rows/columns
            self.cube = [
                [[0] * columns for _ in range(rows)],  # Top (White)
                [[1] * columns for _ in range(rows)],  # Left (Green)
                [[2] * columns for _ in range(rows)],  # Front (Red)
                [[3] * columns for _ in range(rows)],  # Right (Blue)
                [[4] * columns for _ in range(rows)],  # Back (Orange)
                [[5] * columns for _ in range(rows)]   # Bottom (Yellow)
            ]

    # Prints the current state of the 3D array-based cube using enumerate
    def display(self):
        faces = ['Top', 'Left', 'Front', 'Right', 'Back', 'Bottom']
        for idx, face in enumerate(faces):
            print(f"{face}:")
            for row in self.cube[idx]:
                print(row)
            print()

    # Rotates a face 90 degrees clockwise.
    def rotate_face_clockwise(self, face_idx):
        self.cube[face_idx] = [list(x) for x in zip(*reversed(self.cube[face_idx]))]
    # Rotates a face 90 degrees counterclockwise.
    def rotate_face_counter_clockwise(self, face_idx):
        """Rotates a face 90 degrees counterclockwise."""
        self.cube[face_idx] = [list(x) for x in zip(*self.cube[face_idx])][::-1]

    # Performs a horizontal twist on the specified row (0 = left, rows-1 = right).
    # Direction (0 = right/clockwise, 1 = left/counterclockwise)
    def horizontal_twist(self, row, direction):
        if row < self.rows:
            if direction == 0:  # Twist right
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (
                    self.cube[2][row], self.cube[3][row], self.cube[4][row], self.cube[1][row])

            elif direction == 1:  # Twist left
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (
                    self.cube[4][row], self.cube[1][row], self.cube[2][row], self.cube[3][row])

            else:
                print(f'Choose a direction to be either 0 (right) or 1 (left)')
                return

            # Rotating top or bottom face
            if direction == 0:  # Twist left
                if row == 0:
                    self.rotate_face_counter_clockwise(0)
                elif row == self.rows - 1:
                    self.rotate_face_counter_clockwise(5)
            elif direction == 1:  # Twist right
                if row == 0:
                    self.rotate_face_clockwise(0)
                elif row == self.rows - 1:
                    self.rotate_face_clockwise(5)
        else:
            print(f'Please select a row between 0 and {self.rows - 1}')
            return
        
    # Performs a vertical twist on the specified column (0 = left, columns-1 = right).
    # Direction (0 = up, 1 = down)
    def vertical_twist(self, col, direction):
        if 0 <= col < self.columns:
            temp = [self.cube[0][i][col] for i in range(self.rows)]  # Store top face column

            if direction == 0:  # Twist up
                for i in range(self.rows):
                    # Move values up in the columns
                    self.cube[0][i][col], self.cube[2][i][col], self.cube[5][i][col], self.cube[4][self.rows - 1 - i][col] = (
                        self.cube[2][i][col], self.cube[5][i][col], self.cube[4][self.rows - 1 - i][col], temp[i])

                # Rotate Left or Right face
                if col == 0:
                    self.rotate_face_counter_clockwise(1)  # Left face
                elif col == self.columns - 1:
                    self.rotate_face_clockwise(3)  # Right face

            elif direction == 1:  # Twist down
                for i in range(self.rows):
                    # Move values down in the columns
                    self.cube[0][i][col], self.cube[2][i][col], self.cube[5][i][col], self.cube[4][i][col] = (
                        self.cube[4][i][col], temp[i], self.cube[2][i][col], self.cube[5][i][col])
            
                # Rotate Left or Right face
                if col == 0:
                    self.rotate_face_clockwise(1)  # Left face
                elif col == self.columns - 1:
                    self.rotate_face_counter_clockwise(3)  # Right face
            else:
                print(f'Choose a direction to be either 0 (up) or 1 (down)')
                return
        else:
            print(f'Choose a column between 0 and {self.columns - 1}.')


