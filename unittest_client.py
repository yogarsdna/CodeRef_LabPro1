import unittest
from game_client import Client

class MockGUI:
    def __init__(self):
        self.display = ""
    
    def set_display(self, value):
        self.display = value
    
    def get_display(self):
        return self.display

class TestClient(unittest.TestCase):
    def test_gui_display(self):
        client = Client()
        client.gui = MockGUI()  # Replace the client's GUI with the MockGUI
        
        # Start the game
        client.start_game()
        
        # Run the game for 3 rounds
        for _ in range(3):
            # Simulate player choosing "rock"
            client.make_move("rock")
            
            # Verify that the GUI displays "paper"
            display = client.gui.get_display()
            self.assertTrue(display == "paper")
        
        # Stop the game
        client.stop_game()

if __name__ == '__main__':
    unittest.main()