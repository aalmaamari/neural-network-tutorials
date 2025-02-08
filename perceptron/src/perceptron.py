import numpy as np
import matplotlib.pyplot as plt



def step_function(x):
    return 1 if x >= 0 else 0


class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.random.randn(input_size)
        self.bias = np.random.randn()
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.perceptron_history = []


    def predict(self, x):
        linear_output = np.dot(x, self.weights) + self.bias
        return step_function(linear_output)

    def train(self, X, y):
        for epoch in range(self.epochs):
            total_error =  0
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = y[i] - prediction

                self.weights = self.weights + (self.learning_rate * error * X[i])
                self.bias = self.bias + (self.learning_rate * error)
                total_error = total_error + abs(error)
                
            
            print(f"Epoch {epoch+1}, Total Errors: {total_error}")
            

            if total_error == 0:
                break
            self.perceptron_history.append((self.weights.copy(), self.bias))
            
    def plot_training(self, history_length=7):
        """ history_lengthis the Number of epochs to display from training history """
        # Plotting Decision boundary (The Perceptron Training History)
        plt.figure(figsize=(6, 6))
        plt.xlim(-0.5, 1.5)
        plt.ylim(-0.5, 1.5)

        first_logic_input = [0, 0, 1, 1]
        second_logic_input = [0, 1, 0, 1]
        plt.scatter(first_logic_input, second_logic_input, color='red', marker='o', label='Points')
        
        
        # Decision boundary = -(self.weights[0] * x_vals + self.bias) / self.weights[1]
        x_vals = np.linspace(-0.5, 1.5, 100)
        for index, item in enumerate(self.perceptron_history):
            if (index >= len(self.perceptron_history) - history_length ):
                y_vals = - (item[0][0] * x_vals + item[1])/item[0][1]  
                label = "epoch " + str(index)     
                plt.plot(x_vals, y_vals,  label = label)


        plt.xlabel("Input 1")
        plt.ylabel("Input 2")
        plt.title("Perceptron Decision Boundary Evolution (AND Gate)")
        plt.legend()
        plt.grid()
        plt.show()
        