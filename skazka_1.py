import time
import random


class KurochkaRyaba(object):
  def __init__(self):
    print('I byla u nih kurochka ryaba')
    # Play with this number to increase the number of normal eggs
    random.seed(2)

  def lay_egg(self):
    egg_type = random.randint(0,10)
    if egg_type <= 5:
      egg = 'Normal'
    else:
      egg = 'Gold'
    print('The Kurochka has layed a {} egg'.format(egg))
    return egg


class DedAndBabka(object):
  def __init__(self):
    print('Zhili-byli ded da baba')
    self.kurochka = KurochkaRyaba()

  def live(self):
    while True:
      egg = self.kurochka.lay_egg()
      if egg == 'Normal':
        # Reduce this number for a faster simulation
        time.sleep(1)
      elif egg == 'Gold':
        break
      else:
        print('Unknown egg type!')
        exit(1)


def main():
  # Start Skazka
  ded_da_baba = DedAndBabka()
  # Zhili-byli
  ded_da_baba.live()
  # End Skazka
  print('Vot i skazke konec.')


main()
