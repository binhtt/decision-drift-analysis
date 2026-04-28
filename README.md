# Decision Drift Analysis in Access Control Policy Evolution

This repository contains the **experimental artifact** for the paper:

> *Analyzing Authorization Decision Drift in Access Control Policy Evolution*

---

##  Overview

This project implements a framework for analyzing **decision drift** between versions of access control policies.

Decision drift captures **semantic changes in authorization outcomes** across policy versions, beyond syntactic differences.

The framework supports:
- Cross-version policy evaluation
- Drift detection over a request set
- Classification of drift into:
  - **Expansion** (more permissive)
  - **Restriction** (more restrictive)
  - **Divergence** (non-monotonic change)

---

##  Experimental Setup

We evaluate the approach across three representative domains:

- **RBAC** (Role-Based Access Control)
- **ABAC** (Attribute-Based Access Control)
- **Healthcare policy scenario**

For each domain:
- Multiple policy versions are defined
- A finite request set is generated
- Decision drift is computed between consecutive versions

---

## 📂 Repository Structure
