
**Functional Analysis of Neural Tangent Kernels in Sobolev Networks for Operator Learning**  
Operator Learning in Sobolev Spaces via Neural Tangent Kernels (NTKs)
---

## Overview  
This project bridges **functional analysis**, **neural tangent kernel (NTK) theory**, and **operator learning** to (more rigorously) analyze how deep neural networks approximate nonlinear operators between Sobolev spaces. 

The goal of this project is to characterize/study the interplay between neural network architecture, optimization dynamics, and approximation error in high-dimensional function spaces, with applications to learning solution operators of partial differential equations (PDEs).  

The final report includes the following sections
- **Mathematical Framework**: Sobolev spaces, neural tangent kernels, and operator-valued RKHS.
- **Literature Review**: Existing literature on relevant topics.
- **Theoretical Foundations**: Proving and approximating error bounds, spectral bias, and optimization guarantees.  
- **Numerical Validation**: PDE case studies (e.g., Burgers’ equation) with error analysis.  

---

## Sections
### 1. **Theoretical Contributions**  
- **Operator Approximation**: Prove universal approximation theorems for neural networks mapping between Sobolev spaces \( H^s(D) \to H^t(D') \).  
- **NTK Analysis**: Derive spectral properties of the neural tangent kernel for operator learning and link its eigendecomposition to Sobolev-space error rates.  
- **Error Bounds**: Establish scaling laws for network depth/width and their impact on generalization in Sobolev norms.  

### 2. **Numerical Experiments**  
- **Burgers Equation**: Learn the operator mapping initial conditions to PDE solutions.  
- **NTK Eigenanalysis**: Quantify spectral decay of the NTK and its correlation with Sobolev errors.  
- **Width/Depth Scaling**: Validate theoretical depth-width-error tradeoffs.  

### 3. **Applications**  
- Scientific machine learning (SciML) tasks like PDE surrogate modeling.  
- Cross-domain transfer learning for function-to-function regression.  

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
