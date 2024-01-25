import pygame
import random

pygame.init()

WIDTH, HEIGHT= 700, 600
windows = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("The Dot #7")

background = pygame.Color("white")

center_x = WIDTH // 2
center_y = HEIGHT // 2

circle_radius = 35
temp_x = WIDTH//2
temp_y = HEIGHT//2
circle_x = temp_x - circle_radius
circle_y = temp_y - circle_radius
velocity_y = 7
velocity_x = 7
circle_object = pygame.Rect(circle_x, circle_y - circle_radius, circle_radius * 2, circle_radius * 2)

rect_width = 470
rect_height = 470
rect_x = center_x - rect_width // 2
rect_y = center_y - rect_height // 2
rectangle_object = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

text_font = pygame.font.SysFont(None, 30)

def score_couter(text, font, text_color, x, y):
    skor_text = font.render(text, True, text_color)
    windows.blit(skor_text, (x, y))

def objek():
    pygame.draw.rect(windows,"black", rectangle_object, width= 3)
    pygame.draw.circle(windows, "black", circle_object.center, circle_radius)   
    
boxes = []
scores = 0

def random_object():
    size = random.randint(15,25)
    while True:
        x = random.randint(rectangle_object.left, rectangle_object.right - size)
        y = random.randint(rectangle_object.top, rectangle_object.bottom - size)
        random_boxes_rect = pygame.Rect(x, y , size, size)
        
        if not circle_object.colliderect(random_boxes_rect):
            overlap = False
            for existing_box in boxes:
                if existing_box.colliderect(random_boxes_rect):
                    overlap = True
                    break
            if not overlap:
                # boxes.append(random_boxes_rect)
                return random_boxes_rect

def run_stage():
    run = True
    
    global velocity_x, velocity_y, scores
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        buttons = pygame.key.get_pressed()
        if buttons[pygame.K_LEFT] and circle_object.left - velocity_x >= rectangle_object.left:
            circle_object.x -= velocity_x
        if buttons[pygame.K_RIGHT]and circle_object.right + velocity_x <= rectangle_object.right:
            circle_object.x += velocity_x
        if buttons[pygame.K_UP] and circle_object.top - velocity_y >= rectangle_object.top:
            circle_object.y -= velocity_y
        if buttons[pygame.K_DOWN]and circle_object.bottom + velocity_y <= rectangle_object.bottom:
            circle_object.y += velocity_y
        
        if not boxes:
            random_boxes = random.randint(8, 8)
            boxes.extend([random_object() for _ in range(random_boxes)])
            
        windows.fill(background)
        objek()
        
        for box in boxes:
            pygame.draw.rect(windows, "black", box, width= 2)

        collision_occured = False
        for box in boxes:
            if circle_object.colliderect(box) and not collision_occured:
                scores += 1
                boxes.remove(box)
                collision_occured = True

        score_couter(f"Skor : {scores}", text_font, "black", 300, 25)
        
        pygame.display.flip()
    
    pygame.quit()
            
if __name__ == "__main__":
    run_stage()