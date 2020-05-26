import time
import tkinter
import random

from collections import OrderedDict

CANVAS_WIDTH = 600  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600  # Height of drawing canvas in pixels
UNIT_SIZE = 10
SPEED = 5

class Snake:

    def __init__(self, snake_num, canvas, snake_color):
        self.direction_x = 1
        self.direction_y = 0
        self.start_snake_size = 10
        self.snake_size_counter = 0
        self.score_counter = 0
        self.snake_chain = []
        self.snake_num = snake_num
        self.canvas = canvas
        self.snake_color = snake_color
        self.start_x = (self.start_snake_size - 1)*UNIT_SIZE
        if self.snake_num == 1:
            self.start_y = CANVAS_HEIGHT / 3 - UNIT_SIZE
        else:
            self.start_y = (CANVAS_HEIGHT * 2 / 3) - UNIT_SIZE
        self.initialize_snake()
        self.is_alive = True

    def initialize_snake(self):
        self.snake_chain.append(self.canvas.create_oval(self.start_x, self.start_y,
                                                        self.start_x + UNIT_SIZE, self.start_y + UNIT_SIZE,
                                                        fill='orange', outline='brown', tags=('snake_' + str(self.snake_num), 'head')))
        for blockIndex in range(self.start_snake_size - 1):
            x0 = (self.start_snake_size - 1 - (blockIndex + 1)) * UNIT_SIZE
            x1 = x0 + UNIT_SIZE
            snake_block = self.create_snake_block(x0, self.start_y, x1, self.start_y + UNIT_SIZE,
                                                  self.start_snake_size - 1 - blockIndex)
            self.snake_chain.append(snake_block)

    def create_snake_block(self, x0, y0, x1, y1, tag):
        return self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.snake_color, tags='snake')

    def move_up(self,event):
        if self.direction_x == 0 and self.direction_y == 1:
            pass
        else:
            self.direction_y = -1
            self.direction_x = 0

    def move_down(self,event):
        if self.direction_x == 0 and self.direction_y == -1:
            pass
        else:
            self.direction_y = 1
            self.direction_x = 0

    def move_left(self,event):
        if self.direction_x == 1 and self.direction_y == 0:
            pass
        else:
            self.direction_x = -1
            self.direction_y = 0

    def move_right(self,event):
        if self.direction_x == -1 and self.direction_y == 0:
            pass
        else:
            self.direction_x = 1
            self.direction_y = 0

    def plus_size(self):
        self.snake_size_counter += 1
        x0, y0, x1, y1 = self.canvas.coords(self.snake_chain[0])
        if self.direction_x == 1:
            x0 -= self.snake_size_counter * UNIT_SIZE
            x1 -= self.snake_size_counter * UNIT_SIZE
        elif self.direction_x == -1:
            x0 += self.snake_size_counter * UNIT_SIZE
            x1 += self.snake_size_counter * UNIT_SIZE
        elif self.direction_y == 1:
            y0 -= self.snake_size_counter * UNIT_SIZE
            y1 -= self.snake_size_counter * UNIT_SIZE
        elif self.direction_y == -1:
            y0 += self.snake_size_counter * UNIT_SIZE
            y1 += self.snake_size_counter * UNIT_SIZE
        snake_block = self.create_snake_block(x0, y0, x1, y1, (self.snake_size_counter + self.start_snake_size))
        self.snake_chain.append(snake_block)
        # Whenever a new block is added to snake, add it to snake list.

    def move_snake(self):
        if self.is_alive:
            chain_pos_dict = {}
            for obj in self.snake_chain:
                chain_pos_dict[obj] = self.canvas.coords(obj)

            snake_head_tag = self.get_head_tag()
            self.canvas.move(snake_head_tag, self.direction_x * UNIT_SIZE, self.direction_y * UNIT_SIZE)

            '''
            ASSUMPTION : Object IDs are maintained in a sorted list assuming that 
            the IDs are assigned in increasing order for new objects instantiated on Canvas
            '''
            key_list = sorted(chain_pos_dict.keys())
            nI = len(key_list)
            for i in range(1, nI):
                self.canvas.moveto(key_list[i], chain_pos_dict[key_list[i - 1]][0] - 1,
                                   chain_pos_dict[key_list[i - 1]][1] - 1)

    def get_head_tag(self):
        return 'snake_' + str(self.snake_num) + '&&head'

