<div align="center">

<a href="https://github.com/dhruviraval13110/python-for-ai-engineering">
  <img src="./assets/learning-loop.svg" alt="Animated AI Engineering Learning Loop" width="100%">
</a>

Python for AI Engineering

A structured AI/ML engineering curriculum — from Python fundamentals to machine learning, deep learning, GenAI, LLM systems, MLOps and research.

<p>
  <a href="https://github.com/dhruviraval13110/python-for-ai-engineering/actions/workflows/python-tests.yml"><img src="https://github.com/dhruviraval13110/python-for-ai-engineering/actions/workflows/python-tests.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/dhruviraval13110/python-for-ai-engineering/actions/workflows/quality.yml"><img src="https://github.com/dhruviraval13110/python-for-ai-engineering/actions/workflows/quality.yml/badge.svg" alt="Quality"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python 3.11+"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/dhruviraval13110/python-for-ai-engineering" alt="License"></a>
</p>

<p>
  <a href="#-curriculum">Curriculum</a> •
  <a href="#-learning-system">Learning System</a> •
  <a href="#-machine-learning-lab">ML Lab</a> •
  <a href="#-production-engineering">Production</a> •
  <a href="#-projects">Projects</a> •
  <a href="#-research">Research</a> •
  <a href="#-run-locally">Run Locally</a>
</p>

</div>

<div align="center">

Learn → derive → implement → visualize → test → experiment → debug → explain → document

</div>

🧭 What this repository is

This repository is designed as a textbook + laboratory + engineering portfolio.

It is not organized as a collection of disconnected tutorials. The curriculum is designed to build capability in layers:

Python
  ↓
Data Structures & Numerical Computing
  ↓
Mathematics + Statistics
  ↓
Data Analysis + SQL
  ↓
Classical Machine Learning
  ↓
Deep Learning
  ├── Computer Vision
  └── NLP
  ↓
Generative AI
  ↓
LLM Engineering
  ↓
MLOps + Deployment
  ↓
Research + Production Systems

The objective is simple:

Understand the mechanism, implement the idea, use the professional tool, test the behavior, investigate failure, and explain the result.

✨ Curriculum

#

Layer

Core coverage

01

Python Foundations

Syntax, data types, control flow, functions, collections, OOP, advanced Python, testing and tooling

02

Python for Data

NumPy, Pandas, vectorization, data cleaning, feature engineering and performance

03

Mathematics for ML

Linear algebra, calculus, probability and optimization

04

Statistics

Descriptive statistics, inference, distributions, experiments and uncertainty

05

Data Analysis

Problem framing, cleaning, EDA, feature engineering and decision-oriented analysis

06

Data Visualization

Analytical plots, ML diagnostics and communication

07

SQL

Queries, joins, CTEs, windows, schema design and query performance

08

Machine Learning

Regression, classification, clustering, dimensionality reduction and evaluation

09

Deep Learning

Neural networks, backpropagation, optimization, CNNs, sequences and attention

10

Computer Vision

Classification, transfer learning, detection, segmentation and OCR

11

NLP

Text processing, representations, embeddings, sequence models and transformers

12

Generative AI

LLM foundations, prompting, embeddings, RAG, evaluation and safety

13

LLM Engineering

Tools, agents, memory, structured outputs, reliability, latency and cost

14

MLOps

Reproducibility, experiment tracking, versioning, CI, monitoring and drift

15

Deployment

APIs, containers, CI/CD and production readiness

16

Research

Hypotheses, baselines, controlled experiments, ablations and error analysis

🧠 Learning System

Every major topic follows the same engineering-first learning contract:

flowchart LR
    A[Definition] --> B[Intuition]
    B --> C[Formal Model]
    C --> D[Worked Example]
    D --> E[Implementation]
    E --> F[Visualization]
    F --> G[Tests]
    G --> H[Experiment]
    H --> I[Failure Analysis]
    I --> J[Interview Explanation]
    J --> K[Mastery Check]
    K --> A

Each topic should answer

Layer

Question

Definition

What exactly is it?

Intuition

Why does it work?

Formalism

What are the equations, assumptions or rules?

Implementation

How do I build the smallest working version?

Professional tool

How is it implemented in real projects?

Visualization

Can I see what the system is doing?

Failure

When does it break?

Testing

How do I know it is correct?

Experiment

What changes when an assumption changes?

Communication

Can I explain it clearly in an interview or review?

🐍 Python Foundations

The foundation layer progresses from beginner syntax to engineering practices.

Core Python

Variables · Types · Operators · Conditions · Loops · Functions · Scope · Lists · Tuples · Sets · Dictionaries · Strings · Comprehensions

Engineering Python

