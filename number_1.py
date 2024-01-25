import pygame

WIDTH, HEIGHT= 700, 600
windows = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("The Dot #1")

background = pygame.Color("white")


def run_stage1():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        windows.fill(background)
        pygame.draw.circle(windows, (0,0,0), (WIDTH//2, HEIGHT//2), 35)
        pygame.display.flip()
    
    pygame.quit()
            
if __name__ == "__main__":
    run_stage1()