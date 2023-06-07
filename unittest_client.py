from unittest import TestCase, main
from game_client import Client

class UnitTestClient(TestCase):
    def setUp(self):
        self.client = Client()

    def test_make_move(self):
        # Simulate the client choosing 'rock'
        move = "rock"
        self.client.make_move(move)

        # Get the current GUI output
        gui_output = self.client.get_gui_output()

        # Modify the assertion to check the expected GUI output
        expected_output = "You: paper"
        self.assertEqual(gui_output, expected_output)

if __name__ == '__main__':
    main()