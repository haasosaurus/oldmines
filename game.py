import random
import pygame
from constants import *


class Game(object):
    def __init__(self):

        # set game state variable
        self.state = MENU

        # pygame variables
        self.screen = None
        self.clock = None

        # game variables
        self.game_loop_done = False
        self.difficulty = EASY
        self.game_in_progress = False
        self.columns = 10
        self.rows = 10
        self.box_width = 20
        self.box_height = 20
        self.box_margin = 5
        self.screen_width = 255
        self.screen_height = 255
        self.mine_image = None
        self.flag_image = None

        # set up initial grid
        self.grid = []
        self.grid_visibility = []
        self.set_grid()

        # set game over variables
        self.game_over = False

        # exit game variable
        self.exiting_game = False

        # menu variables
        self.menu_select = 0
        self.difficulty_menu_select = 0

        # initialize mouse press bools
        self.left_mouse_pressed = False
        self.middle_mouse_pressed = False
        self.right_mouse_pressed = False

        # save last frame's mouse position
        self.left_mouse_last_frame = False
        self.middle_mouse_last_frame = False
        self.right_mouse_last_frame = False

        # initialize mouse click bools
        self.left_mouse_click = False
        self.middle_mouse_click = False
        self.right_mouse_click = False

        # initialize key press bools
        self.esc_pressed = False
        self.space_pressed = False
        self.return_pressed = False
        self.lshift_pressed = False
        self.minus_pressed = False
        self.equals_pressed = False
        self.up_pressed = False
        self.left_pressed = False
        self.down_pressed = False
        self.right_pressed = False
        self.w_pressed = False
        self.a_pressed = False
        self.s_pressed = False
        self.d_pressed = False
        self.p_pressed = False
        self.q_pressed = False
        self.r_pressed = False
        self.k1_pressed = False
        self.k2_pressed = False
        self.k3_pressed = False
        self.k4_pressed = False
        self.k5_pressed = False

        # keys last frame
        self.esc_last_frame = False
        self.space_last_frame = False
        self.return_last_frame = False
        self.lshift_last_frame = False
        self.minus_last_frame = False
        self.equals_last_frame = False
        self.up_last_frame = False
        self.left_last_frame = False
        self.down_last_frame = False
        self.right_last_frame = False
        self.w_last_frame = False
        self.a_last_frame = False
        self.s_last_frame = False
        self.d_last_frame = False
        self.p_last_frame = False
        self.q_last_frame = False
        self.r_last_frame = False
        self.k1_last_frame = False
        self.k2_last_frame = False
        self.k3_last_frame = False
        self.k4_last_frame = False
        self.k5_last_frame = False

        # complete keystrokes no looping
        self.esc_keystroke = False
        self.space_keystroke = False
        self.return_keystroke = False
        self.lshift_keystroke = False
        self.minus_keystroke = False
        self.equals_keystroke = False
        self.up_keystroke = False
        self.left_keystroke = False
        self.down_keystroke = False
        self.right_keystroke = False
        self.w_keystroke = False
        self.a_keystroke = False
        self.s_keystroke = False
        self.d_keystroke = False
        self.p_keystroke = False
        self.q_keystroke = False
        self.r_keystroke = False
        self.k1_keystroke = False
        self.k2_keystroke = False
        self.k3_keystroke = False
        self.k4_keystroke = False
        self.k5_keystroke = False

    def process_events(self):
        """ process all game events, return true if we need to close the window """

        # complete mouse clicks with no looping
        self.left_mouse_click = False
        self.middle_mouse_click = False
        self.right_mouse_click = False

        # complete keystrokes no looping
        self.esc_keystroke = False
        self.space_keystroke = False
        self.return_keystroke = False
        self.lshift_keystroke = False
        self.minus_keystroke = False
        self.equals_keystroke = False
        self.up_keystroke = False
        self.left_keystroke = False
        self.down_keystroke = False
        self.right_keystroke = False
        self.w_keystroke = False
        self.a_keystroke = False
        self.s_keystroke = False
        self.d_keystroke = False
        self.p_keystroke = False
        self.q_keystroke = False
        self.r_keystroke = False
        self.k1_keystroke = False
        self.k2_keystroke = False
        self.k3_keystroke = False
        self.k4_keystroke = False
        self.k5_keystroke = False

        # process events
        for event in pygame.event.get():

            # quit on close window
            if event.type == pygame.QUIT:
                self.exiting_game = True

            # press mouse buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # left mouse button
                if event.button == 1:
                    self.left_mouse_pressed = True
                    if not self.left_mouse_last_frame:
                        self.left_mouse_click = True

                # middle mouse button
                elif event.button == 2:
                    self.middle_mouse_pressed = True
                    if not self.middle_mouse_last_frame:
                        self.middle_mouse_click = True

                # right mouse button
                elif event.button == 3:
                    self.right_mouse_pressed = True
                    if not self.right_mouse_last_frame:
                        self.right_mouse_click = True

            # release mouse buttons
            elif event.type == pygame.MOUSEBUTTONUP:

                # left mouse button
                if event.button == 1:
                    self.left_mouse_pressed = False

                # middle mouse button
                elif event.button == 2:
                    self.middle_mouse_pressed = False

                # right mouse button
                elif event.button == 3:
                    self.right_mouse_pressed = False

            # press keys
            elif event.type == pygame.KEYDOWN:

                # esc
                if event.key == pygame.K_ESCAPE:
                    if not self.esc_last_frame:
                        self.esc_keystroke = True

                # space
                elif event.key == pygame.K_SPACE:
                    self.space_pressed = True
                    if not self.space_last_frame:
                        self.space_keystroke = True

                # return
                elif event.key == pygame.K_RETURN:
                    self.return_pressed = True
                    if not self.return_last_frame:
                        self.return_keystroke = True

                # lshift
                elif event.key == pygame.K_LSHIFT:
                    self.lshift_pressed = True
                    if not self.lshift_last_frame:
                        self.lshift_keystroke = True
                    else:
                        self.lshift_keystroke = False

                # minus
                elif event.key == pygame.K_MINUS:
                    self.minus_pressed = True
                    if not self.minus_last_frame:
                        self.minus_keystroke = True

                # equals
                elif event.key == pygame.K_EQUALS:
                    self.equals_pressed = True
                    if not self.equals_last_frame:
                        self.equals_keystroke = True

                # up
                elif event.key == pygame.K_UP:
                    self.up_pressed = True
                    if not self.up_last_frame:
                        self.up_keystroke = True

                # left
                elif event.key == pygame.K_LEFT:
                    self.left_pressed = True
                    if not self.left_last_frame:
                        self.left_keystroke = True

                # down
                elif event.key == pygame.K_DOWN:
                    self.down_pressed = True
                    if not self.down_last_frame:
                        self.down_keystroke = True

                # right
                elif event.key == pygame.K_RIGHT:
                    self.right_pressed = True
                    if not self.right_last_frame:
                        self.right_keystroke = True

                # w
                elif event.key == pygame.K_w:
                    self.w_pressed = True
                    if not self.w_last_frame:
                        self.w_keystroke = True

                # a
                elif event.key == pygame.K_a:
                    self.a_pressed = True
                    if not self.a_last_frame:
                        self.a_keystroke = True

                # s
                elif event.key == pygame.K_s:
                    self.s_pressed = True
                    if not self.s_last_frame:
                        self.s_keystroke = True

                # d
                elif event.key == pygame.K_d:
                    self.d_pressed = True
                    if not self.d_last_frame:
                        self.d_keystroke = True

                # p
                elif event.key == pygame.K_p:
                    self.p_pressed = True
                    if not self.p_last_frame:
                        self.p_keystroke = True

                # q
                elif event.key == pygame.K_q:
                    self.q_pressed = True
                    if not self.q_last_frame:
                        self.q_keystroke = True

                # r
                elif event.key == pygame.K_r:
                    self.r_pressed = True
                    if not self.r_last_frame:
                        self.r_keystroke = True

                # 1
                elif event.key == pygame.K_1:
                    self.k1_pressed = True
                    if not self.k1_last_frame:
                        self.k1_keystroke = True

                # 2
                elif event.key == pygame.K_2:
                    self.k2_pressed = True
                    if not self.k2_last_frame:
                        self.k2_keystroke = True

                # 3
                elif event.key == pygame.K_3:
                    self.k3_pressed = True
                    if not self.k3_last_frame:
                        self.k3_keystroke = True

                # 4
                elif event.key == pygame.K_4:
                    self.k4_pressed = True
                    if not self.k4_last_frame:
                        self.k4_keystroke = True

                # 5
                elif event.key == pygame.K_5:
                    self.k5_pressed = True
                    if not self.k5_last_frame:
                        self.k5_keystroke = True

            # release keys
            elif event.type == pygame.KEYUP:

                # esc
                if event.key == pygame.K_ESCAPE:
                    self.esc_pressed = False

                # space
                elif event.key == pygame.K_SPACE:
                    self.space_pressed = False

                # return
                elif event.key == pygame.K_RETURN:
                    self.return_pressed = False

                # lshift
                elif event.key == pygame.K_LSHIFT:
                    self.lshift_pressed = False

                # minus
                elif event.key == pygame.K_MINUS:
                    self.minus_pressed = False

                # equals
                elif event.key == pygame.K_EQUALS:
                    self.equals_pressed = False

                # up
                elif event.key == pygame.K_UP:
                    self.up_pressed = False

                # left
                elif event.key == pygame.K_LEFT:
                    self.left_pressed = False

                # down
                elif event.key == pygame.K_DOWN:
                    self.down_pressed = False

                # right
                elif event.key == pygame.K_RIGHT:
                    self.right_pressed = False

                # w
                elif event.key == pygame.K_w:
                    self.w_pressed = False

                # a
                elif event.key == pygame.K_a:
                    self.a_pressed = False

                # s
                elif event.key == pygame.K_s:
                    self.s_pressed = False

                # d
                elif event.key == pygame.K_d:
                    self.d_pressed = False

                # p
                elif event.key == pygame.K_p:
                    self.p_pressed = False

                # q
                elif event.key == pygame.K_q:
                    self.q_pressed = False

                # r
                elif event.key == pygame.K_r:
                    self.r_pressed = False

                # 1
                elif event.key == pygame.K_1:
                    self.k1_pressed = False

                # 2
                elif event.key == pygame.K_2:
                    self.k2_pressed = False

                # 3
                elif event.key == pygame.K_3:
                    self.k3_pressed = False

                # 4
                elif event.key == pygame.K_4:
                    self.k4_pressed = False

                # 5
                elif event.key == pygame.K_5:
                    self.k5_pressed = False

        # set mouse button last frame to current one
        self.left_mouse_last_frame = self.left_mouse_pressed
        self.middle_mouse_last_frame = self.middle_mouse_pressed
        self.right_mouse_last_frame = self.right_mouse_pressed

        # set keyboard key last frame to current one
        self.esc_last_frame = self.esc_pressed
        self.space_last_frame = self.space_pressed
        self.return_last_frame = self.return_pressed
        self.lshift_last_frame = self.lshift_pressed
        self.minus_last_frame = self.minus_pressed
        self.equals_last_frame = self.equals_pressed
        self.up_last_frame = self.up_pressed
        self.left_last_frame = self.left_pressed
        self.down_last_frame = self.down_pressed
        self.right_last_frame = self.right_pressed
        self.w_last_frame = self.w_pressed
        self.a_last_frame = self.a_pressed
        self.s_last_frame = self.s_pressed
        self.d_last_frame = self.d_pressed
        self.p_last_frame = self.p_pressed
        self.q_last_frame = self.q_pressed
        self.r_last_frame = self.r_pressed
        self.k1_last_frame = self.k1_pressed
        self.k2_last_frame = self.k2_pressed
        self.k3_last_frame = self.k3_pressed
        self.k4_last_frame = self.k4_pressed
        self.k5_last_frame = self.k5_pressed

    def main_loop(self):
        while not self.exiting_game:
            self.game_loop()

    def set_grid(self):

        # build empty grid
        self.grid = []
        for row in range(self.rows):
            self.grid.append([])
            for column in range(self.columns):
                self.grid[row].append(0)

        # build empty grid for visibility
        self.grid_visibility = []
        for row in range(self.rows):
            self.grid_visibility.append([])
            for column in range(self.columns):
                self.grid_visibility[row].append(0)

        # set mine number based on difficulty
        if self.difficulty == EASY:
            total_mines = self.rows * self.columns // 9
        elif self.difficulty == MODERATE:
            total_mines = self.rows * self.columns // 8
        else:
            total_mines = self.rows * self.columns // 7

        # place mines
        placed_mines = 0
        while placed_mines < total_mines:
            mine_column = random.randrange(self.columns)
            mine_row = random.randrange(self.rows)
            if self.grid[mine_row][mine_column] == 0:
                self.grid[mine_row][mine_column] = -1
                placed_mines += 1

        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row][col] != -1:
                    mines_touching = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if not i == j == 0:
                                if 0 <= row - i < self.rows:
                                    if 0 <= col - j < self.columns:
                                        if self.grid[row - i][col - j] == -1:
                                            mines_touching += 1
                    self.grid[row][col] = mines_touching

    def change_size(self, columns, rows):

        pygame.quit()

        # set row and column size
        self.columns = columns
        self.rows = rows

        self.set_grid()

        # set display size
        self.screen_width = (self.box_width * self.columns) + ((self.box_margin * self.columns) + self.box_margin)
        self.screen_height = (self.box_height * self.rows) + ((self.box_margin * self.rows) + self.box_margin)

        self.init_pygame(self.screen_width, self.screen_height)

    def game_loop(self):
        done = False
        self.init_pygame(self.screen_width, self.screen_height)
        while not done and not self.exiting_game:
            self.process_events()
            self.run_logic()
            self.display_frame(self.screen)
            self.clock.tick(10)
        pygame.quit()

    def init_pygame(self, screen_width, screen_height):
        pygame.init()

        # initialize screen
        size = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("old mines")

        # set pygame clock
        self.clock = pygame.time.Clock()

        self.mine_image = pygame.image.load("images/mine20x20.png").convert_alpha()
        self.flag_image = pygame.image.load("images/flag20x20.png").convert_alpha()

    def run_logic(self):
        """
        this method is run for each frame of the game,
        it updates positions and checks for collisions
        """

        # game logic
        if self.state == GAME:
            self.game_logic()

        # game over logic
        elif self.state == GAME_OVER:
            self.game_over_logic()

        # menu logic
        elif self.state == MENU:
            self.menu_logic()

        # difficulty menu logic
        elif self.state == DIFFICULTY_MENU:
            self.difficulty_logic()

        elif self.state == WIN:
            self.win_logic()

    def display_frame(self, screen):
        """ display everything to the screen for the game """

        screen.fill(DARK_GREY)
        if self.state == GAME_OVER:
            self.display_game_over(screen)

        elif self.state == GAME:
            self.display_game(screen)

        elif self.state == MENU:
            self.display_menu(screen)

        elif self.state == DIFFICULTY_MENU:
            self.display_difficulty_menu(screen)

        elif self.state == WIN:
            self.display_win(screen)

        pygame.display.flip()

    def menu_logic(self):

        # don't let player move too far down the menu
        if self.s_keystroke or self.down_keystroke:
            if self.menu_select < 3:
                self.menu_select += 1

        # don't let player move too far up the menu
        elif self.w_keystroke or self.up_keystroke:
            if self.menu_select > 0:
                self.menu_select -= 1

        # menu selection
        elif self.return_keystroke or self.space_keystroke:

            # resume game
            if self.menu_select == 0:
                self.state = GAME

            # new game
            elif self.menu_select == 1:
                self.set_grid()
                self.game_in_progress = True
                self.state = GAME

            # options
            elif self.menu_select == 2:
                self.state = DIFFICULTY_MENU

            # quit game
            elif self.menu_select == 3:
                self.exiting_game = True

        # close menu on esc
        elif self.esc_keystroke:
            self.state = GAME

    def difficulty_logic(self):

        # don't let player move too far down the menu
        if self.s_keystroke or self.down_keystroke:
            if self.difficulty_menu_select < 3:
                self.difficulty_menu_select += 1

        # don't let player move too far up the menu
        elif self.w_keystroke or self.up_keystroke:
            if self.difficulty_menu_select > 0:
                self.difficulty_menu_select -= 1

        # menu selection
        elif self.return_keystroke or self.space_keystroke:

            # resume game
            if self.difficulty_menu_select == 0 and self.difficulty != EASY:
                self.difficulty = EASY
                self.change_size(10, 10)

            # new game
            elif self.difficulty_menu_select == 1 and self.difficulty != MODERATE:
                self.difficulty = MODERATE
                self.change_size(20, 20)

            # options
            elif self.difficulty_menu_select == 2 and self.difficulty != HARD:
                self.difficulty = HARD
                self.change_size(40, 20)

            # quit game
            elif self.difficulty_menu_select == 3:
                self.state = MENU

        # close menu on esc
        elif self.esc_keystroke:
            self.state = MENU

    def game_over_logic(self):

        # go to menu on esc press
        if self.esc_keystroke:
            self.state = MENU

    def win_logic(self):

        # go to menu on esc press
        if self.esc_keystroke:
            self.state = MENU

    def game_logic(self):

        # show menu
        if self.esc_keystroke:
            self.state = MENU

        elif self.left_mouse_click:

            # make this part better
            pos = pygame.mouse.get_pos()
            pos_x = pos[0]
            pos_y = pos[1]
            mouse_col = int(pos_x // 25)
            mouse_row = int(pos_y // 25)
            if mouse_col > self.columns:
                mouse_col = self.columns
            if mouse_row > self.rows:
                mouse_row = self.rows
            print("row:", mouse_row, "col:", mouse_col)

            if self.grid_visibility[mouse_row][mouse_col] != 2:
                if self.grid[mouse_row][mouse_col] == -1:
                    for i in range(self.rows):
                        for j in range(self.columns):
                            self.grid_visibility[i][j] = 1
                    self.state = GAME_OVER
                elif self.grid_visibility[mouse_row][mouse_col] == 0:
                    if self.grid[mouse_row][mouse_col] == 0:
                        self.grid_visibility[mouse_row][mouse_col] = 1
                        self.clear_blank_area(mouse_row, mouse_col)
                    else:
                        self.grid_visibility[mouse_row][mouse_col] = 1

                    # break these loops if player hasn't won
                    check_win = True
                    for i in range(self.rows):
                        for j in range(self.columns):
                            if self.grid[i][j] != -1:
                                if self.grid_visibility[i][j] == 0:
                                    check_win = False
                    if check_win:
                        self.state = WIN

        elif self.right_mouse_click:
            pos = pygame.mouse.get_pos()
            pos_x = pos[0]
            pos_y = pos[1]
            mouse_col = int(pos_x // 25)
            mouse_row = int(pos_y // 25)
            print("row:", mouse_row, "col:", mouse_col)
            if self.grid_visibility[mouse_row][mouse_col] == 0:
                self.grid_visibility[mouse_row][mouse_col] = 2
            elif self.grid_visibility[mouse_row][mouse_col] == 2:
                self.grid_visibility[mouse_row][mouse_col] = 0

    def clear_blank_area(self, mouse_row, mouse_col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= mouse_row + i < self.rows:
                    if 0 <= mouse_col + j < self.columns:
                        if self.grid[mouse_row + i][mouse_col + j] == 0:
                            self.grid_visibility[mouse_row + i][mouse_col + j] = 1

    def display_game_over(self, screen):
        box_x = self.box_margin
        box_y = self.box_margin
        font = pygame.font.SysFont("Calibri", 20)
        number_colors = [BLUE, GREEN, YELLOW, ORANGE, PURPLE, RED, BROWN, BLACK]

        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid_visibility[row][column] == 1:
                    box_color = DARK_GREY
                else:
                    box_color = DARKER_GREY

                # draw numbers on empty spots showing how many mines they are touching
                if self.grid_visibility[row][column] == 1:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                    if self.grid[row][column] > 0:
                        text = font.render(str(self.grid[row][column]), True, number_colors[self.grid[row][column] - 1])
                        screen.blit(text, [box_x + 5, box_y + 2])

                    # draw mines
                    elif self.grid[row][column] == -1:
                        screen.blit(self.mine_image, [box_x, box_y])

                # draw flags
                elif self.grid_visibility[row][column] == 2:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                    screen.blit(self.flag_image, [box_x, box_y])

                else:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                box_x += self.box_width + self.box_margin
            box_x = self.box_margin
            box_y += self.box_height + self.box_margin
        font2 = pygame.font.SysFont("Calibri", 15,)
        text = font2.render("You Lose, Press ESC for Menu", True, WHITE)
        center_x = (self.screen_width // 2) - (text.get_width() // 2)
        center_y = (self.screen_height // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])

    def display_win(self, screen):
        box_x = self.box_margin
        box_y = self.box_margin
        font = pygame.font.SysFont("Calibri", 20)
        number_colors = [BLUE, GREEN, YELLOW, ORANGE, PURPLE, RED, BROWN, BLACK]

        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid_visibility[row][column] == 1:
                    box_color = DARK_GREY
                else:
                    box_color = DARKER_GREY

                # draw numbers on empty spots showing how many mines they are touching
                if self.grid_visibility[row][column] == 1:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                    if self.grid[row][column] > 0:
                        text = font.render(str(self.grid[row][column]), True, number_colors[self.grid[row][column] - 1])
                        screen.blit(text, [box_x + 5, box_y + 2])

                    # draw mines
                    elif self.grid[row][column] == -1:
                        screen.blit(self.mine_image, [box_x, box_y])

                # draw flags
                elif self.grid_visibility[row][column] == 2:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                    screen.blit(self.flag_image, [box_x, box_y])

                else:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                box_x += self.box_width + self.box_margin
            box_x = self.box_margin
            box_y += self.box_height + self.box_margin
        font2 = pygame.font.SysFont("Calibri", 15,)
        text = font2.render("You Win, Press ESC for Menu", True, WHITE)
        center_x = (self.screen_width // 2) - (text.get_width() // 2)
        center_y = (self.screen_height // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])

    def display_game(self, screen):
        box_x = self.box_margin
        box_y = self.box_margin
        font = pygame.font.SysFont("Calibri", 20)
        number_colors = [BLUE, GREEN, YELLOW, ORANGE, PURPLE, RED, BROWN, BLACK]

        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid_visibility[row][column] == 1:
                    box_color = DARK_GREY
                else:
                    box_color = DARKER_GREY

                # draw numbers on empty spots showing how many mines they are touching
                if self.grid_visibility[row][column] == 1:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                    if self.grid[row][column] > 0:
                        text = font.render(str(self.grid[row][column]), True, number_colors[self.grid[row][column] - 1])
                        screen.blit(text, [box_x + 5, box_y + 2])

                    # draw mines
                    elif self.grid[row][column] == -1:
                        screen.blit(self.mine_image, [box_x, box_y])

                # draw flags
                elif self.grid_visibility[row][column] == 2:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                    screen.blit(self.flag_image, [box_x, box_y])

                else:
                    pygame.draw.rect(screen, box_color, [box_x, box_y, self.box_width, self.box_height])
                box_x += self.box_width + self.box_margin
            box_x = self.box_margin
            box_y += self.box_height + self.box_margin

    def display_menu(self, screen):
            screen.fill(DARKER_GREY)

            y = 20
            font = pygame.font.SysFont("Calibri", 35)
            text = font.render("OLD MINES", True, WHITE)
            screen.blit(text, [20, y])
            y += 65
            menu_list = ["RESUME", "NEW GAME", "DIFFICULTY", "QUIT"]
            menu_x = 30
            for i in range(len(menu_list)):
                if i == self.menu_select:
                    if i == 0 and not self.game_in_progress:
                        menu_item_color = GREY
                    else:
                        menu_item_color = WHITE
                else:
                    if i == 0 and not self.game_in_progress:
                        menu_item_color = DARK_GREY
                    else:
                        menu_item_color = LIGHTER_GREY
                font = pygame.font.SysFont("Calibri", 25)
                text = font.render(menu_list[i], True, menu_item_color)
                screen.blit(text, [menu_x, y])
                y += 40

    def display_difficulty_menu(self, screen):
            screen.fill(DARKER_GREY)

            y = 20
            font = pygame.font.SysFont("Calibri", 35)
            text = font.render("OLD MINES", True, WHITE)
            screen.blit(text, [20, y])
            y += 65
            menu_list = ["EASY", "MODERATE", "HARD", "BACK"]
            menu_x = 30
            for i in range(len(menu_list)):
                if i == self.difficulty_menu_select:
                    if i + 4 == self.difficulty:
                        menu_item_color = GREY
                    else:
                        menu_item_color = WHITE
                elif i + 4 == self.difficulty:
                    menu_item_color = DARK_GREY
                else:
                    menu_item_color = LIGHTER_GREY
                font = pygame.font.SysFont("Calibri", 25)
                text = font.render(menu_list[i], True, menu_item_color)
                screen.blit(text, [menu_x, y])
                y += 40
