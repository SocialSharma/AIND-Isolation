"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = game_agent.MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2)

    def test_gameplay(self):
    	winner, history, outcome = self.game.play()
    	self.assertIn(outcome, ["timeout", "forfeit", "illegal move"])


    """def test_isint(self):
    	self.assertEqual(1, self.player1.max_value(self.game, 3))

    def test_istuple(self):
    	self.assertEqual((1, 1), self.player1.minimax(self.game, 3))"""

if __name__ == '__main__':
    unittest.main()
