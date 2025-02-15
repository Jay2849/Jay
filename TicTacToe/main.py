import pygame
import math
import pyttsx3

pygame.init()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Screen
WIDTH = 300
ROWS = 3
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Images
X_IMAGE = pygame.transform.scale(pygame.image.load("images/x.png"), (80, 80))
O_IMAGE = pygame.transform.scale(pygame.image.load("images/o.png"), (80, 80))

# Fonts
END_FONT = pygame.font.SysFont('arial', 40)

def draw_grid():
    gap = WIDTH // ROWS
    for i in range(ROWS):
        x = i * gap
        pygame.draw.line(win, GRAY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(win, GRAY, (0, x), (WIDTH, x), 3)

def initialize_grid():
    dis_to_cen = WIDTH // ROWS // 2
    game_array = [[None, None, None], [None, None, None], [None, None, None]]
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1)
            y = dis_to_cen * (2 * i + 1)
            game_array[i][j] = (x, y, "", True)
    return game_array

def click(game_array):
    global x_turn, o_turn, images
    m_x, m_y = pygame.mouse.get_pos()
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play = game_array[i][j]
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            if dis < WIDTH // ROWS // 2 and can_play:
                if x_turn:
                    images.append((x, y, X_IMAGE))
                    x_turn = False
                    o_turn = True
                    game_array[i][j] = (x, y, 'x', False)
                elif o_turn:
                    images.append((x, y, O_IMAGE))
                    x_turn = True
                    o_turn = False
                    game_array[i][j] = (x, y, 'o', False)

def has_won(game_array):
    for row in range(len(game_array)):
        if (game_array[row][0][2] == game_array[row][1][2] == game_array[row][2][2]) and game_array[row][0][2] != "":
            speak(game_array[row][0][2].upper() + " has won!")
            display_message(game_array[row][0][2].upper() + " has won!")
            return True

    for col in range(len(game_array)):
        if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2]) and game_array[0][col][2] != "":
            speak(game_array[0][col][2].upper() + " has won!")
            display_message(game_array[0][col][2].upper() + " has won!")
            return True

    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        speak(game_array[0][0][2].upper() + " has won!")
        display_message(game_array[0][0][2].upper() + " has won!")
        return True

    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        speak(game_array[0][2][2].upper() + " has won!")
        display_message(game_array[0][2][2].upper() + " has won!")
        return True

    return False

def has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False

    speak("It's a draw!")
    display_message("It's a draw!")
    return True

def speak(message):
    engine.say(message)
    engine.runAndWait()

def display_message(content):
    pygame.time.delay(500)
    win.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)

def render():
    win.fill(WHITE)
    draw_grid()
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))
    pygame.display.update()

def main():
    global x_turn, o_turn, images, draw
    images = []
    draw = False
    run = True
    x_turn = True
    o_turn = False
    game_array = initialize_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)

        render()

        if has_won(game_array) or has_drawn(game_array):
            run = False

while True:
    if __name__ == '__main__':
        main()