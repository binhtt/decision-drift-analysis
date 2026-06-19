======================================================================
SCALABILITY EVALUATION
======================================================================
N=     1,000  Drift=       632 Runtime=0.0003s
N=    10,000  Drift=     6,194 Runtime=0.0027s
N=   100,000  Drift=    62,758 Runtime=0.0269s
N=   500,000  Drift=   312,549 Runtime=0.1326s
N= 1,000,000  Drift=   624,663 Runtime=0.2616s


======================================================================
DRIFT CATEGORY ANALYSIS
======================================================================
v1→v2 249921 249921 0 0
v2→v3 625063 0 375698 249365
v3→v4 249598 124665 0 124933


SCALABILITY TABLE
   Requests   Drift   Runtime
0      1000     632  0.000261
1     10000    6194  0.002681
2    100000   62758  0.026876
3    500000  312549  0.132567
4   1000000  624663  0.261631


CATEGORY TABLE
  Transition   Drift  Expansion  Restriction  Divergence
0      v1→v2  249921     249921            0           0
1      v2→v3  625063          0       375698      249365
2      v3→v4  249598     124665            0      124933

## Runtime Scalability

![Runtime Scalability](runtime_scalability.png)

## Drift Category Analysis

![Drift Categories](drift_growth.png)

Saved Files:
runtime_scalability.png
drift_growth.png
scalability_results.csv
category_results.csv
