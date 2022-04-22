import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np

# declare the variables we use
a_active = False
b_active = False
c_active = False
d_active = False
selected = "linear"

a_string_value = "a: 1"
b_string_value = "b: 1"
c_string_value = "c: 0"
d_string_value = "d: 0"

a_value = int(a_string_value[3:])
b_value = int(b_string_value[3:])
c_value = int(c_string_value[3:])
d_value = int(d_string_value[3:])

a_value2 = int(a_string_value[3:])
b_value2 = int(b_string_value[3:])
c_value2 = int(c_string_value[3:])
d_value2 = int(d_string_value[3:])

width = 1200
height = 600
selected1 = "linear"
selected2 = "linear"
expression = "ax + b"


# a function that initialize pygame windowing for OpenGl
def init():
    pygame.init()
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)


# a function that draws the graphs on pygame window by taking inputs from OpenGl
def draw():
    global a_value, b_value, c_value, d_value, selected1, selected2
    glClear(GL_COLOR_BUFFER_BIT)
    x = np.linspace(-100, 100, 5000)
    if selected1 == "linear":
        y1 = np.multiply(x, a_value) + b_value
    if selected1 == "quadratic":
        y1 = a_value*np.power(x, 2) + b_value*x + c_value
    if selected1 == "sine":
        y1 = a_value*np.sin(b_value*x + c_value) + d_value
    if selected1 == "cos":
        y1 = a_value*np.cos(b_value*x + c_value) + d_value
    if selected1 == "power":
        y1 = a_value*np.power(x, b_value)
    if selected1 == "exponential":
        y1 = a_value*np.power(np.e, x) + c_value
    if selected1 == "logarithmic":
        y1 = a_value*np.log10(b_value*x + c_value) + d_value
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.0, 0.0)
    for a, b in zip(x, y1):
        glVertex2f(a, b)
    glEnd()

    if selected2 == "linear":
        y2 = np.multiply(x, a_value2) + b_value2
    if selected2 == "quadratic":
        y2 = a_value2*np.power(x, 2) + b_value2*x + c_value2
    if selected2 == "sine":
        y2 = a_value2*np.sin(b_value2*x + c_value2) + d_value2
    if selected2 == "cos":
        y2 = a_value2*np.cos(b_value2*x + c_value2) + d_value2
    if selected2 == "power":
        y2 = a_value2*np.power(x, b_value2)
    if selected2 == "exponential":
        y2 = a_value2*np.power(np.e, x) + c_value2
    if selected2 == "logarithmic":
        y2 = a_value2*np.log10(b_value2*x + c_value2) + d_value2

    glBegin(GL_LINE_STRIP)
    glColor3f(0.0, 0.0, 1.0)
    for c, d in zip(x, y2):
        glVertex2f(c, d)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-100, 0.0)
    glVertex2f(100, 0.0)
    glVertex2f(0.0, 100)
    glVertex2f(0.0, -100)
    glEnd()
    glFlush()


# main function where the graphing window starts
def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


# initialize the controller window using pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 600])
base_font = pygame.font.Font(None, 25)
text_font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 20)
button_gap = 10
start = 10
initial_start = 200
vertical_gap = 10
horizontal_width = 100


def increase_start(button_width=50):
    global start
    start += button_width + button_gap
    return button_width


def vertical_placement(width=40):
    global initial_start
    initial_start += width + vertical_gap
    return width


# declare variables that we use in the controller window
input_rect = pygame.Rect(200, 200, 140, 32)
input_rect2 = pygame.Rect(200, 300, 140, 32)

linear_rect = pygame.Rect(start, 100, increase_start(60), 32)
quadratic_rect = pygame.Rect(start, 100, increase_start(90), 32)
sine_rect = pygame.Rect(start, 100, increase_start(), 32)
cos_rect = pygame.Rect(start, 100, increase_start(), 32)
power_rect = pygame.Rect(start, 100, increase_start(60), 32)
exp_rect = pygame.Rect(start, 100, increase_start(105), 32)
log_rect = pygame.Rect(start, 100, increase_start(105), 32)

explanation_rect = pygame.Rect(230, 150, 200, 32)
a_rect = pygame.Rect(230, initial_start, horizontal_width,
                     vertical_placement())
b_rect = pygame.Rect(230, initial_start, horizontal_width,
                     vertical_placement())
c_rect = pygame.Rect(230, initial_start, horizontal_width,
                     vertical_placement())
d_rect = pygame.Rect(230, initial_start, horizontal_width,
                     vertical_placement())

select1_rect = pygame.Rect(
    100, initial_start, horizontal_width + 50, vertical_placement())
select2_rect = pygame.Rect(300, initial_start - 50, horizontal_width + 50, 40)

