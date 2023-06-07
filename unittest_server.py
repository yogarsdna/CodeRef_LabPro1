from unittest import TestCase, main
from unittest.mock import patch
from game_server import Server
from game_client import Client

class UnitTestServer(TestCase):
    def setUp(self):
        self.server = Server()

    def test_game_rounds(self):
        # Create two clients
        client1 = Client()
        client2 = Client()

        # Start the game
        self.server.start_game()

        # Register clients
        self.server.register_client(client1)
        self.server.register_client(client2)

        # Patch the make_move method of the client to modify the behavior
        with patch.object(Client, 'make_move') as mock_make_move:
            def modified_make_move(move):
                if move == "rock":
                    return "paper"
                else:
                    return move

            # Set the side effect of the mock make_move method
            mock_make_move.side_effect = modified_make_move

            # Run the game round
            self.server.run_game_round()

            # Assert that client1 made the correct move
            mock_make_move.assert_called_with("rock")

        # Stop the game
        self.server.stop_game()

if __name__ == '__main__':
    main()