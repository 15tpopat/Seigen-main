import pygame

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Intiate the screen with the given width and height
    screen = pygame.display.set_mode([600, 400])

    # Create the appropriate groupings of the sprites
    allSpritesGroup = pygame.sprite.Group()

    # Let the game run until the user clicks the exit button
    exit = False

    # Manage how often the screen updates
    clock = pygame.time.Clock()

    while not exit:
        # --- Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # --- Game logic
        # Call the update() method on all the sprites
        allSpritesGroup.update()

        # Clear the screen
        screen.fill((28, 157, 255))

        # Draw all the sprites
        allSpritesGroup.draw(screen)

        # Update the screen with what we've drawn
        pygame.display.flip()

        # Limit to 20 frames per second
        clock.tick(60)

    pygame.quit()
