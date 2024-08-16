import pygame

pygame.init()


tile_size = 64*1.5

white = (255, 255, 255)

grass_img = pygame.image.load("tiles/grass.png")
path_img = pygame.image.load("tiles/path.png")


grass_img = pygame.transform.scale(grass_img, (tile_size, tile_size))
path_img = pygame.transform.scale(path_img, (tile_size, tile_size))


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

screen_width = len(tilemap[0]) * tile_size
screen_height = len(tilemap) * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))


def draw_tilemap():
    # Iterates through each element in the 2d array
    for row in range(len(tilemap)):
        for col in range(len(tilemap[row])):
            tile_type = tilemap[row][col] # Finds the tile type (1 or 0)
            tile_image = tile_images[tile_type] # Matches it with the image using the dictionary
            screen.blit(tile_image, (col * tile_size, row * tile_size)) # Displays them in order using their position in the array and size

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)  # Fill the screen with white

    draw_tilemap()  # Draw the tilemap

    pygame.display.flip()  # Update the display

pygame.quit()
