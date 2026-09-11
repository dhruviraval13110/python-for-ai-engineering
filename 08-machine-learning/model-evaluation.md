# Model Evaluation — the evidence layer

![evaluation](../assets/model-evaluation.svg)

## Why evaluation is difficult

A model score is meaningful only relative to a dataset, split, metric definition, baseline and decision context. The evaluation protocol is part of the model.

## Splits

- **Training:** fit learned parameters.
- **Validation:** choose models/hyperparameters.
- **Test:** estimate final generalization after decisions are frozen.
- **Cross-validation:** repeatedly train/validate across folds when a single split is unstable or data is limited.

For time-dependent problems, use time-aware splits. For grouped entities, keep the same entity out of both train and validation/test when leakage is possible.

## Classification metrics

| Metric | Formula / idea | Use when | Watch out for |
|---|---|---|---|
| Accuracy | correct / total | balanced classes, equal error costs | hides imbalance |
| Precision | TP / (TP+FP) | false positives are costly | ignores false negatives |
| Recall | TP / (TP+FN) | false negatives are costly | can create many false positives |
| F1 | harmonic mean of precision/recall | balance those two | hides threshold/cost details |
| ROC-AUC | ranking quality over thresholds | broad ranking assessment | can look strong on rare positives |
| PR-AUC | precision-recall ranking | rare positive class | interpretation depends on prevalence |

## Regression metrics

- **MAE:** average absolute error; easy to interpret and less sensitive to extreme errors than squared loss.
- **MSE:** squares errors; strongly penalizes large mistakes.
- **RMSE:** square root of MSE, returning to target units.
- **R²:** relative explained variance compared with a baseline; not a direct error magnitude.

## Error analysis

Slice errors by meaningful groups: time period, geography, class, input quality, prediction confidence, customer segment or other domain dimensions. Look for systematic failures, not just the worst individual examples.

## Leakage audit

Ask: could this feature have been known at prediction time? Did preprocessing see the test set? Did duplicate entities cross splits? Did we tune on the test set? A suspiciously excellent score is a debugging signal, not a victory.

## Evaluation record

Every experiment should record:

```text
dataset + version
split strategy
preprocessing
baseline
model + hyperparameters
metric definitions
results
error slices
limitations
```
