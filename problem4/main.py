"""
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
"""

harga = int(input("Input Harga: "))
diskon = int(input("Input Diskon: "))

harga_setelah_diskon = harga - (diskon / 100 * harga)
print(f"harga yang harus dibayar adalah Rp. {harga_setelah_diskon}")
