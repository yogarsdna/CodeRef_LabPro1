import unittest
import subprocess
import time
import game_server

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        self.server_process = subprocess.Popen(['python', 'game_server.py'])
        time.sleep(1)  # Give the server some time to start

    def tearDown(self):
        self.server_process.terminate()
        self.server_process.wait()

    def test_displayed_choice(self):
        # Create an instance of the server
        test_server = game_server.Server()

        # Simulate the client choosing "rock"
        client_choice = "rock"

        # Simulate the server receiving the client's choice
        test_server.handle_client_choice(client_choice)

        # Get the displayed choice from the server
        displayed_choice = test_server.get_displayed_choice()

        # Check if the displayed choice matches the expected value
        expected_choice = "paper"
        self.assertTrue(displayed_choice == expected_choice)

if __name__ == '__main__':
    unittest.main()
