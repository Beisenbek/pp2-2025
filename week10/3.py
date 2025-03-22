import pygame

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

# The rest is code where you implement your game using the Scenes model

class TitleScene(SceneBase):
    def __init__(self):
        self.menu_items = ["1. New Game","2. Preferences", "3. Exit"]
        self.selected_item = 0
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                if self.selected_item == 0:
                    self.SwitchToScene(GameScene())
                if self.selected_item == 1:
                    self.SwitchToScene(PreferencesScene())
                if self.selected_item == 2:
                    self.Terminate()
        
        if pressed_keys[pygame.K_UP]: 
            self.selected_item -= 1
            if(self.selected_item < 0):
                self.selected_item =  len(self.menu_items) - 1
        elif pressed_keys[pygame.K_DOWN]: 
            self.selected_item = (self.selected_item + 1) % len(self.menu_items)

    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("comicsansms", 20)
        offset = 0
        for index in range(0, len(self.menu_items)):
            if index == self.selected_item:
                text = font.render(self.menu_items[index], True, (0, 255, 0))
            else:
                text = font.render(self.menu_items[index], True, (255, 255, 255))

            screen.blit(text, (150, 150 + offset - text.get_height() // 2))
            offset += 20
        
        
class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass
        
    def Update(self):
        pass
    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))

class PreferencesScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass
        
    def Update(self):
        pass
    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((200, 100, 255))

run_game(400, 300, 60, TitleScene())