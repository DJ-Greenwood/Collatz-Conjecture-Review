# Proving the Collatz Conjecture: A Deterministic Approach

This repository contains the research paper on the Proving the Collatz Conjecture: A Deterministic
Approach.

## Introduction

This paper presents a deterministic proof structure for the Collatz conjecture,
demonstrating that every positive integer eventually reaches the cycle {16, 8, 4,
2, 1}. By replacing probabilistic arguments with deterministic transition rules, set
partitioning, modular constraints, and an inductive descent process, we establish
the inevitability of convergence. The Collatz function is analyzed through parti-
tioning numbers into even and odd cases, allowing for a structured deterministic
reduction. Key lemmas and well-ordering arguments are employed to eliminate non-
termination and non-trivial cycles. An inductive proof confirms that all positive
integers ultimately reduce to the cycle {16, 8, 4, 2, 1}, thus proving the conjecture.

The conjecture is that no matter what value of n, the sequence will always reach 1.

## Contents

- `Collatz_Conjecture_Proposed_Proof.pdf`: The main research paper.
- `Paper/Collatz_Conjecture_Proposed_Proof.pdf`: This file also contains the latex files to make the pdf. 
- `data/`: Directory containing data used in the research.
- `python/`: Directory containing scripts used for analysis.

## Usage

To view the paper, open `Collatz_Conjecture_Proposed_Proof.pdf`. For data and scripts, navigate to their respective directories.

## Authors

- Denzil James Greenwood

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International license.