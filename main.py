import pygame

pygame.init()


tile_size = 64*1.5
tower_height = 135
tower_width = tower_height/3
bee_size = 48

white = (255, 255, 255)
black = (0, 0, 0)

grass_img = pygame.image.load("tiles/grass.png")
path_img = pygame.image.load("tiles/path.png")
bee_sprite_sheet = pygame.image.load("bees/bee.png")
tower_sprite_sheet = pygame.image.load("towers/towerBase.png")  #192x192
weapon_img_L1 = pygame.image.load("towers/towerWeaponL1.png")

grass_img = pygame.transform.scale(grass_img, (tile_size, tile_size))
path_img = pygame.transform.scale(path_img, (tile_size, tile_size))
tower_sprite_sheet = pygame.transform.scale(tower_sprite_sheet, (tower_height,tower_height))
#weapon_img_L1 = pygame.transform.scale(weapon_img_L1, (60,60))

tile_images = {
    0: grass_img,
    1: path_img,
}


tilemap = [
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
]

# Sets the screen width and height according to the tile size and number
screen_width = len(tilemap[0]) * tile_size
screen_height = len(tilemap) * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))



class Map:
    def __init__(self, tilemap, tile_images, tile_size):
        self.tilemap = tilemap 
        self.tile_images = tile_images
        self.tile_size = tile_size


    def draw_tilemap(self):
        # Iterates through each element in the 2d array
        for row in range(len(self.tilemap)):
            for col in range(len(self.tilemap[row])):
                tile_type = self.tilemap[row][col] # Finds the tile type at a position (1 or 0)
                tile_image = self.tile_images[tile_type] # Matches it with the image using the dictionary
                screen.blit(tile_image, (col * self.tile_size, row * self.tile_size)) # Displays them in order using their position in the array and size



class Bees:
    def __init__(self, sheet, size: int, color: tuple):
        self.sheet = sheet   # TODO rename this to sprite_sheet
        self.size = size
        self.color = color

    def get_image(self, frame, width, height):

        # Creates a surface to blit the image onto
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0,0), ((frame*width), 0, width, height))

        # Sets the black background to be transparent
        image.set_colorkey(self.color)

        return image
    
    def draw_bee(self, frame, position):
        frame_0 = self.get_image(frame, bee_size, bee_size)

        # Blits the image onto the screen
        screen.blit(frame_0, position)
        

class Towers: #TODO make sure this class actually works and loads a tower
    def __init__(self, sheet, size: int, color: tuple):
        self.sheet = sheet # TODO rename this to sprite_sheet
        self.size = size
        self.color = color

    def get_image(self, level, width, height):

        # Creates a surface to blit the image onto
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0,0), ((level*width), 0, width, height))

        # Sets the black background to be transparent
        image.set_colorkey(self.color)

        return image
    
    def draw_tower(self, level, position):
        level_0 = self.get_image(level, tower_width, tower_height)

        # Blits the image onto the screen
        screen.blit(level_0, position)
        

Background = Map(tilemap, tile_images, tile_size)



Bee = Bees(bee_sprite_sheet, bee_size, black)

Tower = Towers(tower_sprite_sheet, tower_height, black)

# Set up for the bee animation
animation_list = []
animation_steps = 6
last_update = pygame.time.get_ticks()
animation_cooldown = 100 # The time between frames
frame = 0

# Append each frame of bee animation to a list
for x in range(animation_steps):
    animation_list.append(Bee.get_image(x, bee_size, bee_size))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)  # Fill the screen with white

    # Load background
    Background.draw_tilemap()  # Draw the tilemap


    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time # Resets the last update each time a frame updates
        if frame >= animation_steps: # Make sure the animation loops from the start again
            frame = 0

    # Display bee
    screen.blit(animation_list[frame], (0,0))

    # Display tower
    screen.blit(tower_sprite_sheet, (60,60))
    Tower.draw_tower(2, (200,200))
    screen.blit(weapon_img_L1, (180,200))
    
    pygame.display.flip()  # Update the display


pygame.quit()
