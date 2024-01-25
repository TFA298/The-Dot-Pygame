import pygame

WIDTH, HEIGHT= 700, 600
windows = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("The Dot #2")

background = pygame.Color("white")

circle_radius = 35
circle_x = WIDTH//2
circle_y = HEIGHT//2
circle_velocity = 5
    
def run_stage2():
    run = True
    
    global circle_x, circle_y
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        circle_x += circle_velocity
        circle_y -= circle_velocity
            
        windows.fill(background)
        pygame.draw.circle(windows, "black", (circle_x, circle_y), circle_radius)
        pygame.display.flip()
    
    pygame.quit()
            
if __name__ == "__main__":
    run_stage2()