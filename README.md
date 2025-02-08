# Understanding the Perceptron: My Learning Journey

## 🚀 Introduction
This project represents my **learning journey** toward understanding the **Perceptron**, one of the most fundamental building blocks of machine learning. I implemented a **basic perceptron** and gradually improved my understanding by integrating training and visualization functions.



Through this exploration, I learned:
- What the **Perceptron model** is and how it functions.
- The **Perceptron Learning Rule** and how it adjusts weights and bias.
- The **geometric interpretation** of how training modifies the decision boundary.
- How to **visualize training progress** by plotting the evolution of the decision boundary.

---

## 🧠 **Core Concepts of the Perceptron**
### **1️⃣ The Perceptron Model**
A perceptron is a **simple artificial neuron** that takes an input vector, computes a weighted sum, adds a bias, and applies an **activation function** to determine the output:

\[
 y = f(w_1 x_1 + w_2 x_2 + b) 
\]

where:
- \( x_1, x_2 \) are inputs
- \( w_1, w_2 \) are weights
- \( b \) is the bias
- \( f(x) \) is the activation function (in our case, a step function).

![alt text](docs/img/perceptron-diagram.png)

### **2️⃣ The Perceptron Learning Rule**
The perceptron **updates its weights and bias** using the following rule:

\[
 w_{new} = w_{old} + \alpha (y - \hat{y}) x
\]
\[
 b_{new} = b_{old} + \alpha (y - \hat{y})
\]

where:
- \( \alpha \) is the **learning rate**.
- \( y \) is the **actual class label**.
- \( \hat{y} \) is the **predicted output**.
- \( (y - \hat{y}) \) is the **error**.

This rule ensures that the perceptron adjusts its decision boundary **gradually** to minimize classification errors.

### **3️⃣ Geometric Interpretation of Training**
The perceptron represents a **linear decision boundary**, just like a line equation:

\[
 x_2 = \frac{-w_1}{w_2} x_1 + \frac{-b}{w_2}
\]

- **Weights control the slope** of the boundary.
- **Bias shifts the boundary** up or down.
- Training **adjusts both** until all points are correctly classified.

---

## 📌 **Project Overview**
### **1️⃣ Perceptron Implementation (`src/perceptron.py`)**
- Implements the **perceptron model**.
- Includes a **training function** that applies the perceptron learning rule.
- Stores **training history** to visualize how the decision boundary evolves.

### **2️⃣ Main Program (`main.py`)**
- **Trains** the perceptron using the **AND gate dataset**.
- **Tests** the perceptron to verify its predictions.
- **Plots** how the decision boundary changes over time.

---

## 🔥 **Visualizing the Perceptron's Learning Process**
One of the **most insightful aspects** of this project is visualizing **how the decision boundary changes** as training progresses. I implemented a **plotting function** that:
- Shows **how the perceptron gradually tunes itself**.
- Draws multiple decision boundaries over different **epochs**.
- Provides **intuition** into the learning process.

### **Decision Boundary Evolution**
The following images illustrate how the perceptron's decision boundary evolves during training:

#### **Trail 1**
![Trail 1](docs/img/plot_1.png)

#### **Trail 3**
![Trail 3](docs/img/plot_2.png)

#### **Trail 7**
![Trail 7](docs/img/plot_3.png)

At the beginning of training:
- The perceptron’s decision boundary is **randomly initialized**.

As training progresses:
- The perceptron **adjusts weights and bias**, shifting the boundary toward correct classifications.

At convergence:
- The perceptron correctly **separates all data points** with an optimal decision boundary.

---

## 🏆 **Key Takeaways from My Journey**
✅ The perceptron **represents a linear decision boundary**.
✅ The **learning rule adjusts weights and bias** to fit the data.
✅ The **learning rate** controls the step size of updates.
✅ Visualizing training helps **develop intuition** about how the perceptron learns.
✅ The perceptron **can only classify linearly separable data** (AND, OR) but **not XOR**.

---

## 🎯 **Next Steps**
Now that I understand the single perceptron, I plan to explore:
- **Multi-Layer Perceptrons (MLP)** for non-linear problems like XOR.
- **Other activation functions** (Sigmoid, ReLU) for deeper models.
- **Gradient Descent and Backpropagation** for complex learning.

🚀 **This journey has just begun!** 🚀

---

## 📂 **Project Structure**
```
.
├── README.md
├── docs
│   └── img
│       ├── plot_1.png
│       ├── plot_2.png
│       ├── plot_3.png
├── main.py
├── requirements.txt
└── src
    ├── __pycache__
    ├── perceptron.py
```

---

## 📌 **How to Run the Project**
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the main script:**
   ```bash
   python main.py
   ```

This will **train the perceptron**, print results, and **visualize training evolution**.

---

## 🎉 **Conclusion**
This project helped me **understand perceptrons from theory to implementation**. I now have an **intuitive grasp** of how perceptrons learn and adjust decision boundaries. Next, I will move to **multi-layer networks** to solve more complex problems!
