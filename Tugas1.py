import sys

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def angka(h):
    return alfabet.index(h)

def huruf(n):
    return alfabet[n % 26]

def normal(s):
    return "".join(ch for ch in s.upper() if ch.isalpha())

def enkrip_2x2(teks, K):
    teks = normal(teks)
    if len(teks) % 2 == 1:
        teks += "X"
    a, b = K[0]
    c, d = K[1]
    hasil = []
    langkah = []
    for i in range(0, len(teks), 2):
        p1 = angka(teks[i]); p2 = angka(teks[i+1])
        c1 = (a*p1 + b*p2) % 26
        c2 = (c*p1 + d*p2) % 26
        hasil.append(huruf(c1) + huruf(c2))
        langkah.append((teks[i], teks[i+1], p1, p2, c1, c2, huruf(c1), huruf(c2)))
    return "".join(hasil), langkah

def cetak(teks, K):
    ct, step = enkrip_2x2(teks, K)
    print("teks:", teks)
    print("kunci:", K[0], K[1])
    print("normal:", normal(teks))
    if len(normal(teks)) % 2 == 1:
        print("ganjil, nambah 'X' di belakang")
    print()
    for idx, (h1, h2, p1, p2, c1, c2, ch1, ch2) in enumerate(step, 1):
        print(f"blok {idx}: {h1}{h2} -> [{p1} {p2}]")
        print(f"  c1 = {K[0][0]}*{p1} + {K[0][1]}*{p2} = {(K[0][0]*p1 + K[0][1]*p2)} ≡ {c1} (mod 26) -> {ch1}")
        print(f"  c2 = {K[1][0]}*{p1} + {K[1][1]}*{p2} = {(K[1][0]*p1 + K[1][1]*p2)} ≡ {c2} (mod 26) -> {ch2}")
    print()
    print("ciphertext:", ct)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        teks = "PYTHON"; K = [[7,6],[2,5]]
        cetak(teks, K)
    else:
        teks = input("masukin teks (contoh: PYTHON): ").strip()
        if not teks:
            teks = "PYTHON"
        print("masukin matriks 2x2 berurutan a b c d (contoh: 7 6 2 5): ", end="")
        bagian = input().split()
        if len(bagian) == 4:
            a, b, c, d = map(int, bagian)
        else:
            a, b, c, d = 7, 6, 2, 5
        cetak(teks, [[a, b], [c, d]])
