class Automaton(object):

    def __init__(self, states):
        self.states = states

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        current_state = self.states[0]
        for command in commands:
            if command == "1":
                if current_state == self.states[0]:
                    new_state = self.states[1]
                elif current_state == self.states[1]:
                    new_state = self.states[1]
                else:
                    new_state = self.states[1]
            else:
                if current_state == self.states[0]:
                    new_state = self.states[0]
                elif current_state == self.states[1]:
                    new_state = self.states[2]
                else:
                    new_state = self.states[1]
            current_state = new_state
        return True if current_state == self.states[1] else False

my_automaton = Automaton(["q1", "q2", "q3"])

print(my_automaton.read_commands(["1", "0", "0", "1"]))
# Do anything necessary to set up your automaton's states, q1, q2, and q3.