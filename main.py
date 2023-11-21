import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HEALTH = 3
TIMER = 5  # Время на ход в секундах

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting Game")

# Удары
UPPER = 'верхний'
MIDDLE = 'средний'
LOWER = 'нижний'
MOVES = [UPPER, MIDDLE, LOWER]

# Игрок
class Player:
    def init(self, color, position):
        self.health = HEALTH
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], 50, 50)  # Простой квадрат в качестве спрайта

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, move):
        # Простая анимация: меняем размер спрайта
        if move == UPPER:
            self.rect.inflate_ip(10, 0)
        elif move == MIDDLE:
            self.rect.inflate_ip(0, 10)
        elif move == LOWER:
            self.rect.inflate_ip(-10, 0)

# Выбор удара для компьютера
def choose_move_computer():
    return random.choice(MOVES)

# Разрешение раунда
def resolve_round(player1_move, player2_move, player1, player2):
    if player1_move == player2_move:
        player1.health -= 1
        player2.health -= 1
    elif (player1_move == UPPER and player2_move == MIDDLE) or \
         (player1_move == MIDDLE and player2_move == LOWER) or \
         (player1_move == LOWER and player2_move == UPPER):
        player2.health -= 1
    else:
        player1.health -= 1

# Игроки
player1 = Player(RED, (100, 300))
player2 = Player(BLUE, (650, 300))

# Игровой цикл
running = True
clock = pygame.time.Clock()
player1_move = None
player2_move = None
timer_start = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_move = UPPER
            elif event.key == pygame.K_DOWN:
                player1_move = LOWER
            elif event.key == pygame.K_LEFT:
                player1_move = MIDDLE

    # Логика таймера
    current_time = pygame.time.get_ticks()
    if player1_move and not player2_move:
        player2_move = choose_move_computer()
    if player1_move and player2_move and current_time - timer_start > TIMER * 1000:
        resolve_round(player1_move, player2_move, player1, player2)
        player1.update(player1_move)
        player2.update(player2_move)
        player1_move = None
        player2_move = None
        timer_start = current_time

    # Отрисовка
    screen.fill(BLACK)
    player1.draw()
    player2.draw()

    # Проверка победы
    if player1.health <= 0 or player2.health <= 0:
        running = False

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

# Завершение игры
pygame.quit()
sys.exit()
