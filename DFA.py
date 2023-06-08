class DFA:

    def __init__(self, alphabet, states, initial_state, accepting_states,
               transitions):
        self.alphabet = alphabet
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions
  
    def minimize(self):
        # Step 1: Initialize the table with all pairs of states (Qi, Qj) where i < j
        table = {}
        for i, s1 in enumerate(self.states):
            for s2 in self.states[i+1:]:
                table[(s1, s2)] = False

        # Step 2: Mark all pairs (Qi, Qj) where Qi is an accepting state and Qj is not an accepting state
        for s1 in self.accepting_states:
            for s2 in set(self.states) - set(self.accepting_states):
                table[(s1, s2)] = True
                table[(s2, s1)] = True

        # Step 3: Repeat until no further changes occur
        refined = True
        while refined:
            refined = False

            # Step 3a: Iterate over all pairs (Qi, Qj) where i < j and table[(Qi, Qj)] == False
            for s1 in self.states:
                for s2 in self.states:
                    if s1 < s2 and not table[(s1, s2)]:
                        # Step 3b: Iterate over all symbols in the alphabet
                        for symbol in self.alphabet:
                            next_s1 = self.transitions[s1][symbol]
                            next_s2 = self.transitions[s2][symbol]

                            # Step 3c: If (next_s1, next_s2) is marked or not in the table, mark (Qi, Qj)
                            if (next_s1, next_s2) in table and table[(next_s1, next_s2)]:
                                table[(s1, s2)] = True
                                table[(s2, s1)] = True
                            elif (next_s2, next_s1) in table and table[(next_s2, next_s1)]:
                                    table[(s1, s2)] = True
                                    table[(s2, s1)] = True

        # Step 4: Construct the minimized DFA
        minimized_states = []
        minimized_transitions = {}
        minimized_initial_state = None
        minimized_accepting_states = set()

        # Step 4a: Create a new state for each equivalence class
        equivalence_classes = {}
        for state in self.states:
            equivalence_class = None
            for key in equivalence_classes.keys():
                if (state, key) not in table and (key, state) not in table:
                    equivalence_class = key
                    break

            if equivalence_class is None:
                equivalence_class = state

            equivalence_classes[equivalence_class] = equivalence_classes.get(equivalence_class, set()) | {state}

        # Step 4b: Add the new states to the minimized DFA
        for state_set in equivalence_classes.values():
            new_state = tuple(sorted(list(state_set)))
            minimized_states.append(new_state)

            if self.initial_state in state_set:
                minimized_initial_state = new_state

            if len(state_set & set(self.accepting_states)) > 0:
                minimized_accepting_states.add(new_state)

            transitions = {}
            for symbol in self.alphabet:
                next_states = set()
                for state in state_set:
                    next_state = self.transitions[state][symbol]
                    next_states.add(next_state)

                next_state_set = None
                for key, value in equivalence_classes.items():
                    if value == next_states:
                        next_state_set = key

                transitions[symbol] = next_state_set

            minimized_transitions[new_state] = transitions

        return DFA(
               self.alphabet,
               minimized_states,
               minimized_initial_state,
               minimized_accepting_states,
               minimized_transitions,)