Exceptions · Files · Modules · Packages · OOP · Decorators · Generators · Iterators · Context Managers · Type Hints · Dataclasses · Testing · Logging · APIs · Async Basics

Professional habits

readable names

small functions

explicit interfaces

useful docstrings

type hints where they improve clarity

deterministic tests

structured logging

configuration separated from secrets

reproducible environments

Start with the Python Foundations chapter and the existing examples.

📊 Data + Mathematical Foundations

AI engineering becomes much easier when the data and mathematics are understood rather than treated as black boxes.

Numerical computing

arrays and dimensions

indexing and slicing

broadcasting

vectorization

dtypes

aggregation

matrix operations

numerical stability

Data manipulation

DataFrames

filtering and sorting

missing values

duplicates

grouping and aggregation

joins and merges

reshaping

dates and strings

feature engineering

performance considerations

Mathematics

vectors and matrices

dot products

matrix multiplication

derivatives

gradients

probability

distributions

expectation and variance

optimization

Explore Python for Data and Mathematics for ML.

🗃️ SQL + Data Analysis

A strong ML engineer must understand the data before training the model.

The curriculum covers:

Business Question
      ↓
Data Model
      ↓
SQL Extraction
      ↓
Data Quality
      ↓
EDA
      ↓
Feature Engineering
      ↓
Statistical Reasoning
      ↓
Model / Decision

SQL topics include:

SELECT · WHERE · GROUP BY · HAVING · ORDER BY · JOIN · CASE · Subqueries · CTEs · Window Functions · Aggregations · Indexes · Normalization · Query Optimization

See SQL and Data Analysis.

🤖 Machine Learning Lab

The ML layer is organized around understanding + implementation + evaluation, not merely calling a library.

Algorithms

Family

Algorithms

Regression

Linear Regression

Classification

Logistic Regression, KNN, Naive Bayes, Decision Trees

Ensembles

Random Forest, Gradient Boosting, XGBoost

Margin-based

SVM

Clustering

K-Means, DBSCAN

Dimensionality Reduction

PCA

From-scratch implementations

The repository includes educational implementations for selected algorithms, including:

Linear Regression

Logistic Regression

K-Means

The purpose of from-scratch work is to expose the mechanism before abstraction.



Evaluation is part of the model

Every ML experiment should make explicit:

Dataset
  ↓
Train / Validation / Test Strategy
  ↓
Baseline
  ↓
Preprocessing
  ↓
Model
  ↓
Metric Selection
  ↓
Error Analysis
  ↓
Conclusion

Covered evaluation concepts include:

train/validation/test splits

cross-validation

overfitting

underfitting

bias/variance

data leakage

class imbalance

accuracy

precision

recall

F1

ROC-AUC

PR-AUC

MAE

MSE

RMSE

R²

Go to Machine Learning.

🧠 Deep Learning

The deep-learning path moves from the smallest neural network to modern architectures.

Perceptron
   ↓
Dense Neural Network
   ↓
Forward Pass
   ↓
Loss
   ↓
Backpropagation
   ↓
Gradient Descent
   ↓
Optimization
   ↓
CNN / Sequence Models
   ↓
Attention
   ↓
Transformers

Topics include:

neurons and layers

activation functions

forward propagation

loss functions

gradients

backpropagation

optimizers

learning rate

batch size

epochs

regularization

CNNs

RNNs

LSTMs / GRUs

attention

transformers

See Deep Learning.

👁️ Computer Vision + 📝 NLP

Computer Vision

Image Classification · CNNs · Preprocessing · Augmentation · Transfer Learning · Object Detection · Segmentation · OCR · Similarity

→ Computer Vision

NLP

Tokenization · Text Cleaning · Bag of Words · TF-IDF · Embeddings · Word2Vec Intuition · Sequence Models · Attention · Transformers

→ NLP

✨ Generative AI

Modern AI systems require more than knowing how to call an LLM.

The curriculum covers:

Tokens
  ↓
Embeddings
  ↓
Context
  ↓
Prompting
  ↓
Retrieval
  ↓
Generation
  ↓
Evaluation
  ↓
Guardrails

Core topics:

LLM fundamentals

tokenization

embeddings

context windows

temperature

top-k / top-p

inference

prompting

structured output

RAG

chunking

retrieval

reranking

vector databases

hallucination analysis

evaluation

safety

→ Generative AI

🛠️ LLM Engineering

LLM applications become engineering systems when they include reliability, observability and controlled interfaces.

flowchart LR
U[User] --> API[Application]
API --> P[Prompt / Policy]
P --> R[Retriever]
R --> M[Model]
M --> T[Tools]
T --> V[Validation]
V --> E[Evaluation]
E --> O[Observability]
O --> U

