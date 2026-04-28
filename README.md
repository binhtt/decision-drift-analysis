# Decision Drift Analysis in Access Control Policy Evolution

This repository contains the **experimental artifact** for the paper:

> *Analyzing Authorization Decision Drift in Access Control Policy Evolution*

---

## Overview

This project implements a framework for analyzing **decision drift** between versions of access control policies.

Decision drift captures **semantic changes in authorization outcomes** across policy versions, going beyond syntactic differences.

The framework supports:

- Cross-version policy evaluation  
- Drift detection over a request set  
- Classification of drift into:
  - **Expansion** (more permissive changes)  
  - **Restriction** (more restrictive changes)  
  - **Divergence** (non-monotonic semantic changes)  

---

## Experimental Setup

The approach is evaluated across three representative policy domains:

- **RBAC** (Role-Based Access Control)  
- **ABAC** (Attribute-Based Access Control)  
- **Healthcare policy scenario**  

For each domain:

- Multiple policy versions are defined  
- A finite request set \( R' \) is generated  
- Decision drift is computed between consecutive policy versions  

---

## Request Sets

- **RBAC and ABAC**: 32 requests  
  (constructed via full combinatorial enumeration of attributes)

- **Healthcare**: 9 requests  
  (domain-specific scenarios focusing on role and emergency conditions)

This design reflects the difference between:

- **Systematic evaluation** (RBAC/ABAC)  
- **Scenario-driven evaluation** (Healthcare)

---

## Requirements

- Python 3.8+  
- Open Policy Agent (OPA)  

---

## Run the Experiment

```bash
python main.py
## Sample Results

- A full example of the experimental output is available at:
[View sample output](./Results/sample_output.txt)

## Output Description

For each policy transition, the framework reports:

- Total number of requests
- Number of drift cases
- Drift rate
- Number of:
     + Expansion cases
     + Restriction cases
     + Divergence cases

## Artifact Structure 
├── src/
│   ├── evaluator.py
│   ├── drift.py
│   ├── generator.py
│   └── policies.py
├── Results/
│   └── sample_output.txt
├── main.py
└── README.md
## Notes
The artifact focuses on semantic behavior comparison, not syntactic policy differences.
Drift results depend on the coverage of the request set R'.
Policy evaluation is assumed to be deterministic.

## License

This project is licensed under the MIT License.
