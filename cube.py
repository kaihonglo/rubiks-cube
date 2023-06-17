class RubiksCube:
    def __init__(self, initial_state = None, scramble = None):
        """
        Initializes a new Rubik's Cube object.

        Args:
            initial_state (str): Optional. A string representing the initial state of the cube.
                                 If not provided, a solved cube is created.
                                 The string should contain 9*6=54 characters representing the colors of each face.
                                 The characters should be in the order: U, D, L, R, F, B.
        """
        self.faces = {}
        if initial_state:
            # Split the string into sets of 9
            sets = [initial_state[i:i+9] for i in range(0, len(initial_state), 9)]

            # Update self.faces dictionary
            self.faces['U'] = list(sets[0])
            self.faces['D'] = list(sets[1])
            self.faces['L'] = list(sets[2])
            self.faces['R'] = list(sets[3])
            self.faces['F'] = list(sets[4])
            self.faces['B'] = list(sets[5])
        else:
            # Initialize with default solved cube configuration
            self.faces = {
                'U': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                'D': ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                'L': ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                'R': ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                'F': ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                'B': ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
            }
        
        if scramble:
            self.execute(scramble)
                       
    def display(self):
        """
        Displays the current state of the cube in a text-based format.
        """
        
        # Display the Up face   
        print('         ' + ' '.join(self.faces['U'][0:3]))
        print('         ' + ' '.join(self.faces['U'][3:6]))
        print('         ' + ' '.join(self.faces['U'][6:9]))

        # Display the Left, Front, and Right faces
        print(" ".join(self.faces['L'][0:3]) + " " + " ".join(self.faces['F'][0:3]) + " " + " ".join(self.faces['R'][0:3]) + " " + " ".join(self.faces['B'][0:3]))
        print(" ".join(self.faces['L'][3:6]) + " " + " ".join(self.faces['F'][3:6]) + " " + " ".join(self.faces['R'][3:6]) + " " + " ".join(self.faces['B'][3:6]))
        print(" ".join(self.faces['L'][6:9]) + " " + " ".join(self.faces['F'][6:9]) + " " + " ".join(self.faces['R'][6:9]) + " " + " ".join(self.faces['B'][6:9]))

        # Display the Down face
        print('         ' + ' '.join(self.faces['D'][0:3]))
        print('         ' + ' '.join(self.faces['D'][3:6]))
        print('         ' + ' '.join(self.faces['D'][6:9]))
        
    def display2(self):
        """
        Displays the current state of the cube using Unicode characters to represent the colors.
        """
        mapping = {
            'w1': '⬜', 'w2': '⬜', 'w3': '⬜',
            'w4': '⬜', 'w5': '⬜', 'w6': '⬜',
            'w7': '⬜', 'w8': '⬜', 'w9': '⬜',
            'r1': '🟥', 'r2': '🟥', 'r3': '🟥',
            'r4': '🟥', 'r5': '🟥', 'r6': '🟥',
            'r7': '🟥', 'r8': '🟥', 'r9': '🟥',
            'g1': '🟩', 'g2': '🟩', 'g3': '🟩',
            'g4': '🟩', 'g5': '🟩', 'g6': '🟩',
            'g7': '🟩', 'g8': '🟩', 'g9': '🟩',
            'o1': '🟧', 'o2': '🟧', 'o3': '🟧',
            'o4': '🟧', 'o5': '🟧', 'o6': '🟧',
            'o7': '🟧', 'o8': '🟧', 'o9': '🟧',
            'b1': '🟦', 'b2': '🟦', 'b3': '🟦',
            'b4': '🟦', 'b5': '🟦', 'b6': '🟦',
            'b7': '🟦', 'b8': '🟦', 'b9': '🟦',
            'y1': '🟨', 'y2': '🟨', 'y3': '🟨',
            'y4': '🟨', 'y5': '🟨', 'y6': '🟨',
            'y7': '🟨', 'y8': '🟨', 'y9': '🟨',
            'w': '⬜',
            'r': '🟥', 
            'g': '🟩', 
            'o': '🟧', 
            'b': '🟦', 
            'y': '🟨', 
        }

        # Display the Up face
        up_face = [mapping.get(pos, pos) for pos in self.faces['U']]
        print('         ' + ' '.join(up_face[0:3]))
        print('         ' + ' '.join(up_face[3:6]))
        print('         ' + ' '.join(up_face[6:9]))

        # Display the Left, Front, and Right faces
        print(" ".join([mapping.get(pos, pos) for pos in self.faces['L'][0:3]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['F'][0:3]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['R'][0:3]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['B'][0:3]]))
        print(" ".join([mapping.get(pos, pos) for pos in self.faces['L'][3:6]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['F'][3:6]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['R'][3:6]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['B'][3:6]]))
        print(" ".join([mapping.get(pos, pos) for pos in self.faces['L'][6:9]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['F'][6:9]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['R'][6:9]]) + " " +
            " ".join([mapping.get(pos, pos) for pos in self.faces['B'][6:9]]))
        
        # Display the Down face
        down_face = [mapping.get(pos, pos) for pos in self.faces['D']]
        print('         ' + ' '.join(down_face[0:3]))
        print('         ' + ' '.join(down_face[3:6]))
        print('         ' + ' '.join(down_face[6:9]))
        
    """
    Clockwise Face Rotations
    """
    def U(self):
        # Rotate the Up (U) face clockwise
        self.faces['U'] = [self.faces['U'][6], self.faces['U'][3], self.faces['U'][0],
                           self.faces['U'][7], self.faces['U'][4], self.faces['U'][1],
                           self.faces['U'][8], self.faces['U'][5], self.faces['U'][2]]

        # Update adjacent faces (L, F, R, B)
        self.faces['L'][0:3], self.faces['B'][0:3], self.faces['R'][0:3], self.faces['F'][0:3] = \
            self.faces['F'][0:3], self.faces['L'][0:3], self.faces['B'][0:3], self.faces['R'][0:3]
    
    def D(self):
        # Rotate the Down (D) face clockwise
        self.faces['D'] = [self.faces['D'][6], self.faces['D'][3], self.faces['D'][0],
                           self.faces['D'][7], self.faces['D'][4], self.faces['D'][1],
                           self.faces['D'][8], self.faces['D'][5], self.faces['D'][2]]

        # Update adjacent faces (L, F, R, B)
        self.faces['L'][6:9], self.faces['B'][6:9], self.faces['R'][6:9], self.faces['F'][6:9] = \
            self.faces['B'][6:9], self.faces['R'][6:9], self.faces['F'][6:9], self.faces['L'][6:9]
            
    def L(self): 
        # Rotate the Left (L) face clockwise
        self.faces['L'] = [self.faces['L'][6], self.faces['L'][3], self.faces['L'][0],
                           self.faces['L'][7], self.faces['L'][4], self.faces['L'][1],
                           self.faces['L'][8], self.faces['L'][5], self.faces['L'][2]]

        # Update adjacent faces (U, F, D, B)
        self.faces['U'][0:9:3], self.faces['F'][0:9:3], self.faces['D'][0:9:3], self.faces['B'][2:9:3] = \
            self.faces['B'][2:9:3][::-1], self.faces['U'][0:9:3], self.faces['F'][0:9:3], self.faces['D'][0:9:3][::-1]
            
    def R(self):
        # Rotate the Right (R) face clockwise
        self.faces['R'] = [self.faces['R'][6], self.faces['R'][3], self.faces['R'][0],
                           self.faces['R'][7], self.faces['R'][4], self.faces['R'][1],
                           self.faces['R'][8], self.faces['R'][5], self.faces['R'][2]]

        # Update adjacent faces (U, F, D, B)
        self.faces['U'][2:9:3], self.faces['F'][2:9:3], self.faces['D'][2:9:3], self.faces['B'][0:9:3] = \
            self.faces['F'][2:9:3], self.faces['D'][2:9:3], self.faces['B'][0:9:3][::-1], self.faces['U'][2:9:3][::-1]

    def F(self):
        # Rotate the Front (F) face clockwise
        self.faces['F'] = [self.faces['F'][6], self.faces['F'][3], self.faces['F'][0],
                           self.faces['F'][7], self.faces['F'][4], self.faces['F'][1],
                           self.faces['F'][8], self.faces['F'][5], self.faces['F'][2]]

        # Update adjacent faces (U, R, D, L)
        self.faces['U'][6:9], self.faces['R'][0:9:3], self.faces['D'][0:3], self.faces['L'][8:1:-3] = \
            self.faces['L'][8:1:-3], self.faces['U'][6:9], self.faces['R'][0:9:3][::-1], self.faces['D'][0:3][::-1]

    def B(self):
        # Rotate the Back (B) face clockwise
        self.faces['B'] = [self.faces['B'][6], self.faces['B'][3], self.faces['B'][0],
                           self.faces['B'][7], self.faces['B'][4], self.faces['B'][1],
                           self.faces['B'][8], self.faces['B'][5], self.faces['B'][2]]

        # Update adjacent faces (U, R, D, L)
        self.faces['U'][0:3], self.faces['R'][2:9:3], self.faces['D'][6:9], self.faces['L'][0:9:3] = \
            self.faces['R'][2:9:3], self.faces['D'][6:9][::-1], self.faces['L'][0:9:3], self.faces['U'][0:3][::-1]

    """
    Slice Turns
    """
    def M(self):
        # Rotates the middle slice of the cube clockwise (between L and R faces)
        self.faces['F'][1:9:3], self.faces['U'][1:9:3], self.faces['B'][1:9:3], self.faces['D'][1:9:3] = \
            self.faces['U'][1:9:3], self.faces['B'][1:9:3][::-1], self.faces['D'][1:9:3][::-1], self.faces['F'][1:9:3]
    
    def E(self):
        # Rotates the equatorial slice of the cube clockwise (between U and D faces)
        self.faces['L'][3:6], self.faces['B'][3:6], self.faces['R'][3:6], self.faces['F'][3:6] = \
            self.faces['B'][3:6], self.faces['R'][3:6], self.faces['F'][3:6], self.faces['L'][3:6]
            
    def S(self):
        # Rotates the standing slice of the cube clockwise (between F and B faces)
        self.faces['U'][3:6], self.faces['R'][1:9:3], self.faces['D'][3:6], self.faces['L'][1:9:3] = \
            self.faces['L'][1:9:3][::-1], self.faces['U'][3:6], self.faces['R'][1:9:3][::-1], self.faces['D'][3:6]

    """
    Anticlockwise Face Rotations
    """
    def Ui(self):
        # Rotate the Up (U) face anticlockwise
        [self.U() for _ in range(3)]
       
    def Di(self):
        # Rotate the Down (D) face anticlockwise
        [self.D() for _ in range(3)]
            
    def Li(self): 
        # Rotate the Left (L) face anticlockwise
        [self.L() for _ in range(3)]
            
    def Ri(self):
        # Rotate the Right (R) face anticlockwise
        [self.R() for _ in range(3)]

    def Fi(self):
        # Rotate the Face (F) face anticlockwise
        [self.F() for _ in range(3)]
        
    def Bi(self):
        # Rotate the Back (B) face anticlockwise
        [self.B() for _ in range(3)]

    """
    Anticlockwise Slice Turns
    """
    def Mi(self):
        # Rotates the middle slice of the cube anticlockwise (between L and R faces)
        [self.M() for _ in range(3)]    
        
    def Ei(self):
        # Rotates the equatorial slice of the cube anticlockwise (between U and D faces)
        [self.E() for _ in range(3)]      
              
    def Si(self):
        # Rotates the standing slice of the cube anticlockwise (between F and B faces)
        [self.S() for _ in range(3)]
        
    """
    Double turns
    """       
    def U2(self):
        # Rotate the Up (U) face twice
        [self.U() for _ in range(2)]
       
    def D2(self):
        # Rotate the Down (D) face twice
        [self.D() for _ in range(2)]
             
    def L2(self): 
        # Rotate the Left (L) face twice
        [self.L() for _ in range(2)]
            
    def R2(self):
        # Rotate the Right (R) face twice
        [self.R() for _ in range(2)]

    def F2(self):
        # Rotate the Front (F) face twice
        [self.F() for _ in range(2)]
        
    def B2(self):
        # Rotate the Back (B) face twice
        [self.B() for _ in range(2)]
        
    def M2(self):
        # Rotates the middle slice of the cube twice (between L and R faces)
        [self.M() for _ in range(2)]    
        
    def E2(self):
        # Rotates the equatorial slice of the cube twice (between U and D faces)
        [self.E() for _ in range(2)]      
              
    def S2(self):
        # Rotates the standing slice of the cube twice (between F and B faces)
        [self.S() for _ in range(2)]
        
    """
    Double layer turns
    """   
    def u(self):
        # Perform a clockwise double layer turn on the upper layer
        self.U()
        self.Ei()

    def d(self):
        # Perform a clockwise double layer turn on the lower layer
        self.D()
        self.E()

    def l(self): 
        # Perform a clockwise double layer turn on the left layer
        self.L()
        self.M()

    def r(self):
        # Perform a clockwise double layer turn on the right layer
        self.R()
        self.Mi()

    def f(self):
        # Perform a clockwise double layer turn on the front layer
        self.F()
        self.S()

    def b(self):
        # Perform a clockwise double layer turn on the back layer
        self.B()
        self.Si()

    """
    Inverse double layer turns
    """     
    def ui(self):
        # Perform an anticlockwise double layer turn on the upper layer
        self.Ui()
        self.E()

    def di(self):
        # Perform an anticlockwise double layer turn on the lower layer
        self.Di()
        self.Ei()

    def li(self): 
        # Perform an anticlockwise double layer turn on the left layer
        self.Li()
        self.Mi()

    def ri(self):
        # Perform an anticlockwise double layer turn on the right layer 
        self.Ri()
        self.M()

    def fi(self):
        # Perform an anticlockwise double layer turn on the front layer
        self.Fi()
        self.Si()

    def bi(self):
        # Perform an anticlockwise double layer turn on the back layer
        self.Bi()
        self.S()        

    """
    2x double layer turns
    """     
    def u2(self):
        # Perform a double layer turn twice on the upper layer
        [self.U() for _ in range(2)]
        [self.Ei() for _ in range(2)]

    def d2(self):
        # Perform a double layer turn twice on the lower layer
        [self.D() for _ in range(2)]
        [self.E() for _ in range(2)]

    def l2(self): 
        # Perform a double layer turn twice on the left layer
        [self.L() for _ in range(2)]
        [self.M() for _ in range(2)]

    def r2(self):
        # Perform a double layer turn twice on the right layer
        [self.R() for _ in range(2)]
        [self.Mi() for _ in range(2)]

    def f2(self):
        # Perform a double layer turn twice on the front layer
        [self.F() for _ in range(2)]
        [self.S() for _ in range(2)]

    def b2(self):
        # Perform a double layer turn twice on the back layer
        [self.B() for _ in range(2)]
        [self.Si() for _ in range(2)]

    """
    Whole cube rotations
    """     
    def x(self):
        # Perform a whole cube rotation following the R direction
        self.li()
        self.R()

    def xi(self):
        # Perform a whole cube rotation following the R' direction
        self.l()
        self.Ri()

    def y(self):
        # Perform a whole cube rotation following the U direction
        self.u()
        self.Di()

    def yi(self):
        # Perform a whole cube rotation following the U' direction
        self.ui()
        self.D()

    def z(self):
        # Perform a whole cube rotation following the F direction
        self.f()
        self.Bi()        

    def zi(self):
        # Perform a whole cube rotation following the F' direction
        self.fi()
        self.B()

    """
    Double whole cube rotations
    """     
    def x2(self):
        # Perform a double whole cube rotation following the R direction
        [self.x() for _ in range(2)]

    def y2(self):
        # Perform a double whole cube rotation following the U direction
        [self.y() for _ in range(2)]

    def z2(self):
        # Perform a double whole cube rotation following the F direction
        [self.z() for _ in range(2)]
         
    def get_edges(self):
        """
        Returns a dictionary mapping edge locations to their corresponding facelet positions.

        Returns:
            edge_locations (dict): Dictionary mapping edge locations to their corresponding facelet positions.
        """
        edge_locations = {
            'UF': (self.faces['U'][7], self.faces['F'][1]),
            'UR': (self.faces['U'][5], self.faces['R'][1]),
            'UB': (self.faces['U'][1], self.faces['B'][1]),
            'UL': (self.faces['U'][3], self.faces['L'][1]),
            'DF': (self.faces['D'][1], self.faces['F'][7]),
            'DR': (self.faces['D'][5], self.faces['R'][7]),
            'DB': (self.faces['D'][7], self.faces['B'][7]),
            'DL': (self.faces['D'][3], self.faces['L'][7]),
            'LF': (self.faces['L'][5], self.faces['F'][3]),
            'LB': (self.faces['L'][3], self.faces['B'][5]),
            'RF': (self.faces['R'][3], self.faces['F'][5]),
            'RB': (self.faces['R'][5], self.faces['B'][3])
        }
        return edge_locations
    
    def get_corners(self):
        """
        Returns a dictionary mapping corner locations to their corresponding facelet positions.

        Returns:
            corner_locations (dict): Dictionary mapping corner locations to their corresponding facelet positions.
        """
        corner_locations = {
            'UFR': (self.faces['U'][8], self.faces['F'][2], self.faces['R'][0]),
            'UFL': (self.faces['U'][6], self.faces['F'][0], self.faces['L'][2]),
            'UBR': (self.faces['U'][2], self.faces['B'][0], self.faces['R'][2]),
            'UBL': (self.faces['U'][0], self.faces['B'][2], self.faces['L'][0]),
            'DFR': (self.faces['D'][2], self.faces['F'][8], self.faces['R'][6]),
            'DFL': (self.faces['D'][0], self.faces['F'][6], self.faces['L'][8]),
            'DBR': (self.faces['D'][8], self.faces['B'][6], self.faces['R'][8]),
            'DBL': (self.faces['D'][6], self.faces['B'][8], self.faces['L'][6])
        }
        
        return corner_locations
        
    def execute(self, moves):
        """
        Executes a series of moves on the cube based on the provided move sequence.

        Args:
            moves (str): A sequence of moves to be executed on the cube.

        """
        moves = self.reformat_moves(moves)
        move_actions = {
            'F': self.F,
            'U': self.U,
            'R': self.R,
            'L': self.L,
            'B': self.B,
            'D': self.D,
            'f': self.f,
            'u': self.u,
            'r': self.r,
            'l': self.l,
            'b': self.b,
            'd': self.d,
            'M': self.M,
            'E': self.E,
            'S': self.S,
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }
        
        for i, move in enumerate(moves):
            if move == "i":
                action = move_actions.get(moves[i-1])
                action()
                action()
            elif move == "2":
                action = move_actions.get(moves[i-1])
                action()
            else:
                action = move_actions.get(move)
                action()
        
        # print()
        # cube.display2()
                    
    def reformat_moves(self, moves):
        """
        Reformats the move sequence by removing spaces and replacing "'" with "i" to represent inverse moves.

        Args:
            moves (str): The move sequence to be reformatted.

        Returns:
            reformatted (str): The reformatted move sequence.

        """
        reformatted = moves.replace(" ", "").replace("'", "i")
        return reformatted
    
    def get_state(self):
        """
        Retrieves the current state of the cube as a string by concatenating facelets of all faces.

        Returns:
            state (str): The current state of the cube.

        """
        return ''.join(''.join(self.faces[face]) for face in ['U', 'D', 'L', 'R', 'F', 'B'])
    
    def is_solved(self):
        """
        Checks if the cube is solved by verifying if all faces have only one unique color.

        Returns:
            is_solved (bool): True if the cube is solved, False otherwise.

        """
        return all(len(set(face)) == 1 for face in self.faces.values())

    
