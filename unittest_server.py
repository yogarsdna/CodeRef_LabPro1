import unittest
from game_server import Server

class TestServer(unittest.TestCase):
    def test_game_logic(self):
        server = Server()
        
        # Start the game
        server.start_game()
        
        # Run the game for 3 rounds
        for _ in range(3):
            # Simulate player choosing "rock"
            server.receive_move("rock")
            
            # Verify that the server's response is "paper"
            response = server.get_response()
            self.assertTrue(response == "paper")
        
        # Stop the game
        server.stop_game()

if __name__ == '__main__':
    unittest.main()