class TkinkerCanvas:

    def __init__(self, top):
        self.top = top
        self.canvas = self.make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Snake Game')
        self.player1_controls = ['<Up>','<Down>','<Left>','<Right>']
        self.player2_controls = ['w','s','a','d']
        self.snake1 = Snake(1, self.canvas, 'brown')
        self.snake2 = Snake(2, self.canvas, 'green')
        self.set_player_control(self.snake1, self.player1_controls)
        self.set_player_control(self.snake2, self.player2_controls)
        self.score_board1 = self.create_score_board(self.snake1.snake_num, self.snake1.snake_color)
        self.score_board2 = self.create_score_board(self.snake2.snake_num, self.snake2.snake_color)
        self.start_game()

    # This function creates a window that contains a drawing canvas
    def make_canvas(self, width, height, title):
        self.top.minsize(width=width, height=height)
        self.top.title(title)

        canvas = tkinter.Canvas(self.top, width=width + 1, height=height + 1, bg='black')
        canvas.pack(padx=10, pady=10)
        return canvas

    def set_player_control(self, snake, player_controls):
        self.canvas.focus_set()
        self.canvas.bind(player_controls[0], snake.move_up)
        self.canvas.bind(player_controls[1], snake.move_down)
        self.canvas.bind(player_controls[2], snake.move_left)
        self.canvas.bind(player_controls[3], snake.move_right)

    def create_score_board(self, num, color):
        if num == 1:
            x_offset = 0.05
        else:
            x_offset = 0.85
        return self.canvas.create_text(x_offset * CANVAS_WIDTH, 0.01 * CANVAS_HEIGHT,
                                text=('Score : ' + str(0)), anchor=tkinter.NW, font=("Times", 12, 'bold'), fill=color)

    def hit_something(self, snake):
        snake_head_tag = snake.get_head_tag()
        x1, y1, x2, y2 = self.canvas.coords(snake_head_tag)

        if (x1 <= 0) or (y1 <= 0) or (x2 >= CANVAS_WIDTH) or (y2 >= CANVAS_HEIGHT):
           self.handle_hit_wall(snake)

        results = self.canvas.find_overlapping(x1+1, y1+1, x2-1, y2-1)
        for item in results:
            if 'food' in self.canvas.gettags(item):
                self.handle_hit_food(item, snake)
                break
            elif 'snake' in self.canvas.gettags(item):
                self.handle_hit_snake(snake)

    def handle_hit_snake(self, snake):
        snake.is_alive = False

    def handle_hit_food(self, food_id, snake):
        self.canvas.delete(food_id)
        snake.plus_size()
        snake.score_counter += 10
        self.place_food()

    def handle_hit_wall(self, snake):
        snake.is_alive = False

    def handle_game_over(self):
        print("Game Over!")
        if (self.snake1.score_counter > self.snake2.score_counter):
            result_msg = self.snake1.snake_color.title() + ' Snake wins!'
        elif (self.snake2.score_counter > self.snake1.score_counter):
            result_msg = self.snake2.snake_color.title() + ' Snake wins!'
        else:
            result_msg = 'Its a tie!'
        widget = tkinter.Label(self.canvas, text='Game Over!\n' + result_msg , fg='white', bg='black', font=("Times", 20, 'bold'))
        widget.pack()
        widget.place(relx=0.5, rely=0.5, anchor='center')

    def is_game_over(self):
        if not self.snake1.is_alive and not self.snake2.is_alive:
            self.handle_game_over()
            return True
        return False

    def place_food(self):
        x1 = random.randrange(2*UNIT_SIZE, CANVAS_WIDTH - UNIT_SIZE, step=UNIT_SIZE)
        y1 = random.randrange(2*UNIT_SIZE, CANVAS_HEIGHT - UNIT_SIZE, step=UNIT_SIZE)
        self.canvas.create_oval(x1, y1, x1 + UNIT_SIZE, y1 + UNIT_SIZE, fill='red', tags='food')

    def update_scores(self):
        self.canvas.itemconfig(self.score_board1, text='Score : ' + str(self.snake1.score_counter))
        self.canvas.itemconfig(self.score_board2, text='Score : ' + str(self.snake2.score_counter))

    def display_label(self, message, display_time):
        widget = tkinter.Label(self.canvas, text=message, fg='white', bg='black',
                               font=("Times", 20, 'bold'))
        widget.place(relx=0.5, rely=0.5, anchor='center')
        self.canvas.update()
        time.sleep(display_time)
        widget.place_forget()
        self.canvas.update()

    def starter_message(self):
        self.display_label('Welcome to the Snake World!', 3)
        self.display_label('Your game starts in \n 3', 1)
        self.display_label('Your game starts in \n 2', 1)
        self.display_label('Your game starts in \n 1', 1)

    def start_game(self):
        self.starter_message()

        self.place_food()
        # ANIMATION LOOP
        while True:
            # Update World
            self.snake1.move_snake()
            self.snake2.move_snake()
            self.canvas.update()

            self.hit_something(self.snake1)
            self.hit_something(self.snake2)

            self.update_scores()

            if self.is_game_over():
                break
            # pause
            time.sleep(1/SPEED)

def main():
    top = tkinter.Tk()
    TkinkerCanvas(top)
    top.mainloop()

if __name__ == '__main__':
    main()
