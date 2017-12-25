from turing_machine import TuringMachine

initial_state = "A",
accepting_states = ["final", "A", "B", "C", "D", "E", "F"],
transition_function = {("A","0"):("B", "1", "R"),
                       ("A","1"):("D", "0", "L"),
                       ("B","0"):("C","1", "R"),
                       ("B","1"):("F","0", "R"),
                       ("C","0"):("C","1", "L"),
                       ("C","1"):("A","1", "L"),
                       ("D","0"):("E","0", "L"),
                       ("D","1"):("A","1", "R"),
                       ("E","0"):("A","1", "L"),
                       ("E","1"):("B","0", "R"),
                       ("F","0"):("C","0", "R"),
                       ("F","1"):("E","0", "R"),
                       }
final_states = {"final"}

t = TuringMachine("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                  initial_state = "A",
                  final_states = final_states,
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())

for i in range(1230229):
    t.step()

print("Result of the Turing machine calculation:")
print(t.get_tape())
