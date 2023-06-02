class RubiksCube:
    def __init__(self):
        # self.faces = {
        #     'U': ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
        #     'D': ['🟨', '🟨', '🟨', '🟨', '🟨', '🟨', '🟨', '🟨', '🟨'],
        #     'F': ['🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'],
        #     'B': ['🟧', '🟧', '🟧', '🟧', '🟧', '🟧', '🟧', '🟧', '🟧'],
        #     'L': ['🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩'],
        #     'R': ['🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦']
        # }
        self.faces = {
            'U': ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9'],
            'D': ['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9'],
            'L': ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9'],
            'R': ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9'],
            'F': ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9'],
            'B': ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
        }
        
    def display_cube(self):
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
        
    def display_cube2(self):
        mapping = {
            'w1': '⬜', 'w2': '⬜', 'w3': '⬜',
            'w4': '⬜', 'w5': '⬜', 'w6': '⬜',
            'w7': '⬜', 'w8': '⬜', 'w9': '⬜',
            'r1': '🟩', 'r2': '🟩', 'r3': '🟩',
            'r4': '🟩', 'r5': '🟩', 'r6': '🟩',
            'r7': '🟩', 'r8': '🟩', 'r9': '🟩',
            'g1': '🟥', 'g2': '🟥', 'g3': '🟥',
            'g4': '🟥', 'g5': '🟥', 'g6': '🟥',
            'g7': '🟥', 'g8': '🟥', 'g9': '🟥',
            'o1': '🟦', 'o2': '🟦', 'o3': '🟦',
            'o4': '🟦', 'o5': '🟦', 'o6': '🟦',
            'o7': '🟦', 'o8': '🟦', 'o9': '🟦',
            'b1': '🟧', 'b2': '🟧', 'b3': '🟧',
            'b4': '🟧', 'b5': '🟧', 'b6': '🟧',
            'b7': '🟧', 'b8': '🟧', 'b9': '🟧',
            'y1': '🟨', 'y2': '🟨', 'y3': '🟨',
            'y4': '🟨', 'y5': '🟨', 'y6': '🟨',
            'y7': '🟨', 'y8': '🟨', 'y9': '🟨'
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
        # Rotate the U face clockwise
        self.faces['U'] = [self.faces['U'][6], self.faces['U'][3], self.faces['U'][0],
                           self.faces['U'][7], self.faces['U'][4], self.faces['U'][1],
                           self.faces['U'][8], self.faces['U'][5], self.faces['U'][2]]

        # Update adjacent faces (L, F, R, B)
        self.faces['L'][0:3], self.faces['B'][0:3], self.faces['R'][0:3], self.faces['F'][0:3] = \
            self.faces['F'][0:3], self.faces['L'][0:3], self.faces['B'][0:3], self.faces['R'][0:3]
    
    def D(self):
        # Rotate the Down face clockwise
        self.faces['D'] = [self.faces['D'][6], self.faces['D'][3], self.faces['D'][0],
                           self.faces['D'][7], self.faces['D'][4], self.faces['D'][1],
                           self.faces['D'][8], self.faces['D'][5], self.faces['D'][2]]

        # Update adjacent faces (L, F, R, B)
        self.faces['L'][6:9], self.faces['B'][6:9], self.faces['R'][6:9], self.faces['F'][6:9] = \
            self.faces['B'][6:9], self.faces['R'][6:9], self.faces['F'][6:9], self.faces['L'][6:9]
            
    def L(self): 
        # Rotate the Left face clockwise
        self.faces['L'] = [self.faces['L'][6], self.faces['L'][3], self.faces['L'][0],
                           self.faces['L'][7], self.faces['L'][4], self.faces['L'][1],
                           self.faces['L'][8], self.faces['L'][5], self.faces['L'][2]]

        # Update adjacent faces (U, F, D, B)
        self.faces['U'][0:9:3], self.faces['F'][0:9:3], self.faces['D'][0:9:3], self.faces['B'][2:9:3] = \
            self.faces['B'][2:9:3], self.faces['U'][0:9:3], self.faces['F'][0:9:3], self.faces['D'][0:9:3]
            
    def R(self):
        # Rotate the Right face clockwise
        self.faces['R'] = [self.faces['R'][6], self.faces['R'][3], self.faces['R'][0],
                           self.faces['R'][7], self.faces['R'][4], self.faces['R'][1],
                           self.faces['R'][8], self.faces['R'][5], self.faces['R'][2]]

        # Update adjacent faces (U, F, D, B)
        self.faces['U'][2:9:3], self.faces['F'][2:9:3], self.faces['D'][2:9:3], self.faces['B'][0:9:3] = \
            self.faces['F'][2:9:3], self.faces['D'][2:9:3], self.faces['B'][0:9:3], self.faces['U'][2:9:3]

    def F(self):
        # Rotate the Front face clockwise
        self.faces['F'] = [self.faces['F'][6], self.faces['F'][3], self.faces['F'][0],
                           self.faces['F'][7], self.faces['F'][4], self.faces['F'][1],
                           self.faces['F'][8], self.faces['F'][5], self.faces['F'][2]]

        # Update adjacent faces (U, R, D, L)
        self.faces['U'][6:9], self.faces['R'][0:9:3], self.faces['D'][0:3], self.faces['L'][8:1:-3] = \
            self.faces['L'][8:1:-3], self.faces['U'][6:9], self.faces['R'][0:9:3][::-1], self.faces['D'][0:3][::-1]

    def B(self):
        # Rotate the Back face clockwise
        self.faces['B'] = [self.faces['B'][6], self.faces['B'][3], self.faces['B'][0],
                           self.faces['B'][7], self.faces['B'][4], self.faces['B'][1],
                           self.faces['B'][8], self.faces['B'][5], self.faces['B'][2]]

        # Update adjacent faces (U, R, D, L)
        self.faces['U'][0:3], self.faces['R'][2:9:3], self.faces['D'][6:9], self.faces['L'][0:9:3] = \
            self.faces['R'][2:9:3], self.faces['D'][6:9], self.faces['L'][0:9:3], self.faces['U'][0:3][::-1]

    """
    Slice Turns
    """
    def M(self):
        self.faces['F'][1:9:3], self.faces['U'][1:9:3], self.faces['B'][1:9:3], self.faces['D'][1:9:3] = \
            self.faces['U'][1:9:3], self.faces['B'][1:9:3], self.faces['D'][1:9:3], self.faces['F'][1:9:3]
    
    def E(self):
        self.faces['L'][3:6], self.faces['B'][3:6], self.faces['R'][3:6], self.faces['F'][3:6] = \
            self.faces['B'][3:6], self.faces['R'][3:6], self.faces['F'][3:6], self.faces['L'][3:6]
            
    def S(self):
        self.faces['U'][3:6], self.faces['R'][1:9:3], self.faces['D'][3:6], self.faces['L'][1:9:3] = \
            self.faces['L'][1:9:3][::-1], self.faces['U'][3:6], self.faces['R'][1:9:3][::-1], self.faces['D'][3:6]

    """
    Anti-clockwise Face Rotations
    """
    def Ui(self):
        [self.U() for _ in range(3)]
       
    def Di(self):
        [self.D() for _ in range(3)]
            
    def Li(self): 
        [self.L() for _ in range(3)]
            
    def Ri(self):
        [self.R() for _ in range(3)]

    def Fi(self):
        [self.F() for _ in range(3)]
        
    def Bi(self):
        [self.B() for _ in range(3)]

    """
    Anti-clockwise Slice Turns
    """
    def Mi(self):
        [self.M() for _ in range(3)]    
        
    def Ei(self):
        [self.E() for _ in range(3)]      
              
    def Si(self):
        [self.S() for _ in range(3)]
        
    def U2(self):
        [self.U() for _ in range(2)]
       
    def Di(self):
        [self.D() for _ in range(2)]
        
    """
    Double turns
    """            
    def L2(self): 
        [self.L() for _ in range(2)]
            
    def R2(self):
        [self.R() for _ in range(2)]

    def F2(self):
        [self.F() for _ in range(2)]
        
    def B2(self):
        [self.B() for _ in range(2)]
        
    def M2(self):
        [self.M() for _ in range(2)]    
        
    def E2(self):
        [self.E() for _ in range(2)]      
              
    def S2(self):
        [self.S() for _ in range(2)]
        

    """
    Double layer turns
    """        
    def u(self):
        self.U()
        self.Ei()
       
    def d(self):
        self.D()
        self.E()
            
    def l(self): 
        self.L()
        self.M()
            
    def r(self):
        self.R()
        self.Mi()

    def f(self):
        self.F()
        self.S()
        
    def b(self):
        self.B()
        self.Si()

    """
    Inverse double layer turns
    """     
    def ui(self):
        self.Ui()
        self.E()
       
    def di(self):
        self.Di()
        self.Ei()
            
    def li(self): 
        self.Li()
        self.Mi()
            
    def ri(self):
        self.Ri()
        self.M()

    def fi(self):
        self.Fi()
        self.Si()
        
    def bi(self):
        self.Bi()
        self.S()        

    """
    2x double layer turns
    """     
    def u2(self):
        [self.U() for _ in range(2)]
        [self.Ei() for _ in range(2)]
       
    def d2(self):
        [self.D() for _ in range(2)]
        [self.E() for _ in range(2)]
            
    def l2(self): 
        [self.L() for _ in range(2)]
        [self.M() for _ in range(2)]
            
    def r2(self):
        [self.R() for _ in range(2)]
        [self.Mi() for _ in range(2)]

    def f2(self):
        [self.F() for _ in range(2)]
        [self.S() for _ in range(2)]
        
    def b2(self):
        [self.B() for _ in range(2)]
        [self.Si() for _ in range(2)]       

    """
    Whole cube rotations
    """     
    def X(self):
        self.li()
        self.R()

    def Xi(self):
        self.l()
        self.Ri()
        
    def Y(self):
        self.u()
        self.Di()

    def Yi(self):
        self.ui()
        self.D()
        
    def Z(self):
        self.f()
        self.Bi()        
        
    def Zi(self):
        self.fi()
        self.B()

    """
    Double whole cube rotations
    """     
    def X2(self):
        [self.X() for _ in range(2)]
        
    def Y2(self):
        [self.Y() for _ in range(2)]
        
    def Z2(self):
        [self.Z() for _ in range(2)]     




if __name__ == "__main__":
    # Example usage:
    cube = RubiksCube()
    # cube.display_cube()
    # cube.S()
    cube.display_cube()
    cube.display_cube2()
    # cube.Ri()
    # cube.display_cube()
    

