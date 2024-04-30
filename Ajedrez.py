import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ajedrez")
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ajedrez para locos")
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 60)
timer = pygame.time.Clock()
fps = 60
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', #fila 1
                 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] #fila 2
white_locations =[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', #fila 8
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] #fila 7
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), #diferente al de white
                 (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
turn_step = 0
selection = 100
valid_moves = []
black_queen = pygame.image.load('./images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('./images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('./images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('./images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('./images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('./images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('./images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('./images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('./images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('./images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('./images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('./images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))


white_images = [white_pawn,white_queen,white_king,white_knight,white_rook,white_bishop]
white_images = [white_pawn_small,white_queen_small,white_king_small,white_knight_small,white_rook_small,white_bishop_small]

black_images = [black_pawn,black_queen,black_king,black_knight,black_rook,black_bishop]
black_images = [black_pawn_small,black_queen_small,black_king_small,black_knight_small,black_rook_small,black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

counter = 0
winner = ''
game_over = False

#dibujar tablero
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            if column % 2 == 0:
                pygame.draw.rect(screen,'light gary',[600-(column* 200),row*100,100,100])
            else:
                pygame.draw.rect(screen,'light gary',[700-(column* 200),row*100,100,100])
            pygame.draw.rect(screen,'gray',[0,800,width,100])
            pygame.draw.rect(screen,'gold',[0,800,width,100],5)
            pygame.draw.rect(screen,'gold',[800,0,100,height],5)
            status_text = ['White: Selecciona una pieza para mover', 'White: Selecciona el destino',
                           'Black: Selecciona una pieza para mover', 'Black: Selecciona el destino']
            screen.blit(big_font.render(
                status_text[turn_step], True, 'black'), (20, 820))    
            for i in range(9):
                pygame.draw.line(screen, 'black', (0,100 * i), (800,100*1), 2)
                pygame.draw.line(screen, 'black', (100*i,0), (100*i ,800), 2)
            screen.blit(medium_font('Perder',True,'Black' )(810, 830))
#Traer las piezas al tablero
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0]* 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', (white_locations[i][0] * 100+1, white_locations[i][1] * 100 + 1,100,100), 5)
#--------black
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (black_locations[i][0]* 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', (black_locations[i][0] * 100+1, black_locations[i][1] * 100 + 1,100,100), 5)

#chequear que las pieza tengas opciones validas en el tablero
def check_options(pieces,locations,turn):
    moves_list = []
    all_moves = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location,turn)
        elif piece == 'rook':
            moves_list = check_rook(location,turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location,turn)
        elif piece == 'queen':
            moves_list = check_queen(location,turn)
        elif piece == 'king':
            moves_list = check_king(location,turn)
        elif piece == 'knight':
            moves_list = check_knight(location,turn)
        all_moves.append(moves_list)
    return all_moves

  #controlar el king
def check_king(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    targets = [(1,0),(1,1),(1,-1),(-1,0),
                (-1,1),(-1,-1),(0,1),(0,-1)]
    for i in range(8):
        target = (position[0] + targets[i][0],position[1] + targets[i][1])
        if target not in friends_list and target[0] >= 0 and target[0] <= 7 and target[1] >= 0 and target[1] <= 7:
            moves_list.append(target)
    return moves_list

def queen_check(position,color):
    moves_list = check_bishop(position,color)
    second_list = check_rook(position,color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list
#alfil
def check_bishop(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x=1
            y=-1
        elif i == 1:
            x=-1
            y=-1
        elif i == 2:
            x=1
            y=1
        else:
            x=-1
            y=1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                    chain += 1
            else:
                path = False
    return moves_list

   
