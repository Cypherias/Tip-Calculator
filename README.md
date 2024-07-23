# 💰 Tip Calculator 

## 📝 Description
This Python program helps you calculate how much each person should pay for a bill, including a tip. You enter the total bill amount, the percentage of tip you want to give, and how many people are splitting the bill. It then computes the total bill with tip, divides it by the number of people, and shows how much each person needs to pay. The program guides you through each step and ensures all inputs are correct. It's handy for quickly figuring out shared expenses at restaurants or events.

## 🖥️ Language Used
- **Python**

## 🎬 Program Demo:

<p align="center">
 Run the program: <br/>
<img src="https://i.imgur.com/S9nJWRF.jpg" height="80%" width="80%" alt="Demo of Tip Calculator by HakubaCode"/>
</p>

<p align="center">
 Input the required fields: <br/>
<img src="https://i.imgur.com/xNJwb18.jpg" height="80%" width="80%" alt="Demo of Tip Calculator by HakubaCode"/>
<img src="https://i.imgur.com/xrT29ck.jpg" height="80%" width="80%" alt="Demo of Tip Calculator by HakubaCode"/>
</p>

<p align="center">
 Final Output:
</p>
<p align="center">
 <img src="https://i.imgur.com/XIevxhI.jpg" height="80%" width="80%" alt="Demo of Tip Calculator by HakubaCode"/>
</p>

## 🌟 Key Features

1. **Input Validation**: The program ensures that the user enters the correct type of data, improving reliability and user experience.
2. **Loops and Error Handling**: Uses loops to keep asking for input until it's valid, making the program more robust and user-friendly.
3. **Basic Arithmetic Operations**: Performs calculations for the total bill, tip amount, and how to split the bill among multiple people.

## 🏗️ Code Structure

The program is structured into three main functions:

### 🔢 `get_float_input(prompt)`
- Continuously asks the user for a number until they provide a valid positive number.
- Uses a `while True` loop for repeated attempts.
- Implements try-except blocks to handle invalid inputs gracefully.

### 🔢 `get_int_input(prompt)`
- Similar to `get_float_input`, but specifically for whole numbers (integers).
- Ensures the input is a positive integer.

### 🧮 `tip_calculator()`
This is the main function that orchestrates the entire process:
1. Displays a welcome message.
2. Collects user inputs:
   - Total bill amount
   - Tip percentage
   - Number of people splitting the bill
3. Performs calculations:
   - Converts tip percentage to decimal
   - Calculates total tip amount
   - Computes total bill including tip
   - Determines amount per person
4. Presents the results in a user-friendly format

## 🔑 Key Programming Concepts

1. **Input Validation**: Always check if user inputs are correct and handle errors gracefully.
2. **Loops for Repeated Actions**: Utilize loops to keep trying until correct input is received.
3. **Error Handling**: Employ try-except blocks to manage errors without crashing the program.
4. **Basic Arithmetic**: Implement fundamental math operations for necessary calculations.
5. **User-Friendly Output**: Display results in an easy-to-understand manner.

This Tip Calculator demonstrates practical application of these programming concepts, creating a useful tool for everyday scenarios while showcasing important coding principles.
