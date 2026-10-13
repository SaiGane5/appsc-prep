# Central Tendencies: Mean, Median, Mode & Weighted Averages

**Topic ID:**  | **Subject:** General Mental and Psychological Abilities | **Paper:** Screening Paper-II (Section A)

**Syllabus Mapping:** Central Tendencies - mean, median, mode — including weighted mean - Arithmetic Mean, Weighted Mean, Median for Ungrouped and Grouped Data, Mode, Empirical Relationship Between Mean, Median and Mode, Measures of Dispersion (Range, Variance, Standard Deviation).

---


# Central Tendencies: Arithmetic Mean, Weighted Averages, Median, Mode, and Dispersion


Measures of central tendency summarize distributions of data into a single representative metric. Civil administrators regularly interpret statistical reports containing arithmetic means, weighted indices, and medians to evaluate income distribution, literacy, and demographic outcomes.


![Normal distribution curve showing standard deviation intervals](https://upload.wikimedia.org/wikipedia/commons/f/fb/Standard_deviation_graph.jpg)
*Caption: Normal distribution curve showing central tendency (mean, median, and mode coincide at the center) and dispersion parameters under empirical standard deviations.*


## 1. Mathematical Formulations of Central Tendencies


### Table: Formulas for Measures of Central Tendency

| Measure | Ungrouped Data Formula | Grouped Frequency Data Formula | Analytical Properties |
| --- | --- | --- | --- |
| Arithmetic Mean ($\bar{x}$) | $\bar{x} = \frac{\sum x_i}{N}$ | $\bar{x} = \frac{\sum f_i x_i}{\sum f_i}$ | Easily distorted by extreme outlier values; sum of deviations from mean is always 0. |
| Weighted Mean ($\bar{x}_w$) | $\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$ | N/A | Assigns relative importance weights (e.g., CPI inflation basket, academic GPAs). |
| Median ($M$) | Middle value when data is sorted in order. If $N$ is odd: $\frac{N+1}{2}$-th. If $N$ is even: avg of $\frac{N}{2}$ and $\frac{N}{2}+1$. | $M = L + \left(\frac{\frac{N}{2} - cf}{f}\right) \times h$ | Positional average resistant to extreme outliers; ideal for measuring skewed income/wealth distribution. |
| Mode ($Z$) | Most frequently occurring value in the dataset. | $Z = L + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h$ | Value with highest frequency; can be unimodal, bimodal, or multimodal. |



## 2. The Karl Pearson Empirical Relationship & Skewness

* Empirical Relationship: For moderately skewed unimodal frequency distributions, Karl Pearson established: $\text{Mode} = 3\text{Median} - 2\text{Mean}$.

* Symmetrical Distribution: Mean = Median = Mode (Skewness = 0).

* Positively Skewed Distribution (Right-tailed, e.g. national wealth): Mean > Median > Mode.

* Negatively Skewed Distribution (Left-tailed): Mean < Median < Mode.




## Previous Years Questions (PYQs) - APPSC Group-1


### Part A: Analytical Statistical Derivations

1. In a moderately skewed district health examination dataset, the mean hemoglobin level is recorded as 13.2 g/dL and the median hemoglobin level is 12.8 g/dL. Determine the mode of the distribution using Karl Pearson's empirical formula. Discuss why median is preferred over mean in reporting household per capita incomes. (APPSC Group-1 Mains Analytical, 10 Marks)
-> Model Approach: 1. Empirical Formula: Mode = 3*Median - 2*Mean. Mode = 3(12.8) - 2(13.2) = 38.4 - 26.4 = 12.0 g/dL. 2. Median vs. Mean for Household Incomes: Income distribution in developing economies is heavily right-skewed with extreme high-income billionaires at the tail. The arithmetic mean is disproportionately inflated by these outliers, creating an overly optimistic false impression of prosperity. The median represents the exact 50th percentile, unaffected by extreme fortunes, reflecting the authentic economic welfare of typical citizens.




### Part B: Screening / Prelims Objective Questions

* Q1. For a moderately skewed distribution, if the mode is 24 and the mean is 60, what is the value of the median?
(a) 36
(b) 48
(c) 52
(d) 54
Correct Answer: (b) 48 [Explanation: Using Mode = 3*Median - 2*Mean: 24 = 3*Median - 2(60) => 24 = 3*Median - 120 => 3*Median = 144 => Median = 48.]

* Q2. The average score of 50 students in an exam is 68. If the average score of boys is 64 and that of girls is 74, what is the number of boys in the class?
(a) 20
(b) 25
(c) 30
(d) 35
Correct Answer: (c) 30 [Explanation: Using alligation or weighted average: Boys avg = 64, Girls avg = 74, Combined avg = 68. Ratio (Boys : Girls) = (74 - 68) : (68 - 64) = 6 : 4 = 3 : 2. Total boys = (3 / 5) * 50 = 30 boys.]

* Q3. What is the median of the dataset: 14, 28, 19, 11, 35, 42, 22, 31, 16?
(a) 19
(b) 22
(c) 25
(d) 28
Correct Answer: (b) 22 [Explanation: Sort the 9 values in ascending order: 11, 14, 16, 19, 22, 28, 31, 35, 42. Since N = 9 (odd), the median is the ((9+1)/2)-th = 5th term. The 5th term is 22.]

* Q4. If every value in a dataset is multiplied by a constant factor k (k > 0), what happens to the standard deviation?
(a) It remains unchanged
(b) It increases by k
(c) It is multiplied by k
(d) It is multiplied by k^2
Correct Answer: (c) It is multiplied by k [Explanation: Multiplying all observations by a constant k scales the standard deviation by |k|, while the variance is scaled by k^2.]

* Q5. In a symmetrical normal distribution, what is the relationship between the Mean, Median, and Mode?
(a) Mean > Median > Mode
(b) Mode > Median > Mean
(c) Mean = Median = Mode
(d) Mean + Mode = 2 Median
Correct Answer: (c) Mean = Median = Mode [Explanation: In any perfectly symmetrical unimodal distribution, the mean, median, and mode coincide at the exact center of the distribution.]


