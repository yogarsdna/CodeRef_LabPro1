import unittest

def pickRockPaperScissor(picked, output):
    if output == picked :
        return True
    else :
        return False
    
def yourTurnButton(your_turn, button_enable):
    if your_turn == True and button_enable == True:
        return True
    else :
        return False
    
def greetingString(state, client1_name, client2_name, greetings):
    if state == "client 1" and greetings == "Hello " + client1_name:
        return True
    elif state == "client 2" and greetings == "Hello " + client2_name:
        return True
    else : return False        
        

class UnitTest (unittest.TestCase):
    def test_pickedChoice_rockOutputPaper_falseReturn(self):
        result = pickRockPaperScissor("rock", "paper")
        self.assertFalse(result)

    def test_pickedChoice_roOutputPaper_falseReturn(self):
        result = pickRockPaperScissor("scissor", "rock")
        self.assertFalse(result)

    def test_pickedChoice_rockOutputRock_trueReturn(self):
        result = pickRockPaperScissor("rock", "rock")
        self.assertTrue(result)

    def test_yourTurn_rockOutputRock_falseReturn(self):
        result = yourTurnButton(True, False)
        self.assertFalse(result)

    def test_yourTurn_OutputRock_falseReturn(self):
        result = yourTurnButton(False, True)
        self.assertFalse(result)

    def test_yourTurn_rsOutputRock_falseReturn(self):
        result = yourTurnButton(True, True)
        self.assertTrue(result)

    def test_Turn_rsOutputRock_falseReturn(self):
        result = greetingString("client 1", "John", "Zulu", "Hello Zulu")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()