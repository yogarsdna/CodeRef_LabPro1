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

        # Set the displayed choice directly
        displayed_choice = "rock"
        test_server.displayed_choice = displayed_choice

        # Check if the displayed choice matches the expected value
        self.assertTrue(displayed_choice == "You: rock")

if __name__ == '__main__':
    unittest.main()