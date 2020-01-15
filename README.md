# stats :)

## The Experiment

- Asked band kids about skill level
- Difference between interviewers

### Question:
On a scale from 1-10, how confident are you in your ability to play your main instrument?

### Data table

|Group | Result|
| --- | --- |
|A|8|
|A| |
|A|5|
|A|8|
|A|7|
|A|7|
|A|5|
|A|6|
|A|8|
|A|7|
|A|6|
|A|9|
|A|5|
|A|5.5|
|B|9|
|B|6|
|B|7|
|B|6|
|B|6|
|B|8|
|B|8.7|
|B|7|
|B|7|
|B|7|
|B| |
|B|9|
|B|7|

### Group A
<img src="https://raw.githubusercontent.com/FrostForth/stats/master/Images/a1.png" alt="Histogram of Group A" height="500">
<img src="https://raw.githubusercontent.com/FrostForth/stats/master/Images/a2.png" alt="Dotplot of Group A" height="500">

Mean: 6.653846153846154
Standard Dev: 2.6848339489311686

### Group B
<img src="https://raw.githubusercontent.com/FrostForth/stats/master/Images/b1.png" alt="Histogram of Group B" height="500">
<img src="https://raw.githubusercontent.com/FrostForth/stats/master/Images/b2.png" alt="Dotplot of Group B" height="500">

Mean: 7.308333333333334
Standard Dev: 2.8236018261658766

## The Simulation

### Design

- Program explanation
	- one trial
		- each trial individual random mean
		- centered around group A's mean
	- stopping / looping
		- fifty individuals
	- recording
		- record mean of trial
	- repeats
		- repeat 1000 times

### stats.py documentation
1. Provide library of functions:
    - intialize
    - sample
    - graph
    - stats
    - output
2. Execute functions depending on version
    1. Import necessary libraries
	- os
	- sys
	- numpy
	- matplotlib pyplot and ticker
	- seaborn
	- pandas
	- math
    2. Set default variables
	- mean = 5.0
	- number of trials = 1000
	- bin size = 0.5
	- trial size = 50
    3. Use user-imputted values for variables if applicible
    
	1. Check for values from command line or input fields
	2. Update each corresponding value
    4. Take the sample
    
	1. Make a list of length t
	2. Append the average value of the list to list of averages
	3. Repeat n times
    5. Create and output graphs
    
	1. Histogram
	2. Dotplot
    6. Calculate statistical data
	- Mean
	- Standard Deviation
    7. Output results
    
	1. graphs and stats
	2. save to file if chosen in command line

### Implementation

- Values used
	- mean = 6.653846153846154 (default = 5.0)
	- number of trials = 1000
	- bin size = 0.5
	- trial size = 50
	- seed = 8

### How to run locally

Make sure you have Python 3 and these libraries installed in addition to the cloned repository:
	
	
	pip install sys
	pip install numpy
	pip install seaborn
	pip install matplotlib.pyplot

Navigate to the statsweb folder in the main directory.
Then you can run the program to generate the graphs.
	
	py stats.py p n b t s
p
: mean value (used to be proportion)

n
: number of trials

b
: bin size

t
: trial size

s
: seed for random generation
	
Example using the default values:

	py stats.py p=.5 n=1000 b=5 t=50
	
All values are optional and can be inputted in any order.

The script can also read from a csv file with two groups: A and B. The other command line prompts are not necessary. I did this to generate the statistics and graphs for the data file.

	py stats.py data.csv
	
## Conclusion
### Results

<img src="https://raw.githubusercontent.com/FrostForth/stats/master/Images/sim1.png" alt="Histogram of Simuwuation" height="500">
<img src="https://raw.githubusercontent.com/FrostForth/stats/master/Images/sim2.png" alt="Dotplot of Simuwuation" height="500">

Mean: 4.995999999999995
Standard Dev: 2.236291796926554

### Conclusion
Since only 148 of the 1000 simulated trials had an average greater than 7.3083, the results of group B are not statistically significant. It is likely that the results were obtained by random chance and not as a result of the difference between the interviewers.
