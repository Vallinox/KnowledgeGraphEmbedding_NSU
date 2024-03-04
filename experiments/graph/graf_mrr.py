import re
import matplotlib.pyplot as plt

def extract_mrr_from_log(log_file):
    # Inizializza le liste per memorizzare gli step e i valori MRR
    steps = []
    mrr_values = []

    # Apre il file e legge le righe
    with open(log_file, 'r') as file:
        for line in file:
            # Utilizza espressione regolare per trovare le linee contenenti "Valid MRR"
            match = re.search(r'Valid MRR at step (\d+): (\d+\.\d+)', line)
            if match:
                # Estrai lo step e il valore MRR dalla riga corrispondente
                step = int(match.group(1))
                mrr = float(match.group(2))
                steps.append(step)
                mrr_values.append(mrr)
    return steps, mrr_values

path = "/Users/valeriosegreto/PycharmProjects/KnowledgeGraphEmbedding_NTU/experiments/"
name_dataset = "FB15K"
# Estrai i dati dal primo file
steps1, mrr_values1 = extract_mrr_from_log(path + name_dataset + '/train.log')

# Estrai i dati dal secondo file
steps2, mrr_values2 = extract_mrr_from_log(path + name_dataset + '/train_ntu.log')

# Estrai i dati dal terzo file
steps3, mrr_values3 = extract_mrr_from_log(path + name_dataset + '/train_variant_ntu.log')

# Plot
plt.plot(steps1, mrr_values1, marker='*', label='Self-Adversarial')
plt.plot(steps2, mrr_values2, marker='D', label='NTU')
plt.plot(steps3, mrr_values3, marker='.', label='Variant-NTU')

plt.title('MRR - ' + name_dataset)
plt.xlabel('Step')
plt.ylabel('MRR')
plt.legend()
plt.grid(True)

plt.savefig(path+name_dataset+"/" + "graph_" + name_dataset + "_mrr.png")
plt.show()