class Solver():
    """
    The Solver class provides methods to solve a Rubik's Cube using a layer-by-layer approach.
    It implements methods for solving the cross, first two layers (F2L), orientation of the last layer (OLL),
    and permutation of the last layer (PLL).

    Methods:
    - move_white_center_to_bottom(cube): Moves the white center piece to the bottom layer.
    - Cross(cube): Solves the cross on the bottom layer.
    - F2L(cube): Solves the first two layers of the Rubik's Cube.
    - OLL(cube): Orient the last layer.
    - PLL(cube): Permute the last layer.
    - solve(cube): Solves the Rubik's Cube using a layer-by-layer approach.

    """
    
    def __init__(self, cube, debug = 0):
        """
        Initializes a Solver object with a Rubik's Cube.

        Parameters:
        - cube (Cube): The Rubik's Cube object to solve.
        """
        self.DEBUG = debug
        self.cube = cube
        

    def move_white_center_to_bottom(self, cube):
        """
        Moves the white center piece to the bottom layer.

        Parameters:
        - cube (Cube): The Rubik's Cube object.

        This method finds the face of the white center piece and rotates the cube accordingly.

        Returns:
        None
        """
        
        # Find the face of the white center piece
        white_center_face = None
        for face, stickers in cube.faces.items():
            if 'w' in stickers[4]:
                white_center_face = face
                break

        # Rotate the cube according to the face of the white center piece
        switch = {
            'U': cube.x2,
            'D': lambda: None,  # No rotation needed
            'L': cube.zi,
            'R': cube.z,
            'F': cube.xi,
            'B': cube.x
        }

        # Call the corresponding function based on the white center face
        switch.get(white_center_face, lambda: None)()
        
    def Cross(self, cube):
        """
        Solves the cross on the bottom layer of the Rubik's Cube.

        Parameters:
        - cube (Cube): The Rubik's Cube object.

        This method solves the cross by finding the edge pieces with white and the face color,
        and executing the corresponding moves to position and orient them correctly.

        Returns:
        bool: True if the cross is solved, False otherwise.
        """
        
        self.move_white_center_to_bottom(cube)
        
        moves = {
            'UF': {'U':"F2", 'F':"Ui Ri F R"},
            'UR': {'U':"U F2", 'R':"Ri F R"},
            'UB': {'U':"U2 F2", 'B':"U Ri F R"},
            'UL': {'U':"Ui F2", 'L':"L Fi Li"},
            'DF': {'D':"", 'F':"F2 Ui Ri F R"},
            'DR': {'D':"R2 U F2", 'R':"R F"},
            'DB': {'D':"B2 U2 F2", 'B':"B2 U Ri F R"},
            'DL': {'D':"L2 Ui F2", 'L':"Li Fi"},
            'LF': {'L':"Fi", 'F':"F Ui Ri F R"},
            'LB': {'L':"Bi U2 B F2", 'B':"L Ui Li F2"},
            'RF': {'R':"F", 'F':"Fi Ui Ri F R"},
            'RB': {'R':"B U2 Bi F2", 'B':"Ri U R F2"},
        }
        
        for _ in range(4):
            edge_locations = cube.get_edges().items()

            # Accessing the locations
            current_face_colour = cube.faces['F'][4]
            
            for edge, location in edge_locations:
                if 'w' in location and current_face_colour in location:
                    if 'w' == location[0]:
                        white_at = edge[0]
                    else:
                        white_at = edge[1]
                        
                    break
            
            # if self.DEBUG: print("CROSS"); cube.display2(); print()
            
            cube.execute(moves[edge][white_at])

            
            cube.di()
            
        edges = {"L":{"sideCenter":cube.faces['L'][4], "sideEdge": cube.faces['L'][7], "botEdge": cube.faces['D'][3], "botCenter": cube.faces['D'][4], "adj":3},
                 "R":{"sideCenter":cube.faces['R'][4], "sideEdge": cube.faces['R'][7], "botEdge": cube.faces['D'][5], "botCenter": cube.faces['D'][4], "adj":5},
                 "F":{"sideCenter":cube.faces['F'][4], "sideEdge": cube.faces['F'][7], "botEdge": cube.faces['D'][1], "botCenter": cube.faces['D'][4], "adj":1},
                 "B":{"sideCenter":cube.faces['B'][4], "sideEdge": cube.faces['B'][7], "botEdge": cube.faces['D'][7], "botCenter": cube.faces['D'][4], "adj":7},
                }
        
        solved = all(face['botEdge'] == face['botCenter'] and face['sideEdge'] == face['sideCenter'] for face in edges.values())

        return solved
    
    def F2L(self, cube):
        """
        Solves the first two layers (F2L) of the Rubik's Cube.

        Parameters:
        - cube (Cube): The Rubik's Cube object.

        This method solves the first two layers by finding the corner and edge pieces with white and face colors,
        and executing the corresponding moves to position and orient them correctly.

        Returns:
        bool: True if the first two layers are solved, False otherwise.
        """
        
        # Solve DFR corner
        moves = {
            'UFR': {'U':"Fi U F Ui R Ui Ri", 'F':"U R Ui Ri", 'R':"R U Ri"},
            'UFL': {'U':"R U2 Ri U R Ui Ri", 'F':"Ui R U Ri", 'L':"R Ui Ri"},
            'UBR': {'U':"Fi U2 F R U Ri", 'B':"Fi U F", 'R':"U2 R Ui Ri"},
            'UBL': {'U':"R U Ri U R Ui Ri", 'B':"Ui R Ui Ri", 'L':"U Fi U F"},
            'DFR': {'D':"", 'F':"R Ui Ri U R Ui Ri", 'R':"R U Ri Ui R U Ri"},
            'DFL': {'D':"Li Ui L R U Ri", 'F':"Li U L Ui R U Ri", 'L':"Li Ui L U R Ui Ri"},
            'DBR': {'D':"B U Bi U R Ui Ri", 'B':"B U Bi R U Ri", 'R':"Ri U2 R R Ui Ri"},
            'DBL': {'D':"Bi Ui B Ui R U Ri", 'B':"Bi Ui B R Ui Ri", 'L':"L U2 Li R U Ri"},
        }
        
        for _ in range(4):
            corner_locations = cube.get_corners().items()  

            # Accessing the locations
            current_face_colour = cube.faces['F'][4]
            current_right_colour = cube.faces['R'][4]
            
            for corner, location in corner_locations:
                if 'w' in location and current_face_colour in location and current_right_colour in location:
                    if 'w' == location[0]:
                        white_at = corner[0]
                    elif 'w' == location[1]:
                        white_at = corner[1]
                    else:
                        white_at = corner[2]
                        
                    break
            
            if self.DEBUG: print("First Layer"); cube.display2(); print()
            
            cube.execute(moves[corner][white_at])
            
            cube.di()
        
        first_layer_solved = len(set(cube.faces['D'])) == 1 and all(cube.faces[face][i] == cube.faces[face][4] for face in ['L', 'F', 'R', 'B'] for i in range(6,9))
        
        # Solve FR edge
        moves = {
            'UF': {'U':"y Ui Ui Li U L U F Ui Fi yi", 'F':"U R Ui Ri Ui Fi U F"},
            'UR': {'U':"y Ui Li U L U F Ui Fi yi", 'R':"U U R Ui Ri Ui Fi U F"},
            'UB': {'U':"y Li U L U F Ui Fi yi", 'B':"Ui R Ui Ri Ui Fi U F"},
            'UL': {'U':"y U Li U L U F Ui Fi yi", 'L':"R Ui Ri Ui Fi U F"},
            'LF': {'L':"Li U L U F Ui Fi Ui R Ui Ri Ui Fi U F", 'F':"Li U L U F Ui Fi y Li U L U F Ui Fi yi"},
            'LB': {'L':"d Li U L U F Ui Fi di y Li U L U F Ui Fi yi", 'B':"d Li U L U F Ui Fi di Ui R Ui Ri Ui Fi U F"},
            'RF': {'R':"R Ui Ri Ui Fi U F Ui R Ui Ri Ui Fi U F", 'F':""},
            'RB': {'R':"y R Ui Ri Ui Fi U F U Li U L U F Ui Fi yi", 'B':"y R Ui Ri Ui Fi U F yi R Ui Ri Ui Fi U F"},
        }
        
        for _ in range(4):
            edge_locations = cube.get_edges().items()

            # Accessing the locations
            current_face_colour = cube.faces['F'][4]
            current_right_colour = cube.faces['R'][4]
            
            for edge, location in edge_locations:
                if current_face_colour in location and current_right_colour in location:
                    if current_face_colour == location[0]:
                        face_colour_at = edge[0]
                    else:
                        face_colour_at = edge[1]
                        
                    break
            
            if self.DEBUG: print("Second Layer"); cube.display2(); print()
            cube.execute(moves[edge][face_colour_at])
            
            cube.di()
        
        solved = len(set(cube.faces['D'])) == 1 and all(cube.faces[face][i] == cube.faces[face][4] for face in ['L', 'F', 'R', 'B'] for i in range(3,9))
        return solved

    
    def OLL(self, cube):
        """
        Solves the orientation of the last layer (2 look OLL) of the Rubik's Cube.

        Parameters:
        - cube (Cube): The Rubik's Cube object.

        This method solves the orientation of the last layer by executing the appropriate algorithm based on
        the pattern of the edges and corners on the top layer.

        Returns:
        bool: True if the orientation of the last layer is solved, False otherwise.
        """

        # Solve edge
        move = "F R U Ri Ui Fi f R U Ri Ui fi"
        for _ in range(4):
            if all(cube.faces['U'][i] == cube.faces['U'][4] for i in range(1,9,2)):
                move = ""
                break
            elif all(cube.faces['U'][i] == cube.faces['U'][4] for i in range(3,6,2)):
                move = "F R U Ri Ui Fi"
                break
            elif all(cube.faces['U'][i] == cube.faces['U'][4] for i in range(5,9,2)):
                move = "f R U Ri Ui fi"
                break
            
            cube.U()
        
        if self.DEBUG: print("OLL 1"); cube.display2(); print()
        cube.execute(move)
            
        
        
        # Solve corner
        move = ""
        for _ in range(4):
            if all(cube.faces['U'][i] == cube.faces['U'][4] for i in range(1,9)):
                move = ""
                break
            elif cube.faces['U'][2] == cube.faces['U'][4] and cube.faces['L'][0] == cube.faces['U'][4] and \
                cube.faces['F'][0] == cube.faces['U'][4] and cube.faces['R'][0] == cube.faces['U'][4]:
                move = "R U2 Ri Ui R Ui Ri"
                break
            elif cube.faces['U'][0] == cube.faces['U'][4] and cube.faces['L'][2] == cube.faces['U'][4] and \
                cube.faces['F'][2] == cube.faces['U'][4] and cube.faces['R'][2] == cube.faces['U'][4]:
                move = "Li U2 L U Li U L"
                break
            elif cube.faces['L'][0] == cube.faces['U'][4] and cube.faces['L'][2] == cube.faces['U'][4] and \
                cube.faces['R'][0] == cube.faces['U'][4] and cube.faces['R'][2] == cube.faces['U'][4]:
                move = "R U Ri U R Ui Ri U R U2 Ri"
                break
            elif cube.faces['U'][0] == cube.faces['U'][4] and cube.faces['U'][8] == cube.faces['U'][4] and \
                cube.faces['F'][0] == cube.faces['U'][4] and cube.faces['R'][2] == cube.faces['U'][4]:
                move = "F Ri Fi r U R Ui ri"
                break
            elif cube.faces['L'][0] == cube.faces['U'][4] and cube.faces['L'][2] == cube.faces['U'][4] and \
                cube.faces['F'][2] == cube.faces['U'][4] and cube.faces['B'][0] == cube.faces['U'][4]:
                move = "R U2 R2 Ui R2 Ui R2 U2 R"
                break
            elif cube.faces['U'][2] == cube.faces['U'][4] and cube.faces['U'][8] == cube.faces['U'][4] and \
                cube.faces['F'][0] == cube.faces['U'][4] and cube.faces['B'][2] == cube.faces['U'][4]:
                move = "r U Ri Ui ri F R Fi"
                break
            elif cube.faces['U'][0] == cube.faces['U'][4] and cube.faces['U'][6] == cube.faces['U'][4] and \
                cube.faces['R'][0] == cube.faces['U'][4] and cube.faces['R'][2] == cube.faces['U'][4]:
                move = "R U2 Ri Ui R Ui Ri Li U2 L U Li U L"
                break
            
            cube.U()
        
        if self.DEBUG: print("OLL 2"); cube.display2(); print()
        cube.execute(move)
        
        return len(set(cube.faces['U'])) == 1 and len(set(cube.faces['D'])) == 1 and all(cube.faces[face][i] == cube.faces[face][4] for face in ['L', 'F', 'R', 'B'] for i in range(3,9))
        
    def PLL(self, cube):
        """
        Solves the permutation of the last layer (2 Look PLL) of the Rubik's Cube.

        Parameters:
        - cube (Cube): The Rubik's Cube object.

        This method solves the permutation of the last layer by executing the appropriate algorithm based on
        the pattern of the edges and corners on the top layer.

        Returns:
        bool: True if the permutation of the last layer is solved, False otherwise.
        """
        
        # Solve corner
        same_corners_at_face = sum(cube.faces[face][0] == cube.faces[face][2] for face in ['L', 'F', 'R', 'B'])
        
        if self.DEBUG: print("PLL 1"); cube.display2(); print()
        
        if same_corners_at_face == 0:
            cube.execute("F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi")
        elif same_corners_at_face == 1:
            for _ in range(3):
                if cube.faces['L'][0] == cube.faces['L'][2]:
                    break
                cube.U()
            
            cube.execute("R U Ri Ui Ri F R2 Ui Ri Ui R U Ri Fi")
        else:
            pass
            
        for _ in range(3):
            if all(cube.faces[face][i] == cube.faces[face][4] for face in ['L', 'F', 'R', 'B'] for i in [0,2]):
                break
            cube.U()
            
        # Solve edge
        solved_edges = sum(cube.faces[face][0] == cube.faces[face][1] for face in ['L', 'F', 'R', 'B'])
        
        if self.DEBUG: print("PLL 2"); cube.display2(); print()

        if solved_edges == 0:    
            if cube.faces['F'][1] == cube.faces['B'][0]:
                cube.execute("M2 Ui M2 U2 M2 Ui M2")
            else:
                if cube.faces['F'][1] != cube.faces['R'][4]:
                    cube.y()
                cube.execute("Mi Ui M2 Ui M2 Ui Mi U2 M2")
        elif solved_edges == 1:
            for _ in range(3):
                if cube.faces['B'][0] == cube.faces['B'][1]:
                    break
                cube.U()
                
            if cube.faces['F'][1] == cube.faces['R'][0]:
                cube.execute("R Ui R U R U R Ui Ri Ui R2")
            else:
                cube.execute("R2 U R U Ri Ui Ri Ui Ri U Ri")
        else:
            pass
        
        for _ in range(3):
            if all(cube.faces[face][i] == cube.faces[face][4] for face in ['L', 'F', 'R', 'B'] for i in range(0,3)):
                break
            cube.U()
        
        return cube.is_solved()
    
    def solve(self,cube,display = False):
        """
        Solves the Rubik's Cube using the CFOP method.

        Parameters:
        - cube (Cube): The Rubik's Cube object.

        This method solves the Rubik's Cube by invoking the Cross, F2L, OLL, and PLL methods
        in the appropriate order until the cube is completely solved.

        Returns:
        bool: True if the Rubik's Cube is solved, False otherwise.
        """
        
        if display: cube.display2()
        
        c = self.Cross(cube)
        if display: 
            cube.display2()
            print("Cross Solved: ", c)
            print()
        
        f = self.F2L(cube)
        if display: 
            cube.display2()
            print("F2L Solved: ", f)
            print()
        
        o = self.OLL(cube)
        if display: 
            cube.display2()
            print("OLL Solved: ", o)
            print()
        
        p = self.PLL(cube)
        if display: 
            cube.display2()
            print("PLL Solved: ", p)
            print()
        
        return c,f,o,p
        
    