select_rect = pygame.Rect(
    170, initial_start, horizontal_width + 100, vertical_placement())
plot_rect = pygame.Rect(
    170, initial_start, horizontal_width + 100, vertical_placement())

color_rect = pygame.Color(25, 25, 55)
color_selected = pygame.Color(25, 25, 255)
text_color = (255, 255, 255)

second = False
finished = False
first_function = ""
second_function = ""
error_occured = False


# converts the input variables into a single mathematical function string for the first function
def text_maker1(a, b, c, d):
    global first_function
    exp = "y="
    if selected1 == "linear":
        exp += "(" + str(a) + ")x + (" + str(b) + ")"
    if selected1 == "quadratic":
        exp += "(" + str(a) + ")x^2+(" + str(b) + ")x+(" + str(c) + ")"
    if selected1 == "sine":
        exp += "(" + str(a) + ")sin((" + str(b) + "x)+(" + \
            str(c) + "))+" + "(" + str(d) + ")"
    if selected1 == "cos":
        exp += "(" + str(a) + ")cos((" + str(b) + "x)+(" + \
            str(c) + "))+" + "(" + str(d) + ")"
    if selected1 == "power":
        exp += "(" + str(a) + ")x^(" + str(b) + ")"
    if selected1 == "exponential":
        exp += "(" + str(a) + ")(" + str(b) + "^x)+(" + str(c) + ")"
    if selected1 == "logarithmic":
        exp += "(" + str(a) + ")log((" + str(b) + \
            ")x+(" + str(c) + "))+(" + str(d) + ")"
    first_function = exp
    return exp


# converts the input variables into a single mathematical function string for the second function
def text_maker2(a, b, c, d):
    global second_function
    exp = "y="
    if selected2 == "linear":
        exp += "(" + str(a) + ")x + (" + str(b) + ")"
    if selected2 == "quadratic":
        exp += "(" + str(a) + ")x^2+(" + str(b) + ")x+(" + str(c) + ")"
    if selected2 == "sine":
        exp += "(" + str(a) + ")sin((" + str(b) + "x)+(" + \
            str(c) + "))+" + "(" + str(d) + ")"
    if selected2 == "cos":
        exp += "(" + str(a) + ")cos((" + str(b) + "x)+(" + \
            str(c) + "))+" + "(" + str(d) + ")"
    if selected2 == "power":
        exp += "(" + str(a) + ")x^(" + str(b) + ")"
    if selected2 == "exponential":
        exp += "(" + str(a) + ")(" + str(b) + "^x)+(" + str(c) + ")"
    if selected2 == "logarithmic":
        exp += "(" + str(a) + ")log((" + str(b) + \
            ")x+(" + str(c) + "))+(" + str(d) + ")"
    second_function = exp
    return exp


