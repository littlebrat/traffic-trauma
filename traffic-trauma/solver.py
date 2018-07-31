
class Solver(object):

    def __init__(self, game):
        self.__game = game

    def run(self):
        pass

class NaiveSolver(Solver):

    def __init__(self, game):
        super().__init__(game)

    def initial_states(self):
        self.__game.generate_initial_state()

    def run(self):
        pass