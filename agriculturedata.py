import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd 

# CSV dosyasını okuma
df = pd.read_csv('"C:\Users\Emine\OneDrive\Masaüstü\Akıllı Tarım\veri.csv"')

# Graf oluşturma
G = nx.Graph()

# Düğümleri ve kenarları ekleme
for index, row in df.iterrows():
    crop = row['Crop_Name']
    G.add_node(crop, size=3000, color='skyblue', label=crop)  # Crop_Name düğümü ekle

    # Mineralleri düğüm olarak ekleme ve bitki ile mineraller arasında kenar oluşturma
    for mineral, value in row.items():
        if mineral != 'Crop_Name':
            mineral_label = f"{mineral} ({value})"
            G.add_node(mineral_label, size=1500, color='lightgreen', label=mineral_label)  # Her mineral için düğüm oluşturma
            G.add_edge(crop, mineral_label)  # Bitkiler ile mineraller arasında kenar oluşturma

# Grafı çizdirme
plt.figure(figsize=(14, 10))

# Crop_Name düğümlerinin rengini ve boyutunu ayarlama
node_colors = [G.nodes[node]['color'] for node in G.nodes]
node_sizes = [G.nodes[node]['size'] for node in G.nodes]

# Düğümlerin konumunu belirleme
pos = nx.spring_layout(G, k=0.50)

nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=node_sizes, font_size=10, font_weight='bold')

plt.title('Bitkiler ve Mineraller Arasındaki İlişkiler')
plt.show()