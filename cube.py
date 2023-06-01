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
        for i in range(3):
            l_row = ' '.join(self.faces['L'][i*3:(i+1)*3])
            f_row = ' '.join(self.faces['F'][i*3:(i+1)*3])
            r_row = ' '.join(self.faces['R'][i*3:(i+1)*3])
            b_row = ' '.join(self.faces['B'][i*3:(i+1)*3])
            print(f'{l_row} {f_row} {r_row} {b_row}')

        # Display the Down face
        print('         ' + ' '.join(self.faces['D'][0:3]))
        print('         ' + ' '.join(self.faces['D'][3:6]))
        print('         ' + ' '.join(self.faces['D'][6:9]))

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
        self.faces['L'][0:3], self.faces['B'][0:3], self.faces['R'][0:3], self.faces['F'][0:3] = \
            self.faces['B'][0:3], self.faces['R'][0:3], self.faces['F'][0:3], self.faces['L'][0:3]
            
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



if __name__ == "__main__":
    # Example usage:
    cube = RubiksCube()
    # cube.display_cube()
    cube.B()
    cube.display_cube()
    # cube.Ri()
    # cube.display_cube()
    

