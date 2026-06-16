# Why Linear Algebra Powers Machine Learning
## 1. Goal
```
- Explain why machine-learning data is represented using vectors and matrices.
- Distinguish between scalars, vectors, matrices and tensors.
- Represent one observation as a feature vector.
- Represent an entire dataset as a matrix.
- Understand dimensions, shapes, axes and feature space.
- Recognize where vectors and matrices appear inside ML models.
- Create and inspect mathematical objects using NumPy.
- Debug basic shape, indexing and datatype problems.
```
---
## 2. Why this topic matters
Machine learning is primarily about converting real-world information into numbers and performing mathematical operations on those numbers.
Consider a student-marks prediction system. A student may have:
- 6 study hours
- 85% attendance
- 72 previous marks
The model cannot directly understand concepts such as “attendance” or “study effort.” It receives a numerical representation:
![[Pasted image 20260616092431.png]]​​
This collection of features is a **vector**.
For 1,000 students, we arrange all the student vectors together:
![[Pasted image 20260616092457.png]]
This is a **matrix**.
The model’s parameters are also stored as a vector:
![[Pasted image 20260616092532.png]]
Training the model means finding good values for these parameters.
Therefore:
```
Real-world information        
↓
Numerical features        
↓
Vectors and matrices        
↓
Mathematical operations        
↓
Predictions
```
Without linear algebra, modern machine learning would not be computationally practical.

---
## 3. Industry application
### Recommendation systems
A user can be represented using a vector:
![[Pasted image 20260616092723.png|252]]
A movie can also be represented using a vector:
![[Pasted image 20260616092741.png|255]]
The system compares the vectors to determine whether the user may like the movie.
This idea appears in recommendation systems used by platforms such as Netflix, Spotify, Amazon and YouTube.
### Natural language processing
Words, sentences and documents are converted into embedding vectors.
For example:
```
"machine learning"        
↓
[0.12, -0.84, 0.37, 0.51, ..., 0.28]
```
Modern language models perform enormous numbers of matrix operations to transform these representations.
### Computer vision
An image is stored as a numerical array.
A grayscale image:
![[Pasted image 20260616093326.png|219]]
A colour image:
![[Pasted image 20260616093340.png|231]]
The three channels usually represent red, green and blue intensities.
### Financial systems
A financial model may represent a customer using:
![[Pasted image 20260616093549.png|313]]
Matrix operations allow thousands or millions of customers to be evaluated together.
### Robotics and autonomous systems
Vectors represent:
- Position
- Velocity
- Acceleration
- Sensor readings
- Movement direction
Matrices represent rotations, coordinate transformations and batches of sensor measurements.

---
## 4. Interview relevance
Linear algebra appears directly and indirectly in AI/ML interviews.
Common questions include:
```
- What is the difference between a vector and a matrix?
- What does the shape of a dataset represent?
- Why is vectorisation faster than Python loops?
- What does X∈Rn×dX \in \mathbb{R}^{n \times d}X∈Rn×d mean?
- How are images represented mathematically?
- What is the difference between a NumPy one-dimensional array and a column vector?
- Where do matrices appear in neural networks?
- Why must feature dimensions match model parameter dimensions?
```
Senior interviews may also ask about:
```
- Memory consumption of large matrices
- Sparse versus dense matrix storage
- Batch processing
- GPU tensor operations
- Numerical precision
- Distributed matrix computation
```
---
## 5. Startup relevance
Suppose you build an AI recruitment platform.
Each candidate could be represented as:
![[Pasted image 20260616093802.png|387]]
Each job could also have a requirement vector:
![[Pasted image 20260616093832.png|390]]
Your product could compare candidate vectors with job vectors to build a matching engine.
The mathematics is simple, but it can power a commercially useful product.
The startup lesson is:
> Find a real-world entity, decide its measurable characteristics, and represent those characteristics as a vector.

---
## 6. The four fundamental mathematical objects
### 6.1 Scalar
A scalar is one number.
Examples:
```
5,-3.3,0.0001
```
In ML, scalars may represent:
- Learning rate
- Loss value
- Bias
- Accuracy
- Temperature
- One feature value