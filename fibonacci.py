#İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacci_seri = [1, 1]

while len(fibonacci_seri) < 20:
    yeni_eleman = fibonacci_seri[-1] + fibonacci_seri[-2]
    fibonacci_seri.append(yeni_eleman)

print(fibonacci_seri)
