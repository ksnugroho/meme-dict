meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "AGGRO": "Untuk menjadi agresif/marah"
            }

for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    
    if word == "END":
        print("Program Selesai. Terima kasih")
        break
            
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Kata tidak ditemukan")

