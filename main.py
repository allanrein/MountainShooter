import pygame

print("Setup Starting...")
pygame.init()
window = pygame.display.set_mode((800, 600))
print("Setup Complete!")

print("Start Loop")

while True:
  #check for all events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit() #Close Window 
      quit()  #end pygame loop
  pass