# take inputs from users in the controller window
while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if linear_rect.collidepoint(event.pos):
                    selected = "linear"
                if quadratic_rect.collidepoint(event.pos):
                    selected = "quadratic"
                if sine_rect.collidepoint(event.pos):
                    selected = 'sine'
                if cos_rect.collidepoint(event.pos):
                    selected = "cos"
                if power_rect.collidepoint(event.pos):
                    selected = "power"
                if exp_rect.collidepoint(event.pos):
                    selected = "exponential"
                if log_rect.collidepoint(event.pos):
                    selected = "logarithmic"
                if a_rect.collidepoint(event.pos):
                    a_active = True
                    b_active = False
                    c_active = False
                    d_active = False
                if b_rect.collidepoint(event.pos):
                    a_active = False
                    b_active = True
                    c_active = False
                    d_active = False
                if c_rect.collidepoint(event.pos):
                    a_active = False
                    b_active = False
                    c_active = True
                    d_active = False
                if d_rect.collidepoint(event.pos):
                    a_active = False
                    b_active = False
                    c_active = False
                    d_active = True
                if select_rect.collidepoint(event.pos):
                    if not second and not finished:
                        a_value = int(a_string_value[3:])
                        b_value = int(b_string_value[3:])
                        c_value = int(c_string_value[3:])
                        d_value = int(d_string_value[3:])
                        a_string_value = "a: 1"
                        b_string_value = "b: 1"
                        c_string_value = "c: 0"
                        d_string_value = "d: 0"
                        if selected == "linear":
                            selected1 = "linear"
                        if selected == "quadratic":
                            selected1 = "quadratic"
                        if selected == "sine":
                            selected1 = "sine"
                        if selected == "cos":
                            selected1 = "cos"
                        if selected == "power":
                            selected1 = "power"
                        if selected == "exponential":
                            selected1 = "exponential"
                        if selected == "logarithmic":
                            selected1 = "logarithmic"
                        second = True
                        finished = False
                        text_maker1(a_value, b_value, c_value, d_value)
                    elif second:
                        a_value2 = int(a_string_value[3:])
                        b_value2 = int(b_string_value[3:])
                        c_value2 = int(c_string_value[3:])
                        d_value2 = int(d_string_value[3:])
                        a_string_value = "a: 1"
                        b_string_value = "b: 1"
                        c_string_value = "c: 0"
                        d_string_value = "d: 0"
                        if selected == "linear":
                            selected2 = "linear"
                        if selected == "quadratic":
                            selected2 = "quadratic"
                        if selected == "sine":
                            selected2 = "sine"
                        if selected == "cos":
                            selected2 = "cos"
                        if selected == "power":
                            selected2 = "power"
                        if selected == "exponential":
                            selected2 = "exponential"
                        if selected == "logarithmic":
                            selected2 = "logarithmic"
                        finished = True
                        text_maker2(a_value2, b_value2, c_value2, d_value2)
                if plot_rect.collidepoint(event.pos):
                    if finished:
                        main()
            if event.type == pygame.KEYDOWN:
                error_occured = False
                if a_active:
                    if event.key == pygame.K_BACKSPACE and len(a_string_value) > 3:
                        a_string_value = a_string_value[:-1]
                    else:
                        if (48 <= ord(event.unicode) <= 57 or ord(event.unicode) == 45) and len(a_string_value) < 5:
                            a_string_value += event.unicode
                elif b_active:
                    if event.key == pygame.K_BACKSPACE and len(b_string_value) > 3:
                        b_string_value = b_string_value[:-1]
                    else:
                        if (48 <= ord(event.unicode) <= 57 or ord(event.unicode) == 45) and len(b_string_value) < 5:
                            b_string_value += event.unicode
                elif c_active:
                    if event.key == pygame.K_BACKSPACE and len(c_string_value) > 3:
                        c_string_value = c_string_value[:-1]
                    else:
                        if (48 <= ord(event.unicode) <= 57 or ord(event.unicode) == 45) and len(c_string_value) < 5:
                            c_string_value += event.unicode
                elif d_active:
                    if event.key == pygame.K_BACKSPACE and len(d_string_value) > 3:
                        d_string_value = d_string_value[:-1]
                    else:
                        if (48 <= ord(event.unicode) <= 57 or ord(event.unicode) == 45) and len(d_string_value) < 5:
                            d_string_value += event.unicode
    except Exception:
        error_occured = True
    screen.fill((255, 255, 255))

    # drawing different rectangles we use
    pygame.draw.rect(screen, color_selected, linear_rect) if selected == "linear" else pygame.draw.rect(
        screen, color_rect, linear_rect)
    pygame.draw.rect(screen, color_selected, quadratic_rect) if selected == "quadratic" else pygame.draw.rect(
        screen, color_rect, quadratic_rect)
    pygame.draw.rect(screen, color_selected, sine_rect) if selected == "sine" else pygame.draw.rect(
        screen, color_rect, sine_rect)
    pygame.draw.rect(screen, color_selected, cos_rect) if selected == "cos" else pygame.draw.rect(
        screen, color_rect, cos_rect)
    pygame.draw.rect(screen, color_selected, power_rect) if selected == "power" else pygame.draw.rect(
        screen, color_rect, power_rect)
    pygame.draw.rect(screen, color_selected, exp_rect) if selected == "exponential" else pygame.draw.rect(
        screen, color_rect, exp_rect)
    pygame.draw.rect(screen, color_selected, log_rect) if selected == "logarithmic" else pygame.draw.rect(
        screen, color_rect, log_rect)
    pygame.draw.rect(screen, pygame.Color("white"), explanation_rect)
    pygame.draw.rect(screen, color_selected, a_rect) if a_active else pygame.draw.rect(
        screen, color_rect, a_rect)
    pygame.draw.rect(screen, color_selected, b_rect) if b_active else pygame.draw.rect(
        screen, color_rect, b_rect)
    pygame.draw.rect(screen, pygame.Color("red"), select1_rect)
    pygame.draw.rect(screen, pygame.Color("blue"), select2_rect)
    pygame.draw.rect(screen, pygame.Color("blue"), select_rect) if not finished else pygame.draw.rect(
        screen, pygame.Color(200, 200, 255), select_rect)
    pygame.draw.rect(screen, pygame.Color("blue"), plot_rect) if finished else pygame.draw.rect(
        screen, pygame.Color(200, 200, 255), plot_rect)

    # declaring different texts we use
    text_surface2 = base_font.render("WELCOME", True, (0, 0, 255))
    text_name = base_font.render("made by Segni Dessalegn", True, (0, 0, 255))
    text_surface3 = base_font.render(
        "Choose two matchematical functions and enter the values of variables", True, (25, 25, 50))
    text_recomended = base_font.render(
        "values around 50 are recomended to better see the effects", True, (255, 25, 50))
    linear_text = base_font.render("linear", True, text_color)
    quadratic_text = base_font.render("quadratic", True, text_color)
    sine_text = base_font.render("sine", True, text_color)
    cos_text = base_font.render("cos", True, text_color)
    power_text = base_font.render("power", True, text_color)
    exp_text = base_font.render("exponential", True, text_color)
    log_text = base_font.render("logarithmic", True, text_color)
    explanation_text = text_font.render(expression, True, (255, 0, 0)) if not error_occured else text_font.render(
        "invalid input", True, (255, 0, 0))
    a_text = text_font.render(a_string_value, True, (255, 255, 255))
    b_text = text_font.render(b_string_value, True, (255, 255, 255))
    c_text = text_font.render(c_string_value, True, (255, 255, 255))
    d_text = text_font.render(d_string_value, True, (255, 255, 255))
    select_text = text_font.render(
        "select", True, (255, 255, 255)) if not finished else text_font.render("select", True, (25, 25, 50))
    function1_text = small_font.render(first_function, True, (255, 255, 255)) if second else base_font.render(
        "first function", True, (255, 255, 255))
    function2_text = small_font.render(second_function, True, (255, 255, 255)) if finished else base_font.render(
        "second function", True, (255, 255, 255))
    plot_text = text_font.render("draw graph", True, (255, 255, 255)) if finished else text_font.render(
        "draw graph", True, (250, 250, 255))

    # attaching the texts to the corresponding rectangles
    screen.blit(text_surface2, (250, 10))
    screen.blit(text_name, (180, 30))
    screen.blit(text_surface3, (10, 50))
    screen.blit(text_recomended, (70, 70))
    screen.blit(sine_text, (sine_rect.x + 5, sine_rect.y + 5))
    screen.blit(cos_text, (cos_rect.x + 5, cos_rect.y + 5))
    screen.blit(linear_text, (linear_rect.x + 5, linear_rect.y + 5))
    screen.blit(quadratic_text, (quadratic_rect.x + 5, quadratic_rect.y + 5))
    screen.blit(power_text, (power_rect.x + 5, power_rect.y + 5))
    screen.blit(exp_text, (exp_rect.x + 5, exp_rect.y + 5))
    screen.blit(log_text, (log_rect.x + 5, log_rect.y + 5))
    screen.blit(explanation_text,
                (explanation_rect.x + 5, explanation_rect.y + 5))
    screen.blit(a_text, (a_rect.x + 5, a_rect.y + 10))
    screen.blit(b_text, (b_rect.x + 5, b_rect.y + 10))
    screen.blit(function1_text, (select1_rect.x + 5, select1_rect.y + 10))
    screen.blit(function2_text, (select2_rect.x + 5, select2_rect.y + 10))
    screen.blit(select_text, (select_rect.x + 70, select_rect.y + 10))
    screen.blit(plot_text, (plot_rect.x + 45, plot_rect.y + 10))

    # show the variables based on the selected function
    if selected == "linear" or selected == "power":
        c_string_value = "c: 0"
        d_string_value = "d: 0"
    if selected == "quadratic" or selected == "exponential":
        pygame.draw.rect(screen, color_selected, c_rect) if c_active else pygame.draw.rect(
            screen, color_rect, c_rect)
        screen.blit(c_text, (c_rect.x + 5, c_rect.y + 10))
        d_string_value = "d: 0"
    if selected == "sine" or selected == "cos" or selected == "logarithmic":
        pygame.draw.rect(screen, color_selected, c_rect) if c_active else pygame.draw.rect(
            screen, color_rect, c_rect)
        screen.blit(c_text, (c_rect.x + 5, c_rect.y + 10))
        pygame.draw.rect(screen, color_selected, d_rect) if d_active else pygame.draw.rect(
            screen, color_rect, d_rect)
        screen.blit(d_text, (d_rect.x + 5, d_rect.y + 10))

    # show different expressions based on the selected function
    if selected == "linear":
        expression = "ax + b"
    elif selected == "quadratic":
        expression = "ax^2 + bx + c"
    elif selected == "sine":
        expression = "asin(bx + c) + d"
    elif selected == "cos":
        expression = "acos(bx + c) + d"
    elif selected == "power":
        expression = "ax^b"
    elif selected == "exponential":
        expression = "a(b^x) +c"
    elif selected == "logarithmic":
        expression = "alog(bx + c) + d"

    pygame.display.flip()
    clock.tick(60)
    