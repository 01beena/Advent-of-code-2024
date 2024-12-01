# Historian Hysteria: Advent of Code 2024 Solution

## 🎄 Overview

This repository contains the Python solution to **Day 1: Historian Hysteria** from Advent of Code 2024. The problem involves processing two lists of numbers to calculate:

1. The **total distance** between corresponding elements after sorting both lists.
2. The **similarity score**, which is determined by matching elements between the lists and summing weighted counts.

The problem demonstrates key concepts in data manipulation, sorting, and frequency analysis in Python.

---

## 🚀 Features

- **Efficient Sorting and Pairing**: Calculates the total distance between sorted elements of two lists.
- **Frequency-Based Analysis**: Determines similarity score using a dictionary for frequency counting.
- **Robust Input Handling**: Reads input from a file and processes it into two lists.
- **Error Handling**: Handles missing or malformed input gracefully.

---

## 🛠️ Setup and Usage

### Prerequisites

- Python 3.8 or higher
- A text editor or IDE for running the Python script

### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/historian-hysteria.git
   cd historian-hysteria
   ```

2. **Prepare the Input File**:
   - Create a file named `input.txt` in the repository root.
   - Add the puzzle input in the following format:
     ```
     <number_from_left_list> <number_from_right_list>
     ...
     ```
     Example:
     ```
     3 4
     4 3
     2 5
     1 3
     3 9
     3 3
     ```

3. **Run the Script**:
   ```bash
   python main.py
   ```

4. **Output**:
   The script will output:
   - **Total Distance (Part 1)**
   - **Similarity Score (Part 2)**

---

## 📂 File Structure

```
historian-hysteria/
│
├── main.py          # Python script containing the solution
├── input.txt        # Input file (you need to create this file)
└── README.md        # This readme file
```

---

## 🔍 Example Output

For the input:
```
3 4
4 3
2 5
1 3
3 9
3 3
```

The script outputs:
```
Total Distance (Part 1): 11
Similarity Score (Part 2): 31

## 🧩 How It Works

### Part 1: Total Distance
1. Sort both lists.
2. Pair elements at corresponding indices from each list.
3. Calculate the absolute difference for each pair and sum these differences.

### Part 2: Similarity Score
1. Count the occurrences of each number in the right list.
2. Multiply each number in the left list by its frequency in the right list.
3. Sum these weighted values for the final score.


## 🌟 Contribution

1. Fork the repository.
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🎉 Acknowledgments

Thanks to the Advent of Code team for creating these fun and challenging puzzles!
