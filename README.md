# Reversible Turing Machine

This tool is a Standard Turing Machine to Reversible Turing Machine converter, programmed in Python 3. 

## Functionality
- **Input:** You provide an input and the transitions for your standard one-tape Turing Machine.
- **Conversion:** The code converts this into a reversible three-tape machine.
- **Output:** After processing the input, you will receive:
  - One tape with the initial input.
  - One empty tape (used for memory).
  - One tape with the result of the computation.

This is all based on the original reversible Turing machine paper: [Bennett, 1973](https://doi.org/10.1137/0403020).

## How to Run
To run the converter, use the following command:
```bash
python3 tm_test0.py
