import numpy as np

class QLearningAgent:
    def __init__(self, state_size=10, action_size=2, alpha=0.1, gamma=0.9, epsilon=0.1):
        # State: discretized queue lengths (0-9 for simplicity)
        self.q_table = np.zeros((state_size, state_size, action_size))
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount
        self.epsilon = epsilon  # Exploration

    def discretize_state(self, state):
        # Cap queues at 9
        return min(state[0], 9), min(state[1], 9)

    def choose_action(self, state):
        disc_state = self.discretize_state(state)
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, 2)  # Explore: NS green (0) or EW green (1)
        return np.argmax(self.q_table[disc_state[0], disc_state[1]])

    def update(self, state, action, reward, next_state):
        disc_state = self.discretize_state(state)
        disc_next = self.discretize_state(next_state)
        best_next = np.max(self.q_table[disc_next[0], disc_next[1]])
        self.q_table[disc_state[0], disc_state[1], action] += self.alpha * (
            reward + self.gamma * best_next - self.q_table[disc_state[0], disc_state[1], action]
        )

    def get_reward(self, prev_queues, curr_queues):
        # Reward: negative of total queue length change
        return - (curr_queues[0] + curr_queues[1]) + (prev_queues[0] + prev_queues[1])