Topics:

prompt templates

tool calling

function interfaces

agents

memory

RAG pipelines

structured outputs

evaluation

guardrails

latency

cost

caching

observability

→ LLM Engineering

⚙️ Production Engineering



A production ML system connects:

data → validation → features → model → evaluation → artifact → API → container → monitoring → feedback

MLOps

Git workflows

reproducibility

data/model versioning

experiment tracking

model registries

testing

CI/CD

monitoring

drift

rollback thinking

Deployment

API design

model serving

Docker

configuration

environment variables

CI/CD

production readiness

See MLOps and Deployment.

🧪 Research

Research is treated as a repeatable engineering process:

Question
  ↓
Hypothesis
  ↓
Baseline
  ↓
Controlled Change
  ↓
Measurement
  ↓
Error Analysis
  ↓
Conclusion
  ↓
Next Experiment

Each experiment should document:

hypothesis

dataset

baseline

method

controlled variable

result

interpretation

limitations

next experiment

→ Research

💼 Projects

The portfolio system is designed around evidence rather than project-count inflation.

Beginner

Build fundamentals through small, complete systems.

Intermediate

Combine data, models, APIs and evaluation.

Advanced

Build systems with:

Frontend
   ↕
Backend API
   ↕
ML / AI Service
   ↕
Database / Vector Store
   ↕
Evaluation + Monitoring

Every serious project should document:

problem

users / decision context

data source

data dictionary

baseline

architecture

methodology

metrics

error analysis

limitations

reproduction

tests

future work

→ Projects

🎓 Interview Preparation

The interview layer is organized around four dimensions:

Dimension

Practice

Fundamentals

concepts, definitions, intuition

Coding

Python, SQL, data structures and implementation

ML reasoning

metrics, leakage, model selection, debugging

System design

data pipelines, model serving, RAG and MLOps

Questions should be answered with why, not only what.

→ Interview Preparation

🧩 Engineering Quality

The repository favors boring, reliable engineering over visual decoration that hides weak fundamentals.

Python 3.11+

Ruff

Black

pytest

mypy where useful

CI checks

deterministic examples

explicit dependencies

environment isolation

no secrets committed to source

no fabricated metrics

no fabricated employment or certifications

no fabricated datasets or deployment claims

📁 Repository Architecture

python-for-ai-engineering/
│
├── 01-python-foundations/
├── 02-python-for-data/
├── 03-mathematics-for-ml/
├── 04-statistics/
├── 05-data-analysis/
├── 06-data-visualization/
├── 07-sql/
├── 08-machine-learning/
├── 09-deep-learning/
├── 10-computer-vision/
├── 11-nlp/
├── 12-generative-ai/
├── 13-llm-engineering/
├── 14-mlops/
├── 15-deployment/
├── 16-research/
│
├── projects/
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
│
├── experiments/
├── notebooks/
├── examples/
├── interview-preparation/
├── resources/
│
├── src/
├── tests/
├── assets/
├── docs/
│
├── pyproject.toml
├── requirements.txt
├── Makefile
├── CONTRIBUTING.md
├── LICENSE
└── README.md

🚀 Run Locally

Windows PowerShell

py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pytest -q
ruff check .

Run an example

python examples/01_variables/variables.py

Run an ML from-scratch implementation

python 08-machine-learning/from_scratch/linear_regression.py

🔍 Reviewer Quick Path

If you are reviewing this repository for technical depth:

README
  ↓
Python Foundations
  ↓
Math + Statistics
  ↓
Data + SQL
  ↓
Machine Learning
  ↓
Deep Learning
  ↓
GenAI / LLM Engineering
  ↓
MLOps / Deployment
  ↓
Projects
  ↓
Research

The goal is for every layer to provide evidence of understanding, not simply a list of technologies.

📈 Progress Philosophy

This repository intentionally avoids fake progress percentages and artificial achievement counters.

A topic is stronger when it has:

Understanding
+ Implementation
+ Tests
+ Experiment
+ Failure Analysis
+ Explanation
+ Documentation

That is the standard.

🛡️ Responsible AI Engineering

AI systems are probabilistic and can fail.

High-impact applications require appropriate:

human oversight

privacy controls

security controls

domain review

evaluation

uncertainty awareness

escalation paths

Technical capability includes knowing when a model should not be trusted.

📚 Documentation

Architecture

Coding Guidelines

Roadmap

Contributing

License

⭐ The Standard

Don't optimize this repository to look like an AI engineer. Build it so the evidence makes that conclusion obvious.

<div align="center">

Learn deeply. Build reproducibly. Measure honestly. Explain clearly.

<img src="./assets/learning-loop.svg" alt="Animated engineering loop" width="90%">

</div>
