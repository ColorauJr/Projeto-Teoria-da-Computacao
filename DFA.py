
class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def map_states_to_integers(self):
        state_mapping = {}
        next_integer = 0
        for state in self.states:
            state_mapping[state] = next_integer
            next_integer += 1
        return state_mapping                        
    
    def convert_to_integers(self, state_mapping):
        transitions_int = {}
        for state, transition in self.transitions.items():
            state_int = state_mapping[state]
            transition_int = {}
            for symbol, next_state in transition.items():
                next_state_int = state_mapping[next_state]
                transition_int[symbol] = next_state_int
            transitions_int[state_int] = transition_int
        return transitions_int

    def convert_to_strings(self, state_mapping):
        transitions_str = {}
        for state_int, transition in self.transitions.items():
            state_str = state_mapping[state_int]
            transition_str = {}
            for symbol, next_state_int in transition.items():
                next_state_str = state_mapping[next_state_int]
                transition_str[symbol] = next_state_str
            transitions_str[state_str] = transition_str
        return transitions_str

    def is_equivalent(self, p, q, partition):
        for symbol in self.alphabet:
            next_p = self.transitions[p][symbol]
            next_q = self.transitions[q][symbol]
            if partition[int(next_p)] != partition[int(next_q)]:
                return False
        return True

    def minimize(self):
        state_mapping = self.map_states_to_integers()
        transitions_int = self.convert_to_integers(state_mapping)

        # Step 1: Initialize the partition with two groups: accepting and non-accepting states
        partition = [{s for s in self.states if s in self.accepting_states},
                     {s for s in self.states if s not in self.accepting_states}]

        # Step 2: Refine the partition until no further changes occur
        refined = True
        while refined:
            refined = False
            new_partition = []

            for group in partition:
                split = False
                for p in group:
                    for q in group:
                        if p != q and self.is_equivalent(p, q, partition):
                            split = True
                            break
                    if split:
                        break

                if split:
                    refined = True
                    new_groups = [set([p]), set([q])]
                    for r in group:
                        if r != p and r != q:
                            for i, new_group in enumerate(new_groups):
                                if self.is_equivalent(r, list(new_group)[0], partition):
                                    new_group.add(r)
                                    break
                            else:
                                new_groups.append(set([r]))
                    new_partition.extend(new_groups)
                else:
                    new_partition.append(group)

            partition = new_partition

        # Step 3: Construct the minimized DFA
        minimized_states = []
        minimized_transitions = {}
        minimized_initial_state = None
        minimized_accepting_states = []

        for group in partition:
            representative = list(group)[0]
            minimized_states.append(representative)
            minimized_transitions[state_mapping[representative]] = {}

            for symbol in self.alphabet:
                next_state = self.transitions[representative][symbol]

                for i, subgroup in enumerate(partition):
                    if next_state in subgroup:
                        minimized_transitions[state_mapping[representative]][symbol] = state_mapping[next_state]
                        break

            if self.initial_state in group:
                minimized_initial_state = state_mapping[representative]

            if any(state in self.accepting_states for state in group):
                minimized_accepting_states.append(state_mapping[representative])

        minimized_states_str = self.convert_to_strings(state_mapping)
        minimized_dfa = DFA(minimized_states, self.alphabet, minimized_transitions,
                            minimized_initial_state, minimized_accepting_states)

        return minimized_dfa
    