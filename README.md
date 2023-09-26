# Genetic-Algorithm
A fully dynamic genetic algorithm for solving the NQueens problem, complete with ancestor tracking.

## The Problem
The objective of the N-Queens problem is to place N chess queens on an N×N chessboard in such a way that no two queens threaten each other. In other words, no two queens can share the same row, column, or diagonal.  
  
Here are the key rules of the N-Queens problem:  
  
1. You have an N×N chessboard.  
2. You need to place N queens on the board.  
3. No two queens can occupy the same row.  
4. No two queens can occupy the same column.  
5. No two queens can occupy the same diagonal.

Here is a sample solution to an 8 Queens problem: 
  
![1_SVCP2lIp1jfzJuQn_QUeVg](https://github.com/tVitta/Genetic-Algorithm/assets/143434462/192f8977-33b7-4753-8620-5b31f1a52f82)  
  
This solution in array format would be [1, 7, 4, 6, 8, 2, 5, 3].  

## Code Breakdown  
The Code has been tested for up to 30 Queens (I would test more but my laptop stinks really bad). Theoretically it should work for an infinite number of queens, if you are comfortable wating for the heat death of the universe.

- **Initialization**: Various constants and parameters are defined for the genetic algorithm, including:
  - Number of queens (N)
  - Population size (POPSIZE)
  - Crossover point (CROSSOVER_POINT)
  - Cull point (CULL_POINT)
  - Mutation rate (MUTATION_RATE)
  - Generation count (gen_count)
  - List of names for individuals in the population.

- **Member Class**: A custom class called `Member` is defined to represent individuals in the population. Attributes include:
  - Name
  - Genes (queen positions)
  - Fitness (measure of conflicts)
  - Ancestor list (for parent tracking).

- **assign_rand Function**: Randomly assigns genes to create the initial generation and assigns random names to each member. This mostly for fun.

- **assign_name Function**: Randomly selects a name from a list and assigns it to an individual. Also mostly for fun.

- **initialize Function**: Sets up the initial population by calling `assign_rand` iteratively and returns a list of individuals.

- **evaluate_fitness Function**: Calculates the fitness of an individual by counting conflicts (queens attacking each other).

- **selection Function**: Culls the population based on the cull point, retaining only the fittest individuals.

- **bubble_sort Function**: Sorts the population based on fitness scores to keep the fittest individuals.

- **crossover Function**: Generates new individuals by combining the genes of two parent individuals, promoting genetic diversity.

- **mutate Function**: Introduces mutations in the genes of new child individuals based on the mutation rate.

- **printout_pop Function**: Displays information about the current population, including generation count, member names, genes, and fitness scores.

- **Main Loop**: The code enters a loop until a solution is found (fitness equals 0). In each generation, it performs selection, crossover, mutation, and sorting operations while keeping track of the generation count.

- **Solution Found**: When a solution is discovered (fitness reaches 0), it displays the name, genes, and fitness of the solution.

## Usage
To use this code, configure the parameters and constants according to your problem size. Run the code to find a valid N-Queens placement.
  
Please hire me.  

Please.  

