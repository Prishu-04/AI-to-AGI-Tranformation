# AIML Big Picture and Python or Tool Setup
## 1. Why Day1 Matters 
Before understanding AI/ML, you need *Python Control*.
AI/ML engineers use Python to:
* Clean data
* build models
* train neural networks
* call APIs
* automate workflows
* build AI products
* deploy ML systems

```
Think logically -> write clean code -> debug errors -> build mini projects -> push to GitHub
```
In AI/ML, Python helps you use libraries like:
![[Pasted image 20260528095405.png]]

---
# 2. AI/ML Big Picture
### Artificial Intelligence (AI)
Artificial Intelligence means building systems that can performs tasks that normally require human intelligence.
Examples:
* Chatbot
* face recognition
* self-driving car
* recommendation system
* fraud detection system
---
### Machine Learning
*Machine Learning* is part of AI where machines learn patterns from data.
Example:
``` 
Past student marks + study hours → Model learns pattern → Predict future marks
```
---
### Deep Learning
*Deep Learning* uses neural networks with many layers
Used in:
* ChatGPT-like systems
* image recognition
* voice assistants
* medical image diagnosis
* autonomous driving
---
### Generative AI
*Generative AI* creates new content.
Examples:
* text generation
* image generation
* code generation
* music generation
* video generation
---
### Understanding the AI/ML Map
Think of AI lioke this:
```
AI = Big field of making machines intelligent
ML = Machines learning patterns from data
Deep Learning = ML using neural networks
Generative AI = AI that creates text, images, code, audio, etc.
```
### Simple Example
Suppose you want to predict student marks:
##### Traditional programming:
```
You manually write rules:
if study_hours > 5:
    marks = high
else:
    marks = low
```
##### Machine learning:
```
You give past data:
study hours, attendance, previous marks

Model learns pattern automatically.
```
so ML is useful when rules are too complex to manually write.

---
### AI/ML Pipeline
```
Problem → Data Collection → Data Cleaning → Feature Engineering → Model Training → Model Evaluation → Deployment → Monitoring
```
Example;
```
Problem: Predict if a student will pass or fail.

Data:
- study hours
- attendance
- previous marks
- assignment score

Model:
- learns pattern

Output:
- Pass / Fail prediction
```
In AI/ML, the pipeline will slowly become:
```
Python → NumPy → Pandas → ML → Deep Learning → GenAI → Deployment → MLOps
```
---
# 3. Setup Checklist
Install:

| Tools                        | Why you need it                |
| ---------------------------- | ------------------------------ |
| Python                       | Main AIML programming language |
| VS code                      | Coding editor                  |
| JupyterLab/ Jupyter Notebook | Notebook-based experimentation |
| Git                          | Version Control                |
| Github                       | Portfolio and Project hosting  |
Install command:
```bash
pip install jupyterlab
```
Run JupyterLab:
```Bash
jupyter lab
```
---
# 4. Create Github Repo
Repository:
```
MachineLearning
```
Folder Structure:
```
MachineLearning/
│
├── README.md
├── Day_01_Python_Setup/
│   ├── notes.md
|   ├── venv
│   ├── student_marks_analyzer.py
│   └── errors_and_fixes.md
│
├── datasets/
├── projects/
└── resources/
```
---
# Debugging Lab
# Error 1: Python not recognized
Error:
```
'python' is not recognized as an internal or external command
```
Meaning:
```
Python is not installed properly or not added to PATH.
```
Fix:
```
Reinstall Python and tick "Add Python to PATH" during installation.
```
---
# Error 2: pip nor recognized
Error:
```
'pip' is not recognized as an internal or external command
```
Fix:
```Bash
python -m ensurepip --upgrade
```
then check:
```Bash
python -m pip --version
```
---
# Error 3: Jupyter command not found
Error:
```
'jupyter' is not recognized
```
Fix:
```bash
python -m pip install jupyterlab
python -m jupyter lab
```
---
# MINI TEST
1. What is the difference between AI and ML?
2. What is Deep Learning?
3. What is Generative AI?
4. Why do AI engineers use Python?
5. What are the 8 stages of an AI/ML pipeline?
6. What command checks Python version?
7. What command installs JupyterLab?
8. What command opens JupyterLab?
---
