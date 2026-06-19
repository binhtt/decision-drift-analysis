# Decision Drift Analysis in Access Control Policy Evolution

This repository contains the experimental artifact for the paper:

> *Analyzing Authorization Decision Drift in Access Control Policy Evolution*

---

## Overview

This project implements a framework for analyzing **authorization decision drift** across evolving access control policies.

The framework supports:

- Cross-version policy evaluation
- Decision drift detection
- Drift quantification
- Drift classification into:
  - **Expansion**
  - **Restriction**
  - **Divergence**

---

## Experimental Evaluation

The artifact includes experiments reported in the paper across:

- RBAC (Role-Based Access Control)
- ABAC (Attribute-Based Access Control)
- Healthcare access control scenarios

The evaluation consists of:

1. Domain-specific policy evolution case studies
2. Monte-Carlo scalability experiments (10³–10⁶ requests)
3. Large-scale drift-category analysis

---

## Requirements

- Python 3.8+
- Open Policy Agent (OPA)

---

## Running the Experiments

### Case Studies

```bash
python main.py
```

### Monte-Carlo Experiments

```bash
python src/Monte_Carlo.py
```

---

## Results

### Sample Output

- Domain-specific experiment results:

  ```
  Results/sample_output.txt
  ```

- Monte-Carlo scalability and drift-category analysis:

  ```
  Results/monte_carlo_results.txt
  ```

### Generated Figures

- Runtime scalability:

  ```
  Results/time.png
  ```

- Drift growth versus request-set size:

  ```
  Results/request.png
  ```

---

## Artifact Structure

```text
decision-drift-analysis
│
├── src
│   ├── Monte_Carlo.py
│   ├── drift.py
│   ├── evaluator.py
│   ├── generator.py
│   └── policies.py
│
├── Results
│   ├── sample_output.txt
│   ├── monte_carlo_results.txt
│   ├── time.png
│   └── request.png
│
├── main.py
├── README.md
└── LICENSE
```

---

## Notes

- The artifact focuses on semantic analysis of authorization behavior rather than syntactic policy differences.
- Drift measurements depend on the coverage of the evaluated request set.
- Monte-Carlo experiments are included to evaluate scalability under large request spaces.
- Policy evaluation is assumed to be deterministic.

---

## License

This project is licensed under the MIT License.
