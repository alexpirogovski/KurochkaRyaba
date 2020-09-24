import time  # Need this to sleep
import random  # Need this to get random numbers

class CanBreakEgg(object):
  # Insert __init__ function
  def can_break_egg(calling_class):
    called_by = calling_class.__class__.__name__
    if called_by == 'DedAndBabka':
      print('{} bili-bili - ne razbili'.format(called_by))
      return False
    else:
      print('Egg is broken by {}'.format(called_by))
      return True


class KurochkaRyaba(CanBreakEgg):
  def __init__(self):
    print('I byla u nih kurochka ryaba.')  # This will be printed second
    # Increase with this number to get more normal eggs
    random.seed(2)

  def lay_egg(self):
    egg_type = bool(random.getrandbits(1))  # This is the fastest according to https://stackoverflow.com/questions/6824681/get-a-random-boolean-in-python
    egg = 'Normal' if egg_type else 'Golden'  # Python syntax
    print('The Kurochka has layed a {} egg.'.format(egg))
    return egg


class DedAndBabka(CanBreakEgg):
  def __init__(self):
    print('Zhili-byli ded da baba.')  # This will be printed first
    self.can_break_egg()
    self.kurochka = KurochkaRyaba()

  def live(self):
    while True:
      egg = self.kurochka.lay_egg()
      if egg == 'Normal':
        # Reduce this number for a faster simulation
        time.sleep(1)
      elif egg == 'Golden':
        for someone in [self, self.kurochka]:
          print('{} tried to break egg')
          if someone.can_break_egg():
            break
        break


def main():
  # Start Skazka about Ded and Babka
  ded_da_babka = DedAndBabka()
  # Zhili-byli
  ded_da_babka.live()
  # End Skazka
  print('Vot i skazke konec.')


main()
