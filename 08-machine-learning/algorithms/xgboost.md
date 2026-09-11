# XGBoost

![ML animation](../../assets/08-machine-learning.svg)

## What it solves
XGBoost is useful when the goal is to **regularized gradient-boosted trees with efficient training**.

## Mental model
Start with a tiny dataset you can draw or calculate by hand. The algorithm repeatedly applies a simple rule to the representation until it produces a prediction or structure.

## Formal view

**Core formulation:** `objective = loss + regularization`

**Training objective / evaluation idea:** `task metric + objective`

## Step-by-step

1. Define the input matrix/features and target when applicable.
2. Establish a trivial baseline.
3. Apply the algorithm's core operation.
4. Measure the result on data that was not used to fit the parameters.
5. Inspect failures and assumptions.

## From-scratch requirement

Implement the smallest educational version before using a library. The implementation should expose the important state (weights, centroids, splits, support vectors, iterations, etc.) and include tests for a hand-worked example.

## Production implementation

Use a maintained library when reliability, performance and edge-case coverage matter. Keep preprocessing and model fitting inside a reproducible pipeline.

## Hyperparameters to understand

Do not tune by superstition. For every hyperparameter, document: what it controls, the direction of its effect, plausible range, interaction with other settings, and validation evidence.

## Strengths

- Clear mathematical or algorithmic interpretation.
- Useful baseline or strong model depending on the data regime.
- Can expose meaningful failure modes.

## Weaknesses / failure cases

- Wrong assumptions about data geometry or noise.
- Sensitivity to scale, imbalance, outliers or hyperparameters where applicable.
- Validation leakage can make any model appear stronger than it is.

## Experiment template

**Question:** What are we trying to learn?

**Baseline:** What happens with the simplest reasonable approach?

**Change:** Exactly one major change at a time.

**Metric:** Why does this metric match the decision?

**Result:** Record the value plus dataset/split/configuration.

**Error analysis:** Which examples fail and why?

**Conclusion:** What evidence supports or rejects the hypothesis?

## Interview questions

1. Explain the algorithm without equations.
2. Derive or motivate its objective.
3. What assumptions matter?
4. How does it behave with noise, scale, imbalance and high dimensions?
5. How would you debug a suspiciously high validation score?
6. When would you choose another algorithm?

## Mastery checklist

- [ ] Intuition
- [ ] Formal objective
- [ ] From-scratch implementation
- [ ] Library implementation
- [ ] Visualization
- [ ] Hyperparameter experiment
- [ ] Failure analysis
- [ ] Interview explanation
