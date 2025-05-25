
## Overview  
This project bridges **functional analysis** and **operator learning** to (more rigorously) analyze how deep neural networks approximate nonlinear operators between Sobolev spaces. 

The goal of this project is to characterize/study the interplay between neural network architecture, optimization dynamics, and approximation error in high-dimensional function spaces, with applications to learning solution operators of PDEs.  

---

## Some background info on Operator Learning
What's operator learning exactly?

So, in normal machine learning, you often try to learn a function—like predicting the price of a house based on its size. One input → one output.

But in science (like physics or climate modeling), we often care about something more complex: what happens to an entire shape, signal, or function when it goes through a system. For example:

Given the temperature across the earth today (a function), predict the temperature tomorrow (another function).

Given how a material is stretched, predict how it bends or cracks.

This is where operator learning comes in.

An operator is like a machine that takes in a whole function and gives you another function. So:

Instead of input: a number → output: a number

It's input: a function → output: a function

Operator learning means using a neural network to learn a machine (the operator) from examples, so you can use it to make predictions in the future.


--- 

## Sections
### 1. **Theoretical Contributions**  
- **Operator Approximation**: Prove universal approximation theorems for neural networks mapping between Sobolev spaces \( H^s(D) \to H^t(D') \).  
- **Error Bounds**: Establish scaling laws for network depth/width and their impact on generalization in Sobolev norms.  

### 2. **Numerical Experiments**  
- **Burgers Equation**: Learn the operator mapping initial conditions to PDE solutions.  
- **Width/Depth Scaling**: Validate theoretical depth-width-error tradeoffs.  


---

##  Setup  
### Dependencies  
- **LaTeX**: Compile theoretical proofs and final report (packages: `amsmath`, `amsthm`, `amssymb`).  
- **Python**: For numerical experiments (PyTorch, NumPy, SciPy, FEniCS).  


---

## For Readers  
- **Theorists**: Focus on `theory/` for functional analysis proofs and NTK-RKHS connections.  
- **Practitioners**: Use `numerics/` to reproduce experiments or adapt code for PDE learning tasks.  
- **Educators**: The LaTeX report (`report/main.tex`) provides a self-contained tutorial on Sobolev-space operator learning. 
