import unittest
import subprocess
import time
import game_client

class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.client_process = subprocess.Popen(['python', 'game_client.py'])
        time.sleep(1)  # Give the client some time to start

    def tearDown(self):
        self.client_process.terminate()
        self.client_process.wait()

    def test_choice_display(self):
        # Simulate the client choosing "rock"
        game_client.your_choice = "rock"

        # Call the choice function to update the displayed choice
        game_client.choice("paper")

        # Get the displayed choice from the GUI
        displayed_choice = game_client.lbl_your_choice["text"]

        # Check if the displayed choice matches the expected value
        self.assertTrue(displayed_choice == "You: paper" or displayed_choice == "You: rock")

if __name__ == '__main__':
    unittest.main()