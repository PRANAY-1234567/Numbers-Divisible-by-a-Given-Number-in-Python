# 🔢 Numbers Divisible by a Given Number in Python

A simple Python program that prints all numbers divisible by a given number **x** within a specified range (`x` to `y`) and displays the total count of divisible numbers.

This project is ideal for beginners learning **loops**, **conditional statements**, and **modulus operations** in Python.

---

# 📌 Overview

The program accepts two integers from the user:

* **x** – the divisor and starting value of the range.
* **y** – the ending value of the range.

It then iterates through the range from **x** to **y**, prints every number divisible by **x**, and counts the total number of divisible values.

---

# 🚀 Features

* Accepts user input for range limits
* Finds all numbers divisible by the given divisor
* Displays the divisible numbers
* Counts and prints the total number of divisible values
* Beginner-friendly implementation

---

# 🛠️ Technologies Used

* Python 3

---

# 📂 Project Structure

```text
Numbers-Divisible-By-X/
│
├── divisible_numbers.py
└── README.md
```

---

# 💻 Source Code

```python
x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))

count = 0

for i in range(x, y + 1):
    if i % x == 0:
        print(i, end=" ")
        count += 1

print("\nTotal numbers divisible by x:", count)
```

---

# ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-divisible-numbers.git

cd python-divisible-numbers
```

### Run the Program

```bash
python divisible_numbers.py
```

---

# 📋 Sample Output

### Example

```text
Enter the value of x : 5
Enter the value of y : 30

5 10 15 20 25 30

Total numbers divisible by x: 6
```

---

# 🧠 Concepts Covered

* User Input
* `for` Loop
* `range()` Function
* `if` Statement
* Modulus (`%`) Operator
* Counter Variable

---

# 🔍 How It Works

1. Read the values of **x** and **y** from the user.
2. Initialize a counter variable to **0**.
3. Iterate through every number from **x** to **y**.
4. Check whether the current number is divisible by **x** using the modulus operator.
5. If divisible:

   * Print the number.
   * Increment the counter.
6. After the loop completes, display the total count of divisible numbers.

---

# 📖 Algorithm

1. Start the program.
2. Input values of **x** and **y**.
3. Set `count = 0`.
4. Loop from `x` to `y`.
5. Check `i % x == 0`.
6. If true:

   * Print the number.
   * Increase `count`.
7. Display the total count.
8. End the program.

---

# ⏱️ Complexity Analysis

| Operation        | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(n)**   |
| Space Complexity | **O(1)**   |

Where **n = y - x + 1**, the number of integers checked in the range.

---

# 🔮 Future Improvements

* Accept multiple divisors
* Find numbers divisible by both `x` and another number
* Display the sum of divisible numbers
* Store results in a list
* Export results to a text or CSV file
* Validate user input

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

* How to iterate through a range of numbers
* Using the modulus operator for divisibility checks
* Counting matching values with a counter variable
* Writing clean and readable Python code
* Basic problem-solving using loops and conditions

---

# 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software Engineer | Python | Java | SQL | Data Analytics

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and contribute for educational and learning purposes.

---

⭐ If you found this project helpful, don't forget to **Star** the repository!
