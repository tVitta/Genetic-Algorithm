
import random

N = 16 #Number of Queens
POPSIZE = 100
CROSSOVER_POINT = 4
CULL_POINT = 50 #How many should survive into the new generation
MUTATION_RATE = 2 #Number of alleles to randomly mutate between generations

gen_count = 1

names = [ "Mohammed", "Sophia", "Aiden", "Ava", "Omar", "Mia", "Ahmed", "Isabella", "Ali", "Olivia", "Youssef", "Emma", "Amir", "Aaliyah", 
         "Zara", "Khaled", "Leila", "Juan", "Sofia", "Alex", "Gabe", "Akira", "Sakura", "Hiroshi", "Mei", "Igo", "Tas", "Yoongi", "Tommy",
         "Hussain", "Pranay", "Kaitlyn", "Shai", "Rahul", "Eva", "Max", "Luna", "Ravi", "Anaya", "Carlos", "Penelope", "Liam", "Maya", "Faisal", 
         "Lina", "Samir", "Amara", "Javier", "Selena", "Yusuf", "Elena", "Rohan", "Nora", "Jaden", "Aria", "Hamza", "Layla", "Luca", "Avery", 
         "Zayn", "Zoe", "Emir", "Chloe", "Nabil", "Leah", "Raja", "Aisha", "Ziad", "Fatima", "Ibrahim", "Hannah", "Kian", "Aaliyah", "Tariq", 
         "Sara", "Aliyah", "Victoria", "Fahad", "Gabriella", "Amira", "Stella", "Nasir", "Penelope", "Rami", "Mila", "Omar", "Aurora", "Elias",
        "Camila", "Hasan", "Eleanor", "Adam", "Lucy", "Khalid", "Lily", "Areesha", "Crystal", "Stelvid", "Nathan", "Misala", "Anojan", "Shamil",
        "Khris", "Micheal", "Imran", "Sim", "John", "Ash", "Matthew", "Tahmeed", "Aatka", "Julie", "Kai", "Wong", "Prayag", "Robbie", "Russell",
        "Shivani", "Thanoshan", "Vasu"]

class Member: #Custom data type for ease of coding and readability's sake 
    def __init__(self, name, genes, fitness, ancestor):
        self.Name = name
        self.Genes = genes
        self.Fitness = fitness
        self.Ancestor = ancestor

def assign_rand(num): #This randomly assigns the genes of the first generation
    a = Member("Temp", [0]*num, 0, [])
    for i in range(num):
        a.Name = assign_name(a.Name)
        a.Genes[i] = random.randint(1, num)
        a.Fitness = evaluate_fitness(a.Genes)
    return a

def assign_name(mem): #This randomly assigns a name to each of the strings of genes
    mem = names[random.randint(0, len(names) - 1)] 
    return mem

def intialize(n, popSize): #This calls assign_rand for the whole population
    pop = []
    for i in range(popSize):
        pop.append(assign_rand(n))
    return pop

def old_fitness(mem): #old code which only worked for 8 Queens, dont worry about it, I worked too hard on it to just delete it
    score = 0
    
    for row in range(N):
        col = mem[row]
        for other_row in range(N):
            if other_row == row:
                continue
            if mem[other_row] == col:
                continue
            if other_row + mem[other_row] == row + col:
                continue
            if other_row - mem[other_row] == row - col:
                continue
            score += 1
    
    return score/2

def evaluate_fitness(genes): #This evaluates the fitness score of whatever member you pass to it
    size = len(genes)
    clashes = 0
    for i in range(size - 1):
        for j in range(i + 1, size):
            # Check if queens clash horizontally or diagonally
            if genes[i] == genes[j] or abs(genes[i] - genes[j]) == abs(i - j):
                clashes += 1
    
    return clashes

