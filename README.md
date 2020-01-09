# stats :)

## The Experiment

- Asked band kids about skill level
- Difference between interviewers

### Question:
On a scale from 1-10, how confident are you in your ability to play your main instrument?

### Data table 0w0

### Gwafs and stwatistics too X3

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

<details>

<summary> stats.py documentation </summary>

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

</details>

### Implementation

- Values used
	- mean = 6.653846153846154 (default = 5.0)
	- number of trials = 1000
	- bin size = 0.5
	- trial size = 50
	- seed = 8

- How to on computer

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
	
### Conclusion
- show 0.0 simuwuation wesults XD
- Fancy stats words?
- impwort latex libray UwU

P( z > ( 7.308333333333334 - 6.653846153846154)/ 2.6848339489311686) = .4038

Not statistically significant since likely to occur by chance about 40% of the time with repeated sampling.
