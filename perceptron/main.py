from src.perceptron import Perceptron, np


# Training data
input_data =np.array([[0, 0], [0, 1], [1, 0], [1, 1]])   # Inputs
target_data = np.array([0, 0, 0, 1])  # Outputs (AND logic)


# Creating the AND gate perceptron
and_gate = Perceptron(input_size=2, learning_rate=0.08, epochs=100)

# Training
and_gate.train(input_data, target_data)


# Testing
print("\nTesting AND Gate:")
for x in input_data:
    print(f"Input: {x}, Prediction: {and_gate.predict(x)}")


and_gate.plot_training()