import re
import matplotlib.pyplot as plt

def extract_mr_from_log(log_file):
    # Inizializza le liste per memorizzare gli step e i valori MRR
    steps = []
    mrr_values = []

    # Apre il file e legge le righe
    with open(log_file, 'r') as file:
        for line in file:
            # Utilizza espressione regolare per trovare le linee contenenti "Valid MRR"
            match = re.search(r'Valid MR at step (\d+): (\d+\.\d+)', line)
            if match:
                # Estrai lo step e il valore MR dalla riga corrispondente
                step = int(match.group(1))
                mr = float(match.group(2))
                steps.append(step)
                mrr_values.append(mr)
    return steps, mrr_values

path = "/Users/valeriosegreto/PycharmProjects/KnowledgeGraphEmbedding_NTU/experiments/"
name_dataset = "WN18RR"
# Estrai i dati dal primo file
steps1, mr_values1 = extract_mr_from_log(path + name_dataset + '/train.log')

# Estrai i dati dal secondo file
steps2, mr_values2 = extract_mr_from_log(path + name_dataset + '/train_ntu.log')

# Estrai i dati dal terzo file
steps3, mr_values3 = extract_mr_from_log(path + name_dataset + '/train_variant_ntu.log')

# Plot
plt.style.use("seaborn")
print(plt.style.available)

plt.plot(steps1, mr_values1,linewidth=2, color="darkred", label='Self-Adversarial')
plt.plot(steps2, mr_values2,linewidth=2, label='NTU')
plt.plot(steps3, mr_values3,linewidth=2, label='Variant-NTU')

plt.yscale('log')
plt.title('MR - ' + name_dataset)
plt.xlabel('Epochs')
plt.ylabel('MR')
plt.legend(loc="best")
plt.grid(True)


plt.savefig(path+name_dataset+"/" + "graph_" + name_dataset + "_mr.png")
plt.show()