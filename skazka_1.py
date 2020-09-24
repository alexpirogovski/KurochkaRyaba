import time  # Need this to sleep
import random  # Need this to get random numbers


class KurochkaRyaba(object):
  def __init__(self):
    print('I byla u nih kurochka ryaba.')  # This will be printed second
    # Increase with this number to get more normal eggs
    random.seed(2)

  def lay_egg(self):
    egg_type = bool(random.getrandbits(1))  # This is the fastest according to https://stackoverflow.com/questions/6824681/get-a-random-boolean-in-python
    egg = 'Normal' if egg_type else 'Golden'  # Python syntax
    print('The Kurochka has layed a {} egg.'.format(egg))
    return egg


class DedAndBabka(object):
  def __init__(self):
    print('Zhili-byli ded da baba.')  # This will be printed first
    self.kurochka = KurochkaRyaba()

  def live(self):
    while True:
      egg = self.kurochka.lay_egg()
      if egg == 'Normal':
        # Reduce this number for a faster simulation
        time.sleep(1)
      elif egg == 'Golden':
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