def selection(pop): #This culls the population based on the cull point
    total = 0
    size = len(pop)

    murdered = []
    murderedNames = []

    for i in range(CULL_POINT, size):
        murdered.append(i)
        murderedNames.append(pop[i].Name)
           
    for index in sorted(murdered, reverse=True):
        pop.pop(index)

    return pop

def bubble_sort(arr): #This sorts the population by fitness score so that the culling gets rid of the less fit
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j].Fitness > arr[j + 1].Fitness:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def bubble_sort_new(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
                
def crossover(pop): #This crosses over the genes of two members of the population
    global gen_count
    gen_count += 1
    size = len(pop)
    new_pop = []
    childPerPair = round((POPSIZE - size) / (size/2))
    for i in range(0, size, 2):
        try:
            childArr = []
            for j in range(childPerPair):
                childPop = Member("Temp", [] * N, 0, [])
                childPop.Genes = pop[i].Genes[:len(pop[i].Genes)//2] + pop[i+1].Genes[len(pop[i+1].Genes)//2:]
                childPop.Name = assign_name(childPop.Name)
                if pop[i].Ancestor != []:
                    childPop.Ancestor.append(pop[i].Ancestor)
                childPop.Ancestor.append(pop[i].Name + " & " + pop[i+1].Name)
                new_pop.append(childPop)
                childArr.append(childPop.Name)
      
        except IndexError:
            print("Could not breed: " + pop[i].Name)
    if len(new_pop) + size < POPSIZE:
        for i in range(POPSIZE - (len(new_pop) + size)):
            try:
                childPop = Member("Temp", [] * N, 0, [])
                childPop.Genes = pop[i].Genes[:len(pop[i].Genes)//2] + pop[i+1].Genes[len(pop[i+1].Genes)//2:]
                childPop.Name = assign_name(childPop.Name)
                childPop.Ancestor.append(pop[i].Name + " & " + pop[i+1].Name)
                new_pop.append(childPop)
                childArr.append(childPop.Name)
            except IndexError:
                print("Could not breed: " + pop[i].Name)
    return new_pop

def mutate(new_pop): #this mutates the new child member's genes based on the mutation rate
    global gen_count
    randAllele = 10
    for member in new_pop:
        randArr = []
        for i in range(MUTATION_RATE):
            while True:
                randAllele = random.randint(0, N - 1)
                if randAllele not in randArr:
                    randArr.append(randAllele)
                    break
            try:
                member.Genes[randAllele] = random.randint(1, N)
            except IndexError:
                print("Error: " +str(randAllele))
    for member in new_pop:
        member.Fitness = evaluate_fitness(member.Genes)
    return new_pop

def printout_pop(pop): 
    global gen_count
    print("Generation: " + str(gen_count))
    max_name_length = max(len(member.Name) for member in pop)
    if gen_count == 1:
        for member in pop:
            gene_str = ", ".join(str(gene) for gene in member.Genes)  # Convert the gene list to a string
            print(f"{member.Name.ljust(max_name_length)}->    [{gene_str}] fitness: {member.Fitness}")
    else:
        for member in pop:
            gene_str = ", ".join(str(gene) for gene in member.Genes)  # Convert the gene list to a string
            print(f"{member.Name.ljust(max_name_length)}->    [{gene_str}] | fitness: {member.Fitness} |")
    print("PopSize = " + str(len(pop)))
    print("")
        
    return None
                
pop = intialize(N, POPSIZE)

bubble_sort(pop)


while pop[0].Fitness != 0:
    selection(pop)
    new_pop = crossover(pop)
    mutate(new_pop)
    pop = pop + new_pop
    bubble_sort(pop)
 
    
    
print(str(N) + " Queens solved in " + str(gen_count) + " generations by:")

max_name_length = max(len(member.Name) for member in pop)

gene_str = ", ".join(str(gene) for gene in pop[0].Genes)  # Convert the gene list to a string
print(f"{pop[0].Name.ljust(max_name_length)}->    [{gene_str}] | fitness: {pop[0].Fitness} |")
