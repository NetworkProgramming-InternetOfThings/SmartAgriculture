import requests
import time
import json
import matplotlib.pyplot as plt
import networkx as nx

# ThingSpeak URL
url = "https://api.thingspeak.com/channels/2511429/feeds.json?api_key=RNAIMH1HTZLK3XYF&results=2"

# Veriyi ThingSpeak'den çekme fonksiyonu
def fetch_data():
    response = requests.get(url)
    data = json.loads(response.text)
    return data

# Grafiği oluşturma fonksiyonu
def create_graph(feed):
    G = nx.Graph()
    
    # Düğümler ekleniyor
    G.add_node(1, name='Hava Sicaklik', value=feed.get('field1', 'N/A'))
    G.add_node(2, name='Hava Nem', value=feed.get('field2', 'N/A'))
    G.add_node(3, name='Toprak Nem', value=feed.get('field3', 'N/A'))
    G.add_node(4, name='Sulama Durumu', value=feed.get('field4', 'N/A'))
    G.add_node(5, name='Sulama Saati', value=feed.get('field5', 'N/A'))
    
    # Yeni düğümler ekleniyor (ortalama değerler)
    G.add_node(6, name='Ortalama Hava Nem', value='50% - 60%')
    G.add_node(7, name='Ortalama Hava Sicaklik', value='20°C - 25°C')
    G.add_node(8, name='Ortalama Toprak Nem', value='40% - 60%')  # Ortalama toprak nemi
    
    # Kenarlar ekleniyor (mantıksal bağlantılar)
    G.add_edges_from([
        (1, 3),  # Hava Sicaklik - Toprak Nem
        (2, 3),  # Hava Nem - Toprak Nem
        (3, 4),  # Toprak Nem - Sulama Durumu
        (3, 5),  # Toprak Nem - Sulama Saati
        (4, 5),  # Sulama Durumu - Sulama Saati
        (2, 6),  # Hava Nem - Ortalama Hava Nem
        (1, 7),  # Hava Sicaklik - Ortalama Hava Sicaklik
        (3, 8)   # Toprak Nem - Ortalama Toprak Nem
    ])
    
    return G

# Grafiği çizme fonksiyonu
def draw_graph(G):
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'value')
    node_labels = nx.get_node_attributes(G, 'name')
    
    # Düğümleri çizme
    nx.draw(G, pos, with_labels=False, node_size=3000, node_color='skyblue', edge_color='gray')
    
    # Düğüm etiketlerini ve değerlerini çizme
    custom_labels = {node: f"{node_labels[node]}\n{labels[node]}" for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, custom_labels, font_size=12, font_color='black')
    
    plt.show()

# Veriyi çekme ve grafiği sürekli olarak güncelleme döngüsü
while True:
    data = fetch_data()
    
    if 'feeds' in data and len(data['feeds']) > 0:
        feed = data['feeds'][0]
        G = create_graph(feed)
        draw_graph(G)
    
    time.sleep(10)
