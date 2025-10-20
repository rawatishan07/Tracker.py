# 🍏 Daily Calorie Tracker CLI (Tracker.py)

**Mini Project Assignment: Daily Calorie Tracker CLI**

| Detail | Value |
| :--- | :--- |
| **Author** | Ishan Rawat |
| **Date** | 5th October 2025 |
| **Project Name** | Caloric |

***

## 1. 🎯 Project Goal

This project provides a **simple, lightweight Command-Line Interface (CLI)** application for tracking daily caloric intake. The primary goal is to offer a quick, digital method for manually logging meals and calculating key health metrics without the overhead of complex applications.

### Key Objectives:
1.  **Efficiency:** Allow rapid data entry for meal and calorie data.
2.  **Monitoring:** Calculate the **Total** and **Average** daily calorie intake.
3.  **Alerting:** Provide an immediate warning if the average caloric intake exceeds a predefined safe limit (`Average_Safe_Calories`).

***

## 2. 📊 Data Understanding (Inputs and Structure)

The tool operates on direct user input to generate its report.

| Data Point | Type | Description |
| :--- | :--- | :--- |
| **Meal Name** | `String` | The name of the food/meal (e.g., "Lunch Salad"). |
| **Calories Intake** | `Float` | The caloric value of the meal. |
| **Number of Meals (x)** | `Integer` | The initial count of meals to be logged. |

**Output Data:** The final report displays the total caloric sum, the average calories per meal, and a formatted breakdown table.

***

## 3. ⚙️ Data Preparation (Input Processing)

Data preparation focuses on collecting and organizing the user inputs for calculation:

1.  **Collection:** The program iteratively prompts the user for the name and calorie count for the specified number of meals.
2.  **Storage:** Meal names and calorie values are temporarily stored in two synchronized Python lists (`Meals` and `Calories`).
3.  **Data Typing:** Input values are immediately cast using `int()` and `float()` to ensure they are ready for mathematical operations.

***

## 4. 🧠 Modeling (The Core Logic)

The "modeling" phase is based on standard arithmetic calculations and a simple rule-based comparison.

| Metric | Calculation |
| :--- | :--- |
| **Total Calories (A)** | Sum of all elements in the `Calories` list (`sum(Calories)`). |
| **Average Calories** | Total Calories divided by the number of meals (`A / x`). |

**Rule-Based Alert Model:**
* **Threshold:** `Average_Safe_Calories` (Set to **600** in the current implementation).
* **Logic:** If the calculated `Average` is greater than the threshold, a "Warning!!" is displayed.

***

## 5. ✅ Evaluation (Verification)

Evaluation is performed by the user reviewing the generated report for accuracy:

* The program prints a detailed, **formatted table** (`Meal Breakdown`) to the console, allowing the user to visually verify that all inputs were correctly captured.
* The final output of the **Total Calories** and **Average Calories** acts as the summary metric, which the user can check against their dietary goals.

***
<H1>Sample</H1>
<img width="462" height="447" alt="Capture" src="https://github.com/user-attachments/assets/a3945abd-7696-4558-98c4-2bfd73b81c9c" />

## 6. 🚀 Deployment (How to Run)

This CLI is ready for immediate use and requires a standard Python environment.

### Prerequisites
* Python 3.x installed on your system.

### Installation & Execution

1.  **Clone the repository or download the script:**
    ```bash
    git clone [https://github.com/rawatishan07/Tracker.py](https://github.com/rawatishan07/Tracker.py)
    cd Tracker.py 
    ```
2.  **Run the script:**
    ```bash
    python Tracker.py
    ```
3.  **Follow Prompts:** The application will guide you through entering the number of meals and then the name and calorie count for each one.
