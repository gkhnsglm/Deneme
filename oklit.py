import math

# Öklid Mesafesini Hesaplayan Fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 2D Noktaları Tanımlayan Liste
points = [(1, 2), (3, 4), (5, 6), (7, 8), (2, 3)]

# Mesafeleri Saklayacak Liste
distances = []

# Noktalar Arasındaki Mesafeleri Hesaplayan Döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Mesafeler İçin Minimum Değeri Bulma
min_distance = min(distances)

# Minimum Mesafeyi Yazdırma
print(f"Minimum mesafe: {min_distance}")
