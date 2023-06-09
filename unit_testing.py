import unittest

def pick_rps(picked, output):
    if output == picked :
        return True
    
    else:
        return False
    
def turn_button(your_turn, button):
    if your_turn == True and button == True:
        return True
    
    elif your_turn == False and button == False:
        return True
    
    else:
        return False
    
def client_name(state, client1_name, client2_name, greetings):
    if state == "client 1" and greetings == "Name: " + client1_name:
        return True
    
    elif state == "client 2" and greetings == "Name: " + client2_name:
        return True
    
    else:
        return False        
        

class UnitTest(unittest.TestCase):
    def test_pick_rps_rock_paper(self):
        result = pick_rps("rock", "paper")
        self.assertFalse(result)

    def test_pick_rps_scissor_rock(self):
        result = pick_rps("scissor", "rock")
        self.assertFalse(result)

    def test_pick_rps_rock_rock(self):
        result = pick_rps("rock", "rock")
        self.assertTrue(result)

    def test_turn_button_your_disable(self):
        result = turn_button(True, False)
        self.assertFalse(result)

    def test_turn_button_not_enable(self):
        result = turn_button(False, True)
        self.assertFalse(result)

    def test_turn_button_your_enable(self):
        result = turn_button(True, True)
        self.assertTrue(result)
    
    def test_turn_button_not_disable(self):
        result = turn_button(False, False)
        self.assertTrue(result)

    def test_client_name_client1_client2(self):
        result = client_name("client 1", "Yog", "Zulu", "Name: Zulu")
        self.assertFalse(result)

    def test_client_name_client2_client1(self):
        result = client_name("client 2", "Yog", "Zulu", "Name: Yog")
        self.assertFalse(result)

    def test_client_name_client1_client1(self):
        result = client_name("client 1", "Yog", "Zulu", "Name: Yog")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()