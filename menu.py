import pygame
import subprocess

pygame.init()

WIDTH, HEIGHT= 700, 600
windows = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Menu")
background = pygame.Color("white")

class button:
    def __init__(self, x, y, width, height, color, text, text_color, page_name):
        self.rect = pygame.Rect(x, y ,width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.page = page_name
    
    def draw(self):
        pygame.draw.rect(windows, self.color, self.rect)
        font = pygame.font.SysFont(None, 48)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center = self.rect.center)
        windows.blit(text, text_rect)
    
    def change_page(self):
        subprocess.run(["python", self.page])


text_font = pygame.font.SysFont("Arial", 50, bold= True)

def text_stage(text, font, text_color, x, y):
    skor_text = font.render(text, True, text_color)
    windows.blit(skor_text, (x, y))

stage1_button =  button(150, 200, 150, 50, "black", "Stage 1", "white", "number_1.py")
stage2_button =  button(150, 300, 150, 50, "black", "Stage 2", "white", "number_2.py")
stage3_button =  button(150, 400, 150, 50, "black", "Stage 3", "white", "number_3.py")
stage4_button =  button(150, 500, 150, 50, "black", "Stage 4", "white", "number_4.py")
stage5_button =  button(400, 200, 150, 50, "black", "Stage 5", "white", "number_5.py")
stage6_button =  button(400, 300, 150, 50, "black", "Stage 6", "white", "number_6.py")
stage7_button =  button(400, 400, 150, 50, "black", "Stage 7", "white", "number_7.py")
stage8_button =  button(400, 500, 150, 50, "black", "Stage 8", "white", "number_8.py")

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stage1_button.rect.collidepoint(event.pos):
                    stage1_button.change_page()
                elif stage2_button.rect.collidepoint(event.pos):
                    stage2_button.change_page()
                elif stage3_button.rect.collidepoint(event.pos):
                    stage3_button.change_page()
                elif stage4_button.rect.collidepoint(event.pos):
                    stage4_button.change_page()
                elif stage5_button.rect.collidepoint(event.pos):
                    stage5_button.change_page()
                elif stage6_button.rect.collidepoint(event.pos):
                    stage6_button.change_page()
                elif stage7_button.rect.collidepoint(event.pos):
                    stage7_button.change_page()
                elif stage8_button.rect.collidepoint(event.pos):
                    stage8_button.change_page()
                
            if event.type == pygame.QUIT:
                run = False
                break
            
        windows.fill(background)
        stage1_button.draw()
        stage2_button.draw()
        stage3_button.draw()
        stage4_button.draw()
        stage5_button.draw()
        stage6_button.draw()
        stage7_button.draw()
        stage8_button.draw()
        
        text_stage("Select Stage ", text_font, "black", 220, 70)
        pygame.display.flip()
    
    pygame.quit()
            
if __name__ == "__main__":
    main()