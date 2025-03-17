import pygame

pygame.init()

print("Before quitting:")
for module in [
    "display", "event", "joystick", "mixer", "mouse",
    "keyboard", "font", "image", "time"
]:
    status = pygame.get_init() if hasattr(pygame, "get_init") else None
    print(f"{module}: {status}")

pygame.display.quit()
# pygame.event.quit()
pygame.joystick.quit()
pygame.mixer.quit()
# pygame.mouse.set_visible(False)
pygame.font.quit()
pygame.quit()
print("After quitting")