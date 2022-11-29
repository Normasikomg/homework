class Tomato:

    states = {0: 'seed', 1: 'green', 2: 'orange', 3: 'red'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Sadovnik rabotaet...')
        self._plant.grow_all()
        print('Sadovnik zakonchil')

    def harvest(self):
        print('Sadovnik sobiraet urozhay...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Sadovnik zakonchil')
        else:
            print('Rano. Pomidori ne virosli.')

    @staticmethod
    def knowledge_base():
        print('''Sobirat nuzhno tolko krasnie pomidory''')

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()