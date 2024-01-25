import pygame

WIDTH, HEIGHT= 700, 600
windows = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("The Dot #5")

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

def objek():
    pygame.draw.rect(windows,"black", rectangle_object, width= 3)
    pygame.draw.circle(windows, "black", circle_object.center, circle_radius)    
    
def run_stage():
    run = True
    global circle_object
    clock = pygame.time.Clock()
    
    while run:
        
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        circle_object.center = (mouse_x, mouse_y)
        
        circle_object = circle_object.clamp(rectangle_object)
        
        windows.fill(background)
        objek()
        pygame.display.flip()
    
    pygame.quit()
            
if __name__ == "__main__":
    run_stage()