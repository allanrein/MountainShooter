from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.Const import WIN_WIDTH

class EntityMediator:

  @staticmethod
  def __verify_collision_window(ent: Entity):
    if isinstance(ent, Entity):
      # Handle window collision logic here
      if ent.rect.right < 0:
        ent.healthy = 0
    if isinstance(ent, PlayerShot):
      if ent.rect.left >= WIN_WIDTH:
        ent.healthy = 0

  @staticmethod
  def verify_collision(entity_list: list[Entity]):
    for i in range(len(entity_list)):
      test_entity = entity_list[i]
      EntityMediator.__verify_collision_window(test_entity)
      # for j in range(i + 1, len(entity_list)):
      #   if entity_list[i].rect.colliderect(entity_list[j].rect):
            # Handle collision logic here

  @staticmethod
  def verify_health(entity_list: list[Entity]):
    for ent in entity_list:
      if ent.healthy <= 0:
        entity_list.remove(ent)