import random
class Tester:
    def __init__(self):
        self.scrambles = [
                        "R U R' U R U2 R' U' R U' R' U' R U R' U R U2 R' U'",
                        "F' L F L' F' L F L' F' L F L' F' L F L'",
                        "y R U R' U R U' R' U R U R' U R U2 R' U' y'",
                        "x' R U R' U R U' R' U R U R' U R U2 R' U' x",
                        "z D' R' D R D' R' D R D' R' D R D' R' D R z'",
                        "U R U' R' U R U' R' U R U' R' U R U' R' U R U' R' U",
                        "F U R U' R' F' R U R' U' R' F R F'",
                        "R U R' U R U2 R' U' R U' R' U' R U R' U R U2 R' U'",
                        "U' R U2 R' U' R U2 R' U' R U2 R' U' R U2 R'",
                        "L' U' L U' L' U2 L U L' U L U L' U2 L U'",
                        "x R U R' U' x' R U R' U' R' F R F'",
                        "z D' R U' R' D R U R' D' R U R' D R U' R' z'",
                        "U R U R' U' R' U' R U' R' U R U R2 U2 R' U'",
                        "R U2 R' U' R U' R' U R U R' U' R U' R'",
                        "F R U R' U' F' R U R' U' R' F R F'",
                        "L F' L' U' L U F U' L' U L F' L' F",
                        "R U2 R' U' R U R' U2 R U' R' U' R U2 R' U'",
                        "D R' U' R D' R' U' R D R' U' R D' R' U R D",
                        "y x' R U R' U' R U R' U' R U R' U' R U R' x y'",
                        "F R U R' U' F' U R U' R'"
                    ]
        


    def generate_scrambles(self, num_scrambles):
        moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2",
                "F", "F'", "F2", "B", "B'", "B2", "M", "M'", "M2", "E", "E'", "E2",
                "S", "S'", "S2", "x", "x'", "x2", "y", "y'", "y2", "z", "z'", "z2"]
        scrambles = []

        for _ in range(num_scrambles):
            scramble_length = random.randint(20, 30)
            scramble = ""

            for _ in range(scramble_length):
                move = random.choice(moves)
                scramble += move + " "

            scrambles.append(scramble.strip())

        return scrambles
    
    def test_solver(self, n_test = 10, debug = 0):
        self.scrambles = self.generate_scrambles(n_test)
        total_tests = len(self.scrambles)
        tests_passed = 0
        
        for i, scramble in enumerate(self.scrambles, 1):
            
            cube = RubiksCube(scramble=scramble)
            initial_state = cube.get_state()
            
            solver = Solver(cube)
            c,f,o,p = solver.solve(cube)
            final_state = cube.get_state()
            
            solved = cube.is_solved()
            status = "PASS" if solved else "FAILED"
            
            
            if solved:
                tests_passed += 1
            else:
                if debug >= 1: 
                    print(f"Testing scramble {i}: {scramble}      ({status})")
                    print(f"C-{c}   F-{f}   O-{o}   P-{p}")
                    if debug == 2:
                        print("Initial State: ")
                        RubiksCube(initial_state=initial_state).display2()
                        print()
                        print("Final State: ")
                        RubiksCube(initial_state=final_state).display2()
            
            
                print()
            
        print(f"Tests ran: {total_tests}, Passed: {tests_passed}, Failed: {total_tests - tests_passed}")
            
                
            
            
            
            

if __name__ == "__main__":
    pass
    cube = RubiksCube()
    cube.execute("")
    # cube.execute("")
    
    # cube.display()
    # cube.display2()
    # print()
    
    # solver = Solver(cube, debug = 1)
    # solver.Cross(cube)
    # # cube.display2()
    # # print()
    # solver.F2L(cube)
    # # cube.display2()
    # # print()
    # solver.OLL(cube)
    # # cube.display2()
    # # print()
    # solver.PLL(cube)
    # print("FINAL")
    # cube.display2()
    # print()
    
    
    tester = Tester()
    tester.test_solver(n_test = 100, debug=1)



    

    

