import pygame

UNIT_LENGTH = 18

class Disk:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win, color_center, color_out):
        pygame.draw.circle(win, color_out, (self.x, self.y), UNIT_LENGTH, 0)
        pygame.draw.circle(win, color_center, (self.x, self.y), UNIT_LENGTH/5, 0)


def draw_grid(win, x, y, k, color):
    for cx in range(x, 1200, k):
        pygame.draw.line(win, color, (cx, 0), (cx, 560), 1)

    for cy in range(y, 560, k):
        pygame.draw.line(win, color, (0, cy), (1200, cy), 1)


def draw_disks(win, disks, color_center, color_out):
    for disk in disks:
        disk.draw(win, color_center, color_out)

def draw_state(win, disks_state, k, offset):
    # disks_state is a dictionary with the following keys:
    # ["grid_coordinate", "current_packing", "fully_contained",
    # "currently_checking", "current_best"]

    # draw a gray opaque rectangle on grid_coordiante
    if disks_state["grid_coordinate"] is not None:
        s = pygame.Surface((UNIT_LENGTH*k, UNIT_LENGTH*k), pygame.SRCALPHA)
        s.fill((192, 192, 192, 100))
        win.blit(s, disks_state["grid_coordinate"])
    
    for disk in disks_state["current_packing"]:
        disk.draw(win, "black", "red")
    
    for disk in disks_state["fully_contained"]:
        disk.draw(win, "black", (173, 216, 230))
    
    for disk in disks_state["currently_checking"]:
        disk.draw(win, "black", (7, 22, 48))
    
    for disk in disks_state["current_best"]:
        disk.draw(win, "black", (0, 128, 0))
    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1200, 560))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # clear the screen
        screen.fill("white")
        draw_grid(screen, 20, 30, 100, "gray")

        Disk(100, 100).draw(screen, "black", "red")

        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
