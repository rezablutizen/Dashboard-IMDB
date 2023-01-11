import pandas as pd
import matplotlib.pyplot as plt
import os
import keyboard

df = pd.read_csv('imdb.csv')


def dashboard():
    print('+===================================+')
    print(f"| {'Hello,':<34}|")
    print(f"| {'Selamat Datang di Dashboard IMDB':<34}|")
    print(f"| {'by.':<34}|")
    print(f"| {'> NIM   : 1912500913':<34}|")
    print(f"| {'> NAMA  : Reza Kurniawan':<34}|")
    print("+-----------------------------------+")
    print("|               MENU                |")
    print("+-----------------------------------+")
    print("| [1] Total Film                    |")
    print("| [2] Bahasa                        |")
    print("| [3] Negara                        |")
    print("| [4] Genre                         |")
    print("| [5] Color                         |")
    print("| [6] Bar Chart Genre               |")
    print("| [7] Resume Budget dan Revenue     |")
    print("| [8] Query (Genre dan Color)       |")
    print("|                                   |")
    print("| [0] Exit                          |")
    print('+===================================+')


def pilihan1():
    total_film = df['Title'].unique()
    print(f"Dataset IMDB saat ini memiliki {len(total_film)} film")

def pilihan2():
    bahasa = df['Language'].unique()
    print(f"Dataset IMDB saat terdiri dari {len(bahasa)} bahasa")

def pilihan3():
    negara = df['Country'].unique()
    print(f"Terdapat {len(negara)} negara dalam dataset IMDB")

def pilihan4():
    genre = df['Genre'].unique()
    print(f"Jenis genre terbagai ke dalam {len(genre)} genre, yaitu:")
    for i in df['Genre'].unique():
        print(f"-{i}")

def pilihan5():
    color = df['Color/B&W'].unique()
    print(f"Jenis warna terbagai ke dalam {len(color)} warna, yaitu:")
    for i in df['Color/B&W'].unique():
        print(f"-{i}")

def pilihan6():
    df.Genre.value_counts().sort_index(ascending=True).plot(kind='bar',title='Film Berdasarkan Genre')
    plt.show()

def pilihan7():
    print("Budget Resume")
    print("===============")
    total = df['Budget'].sum()
    print(f"Total         : $ {total}")
    mean = df['Budget'].mean()
    print(f"Rata-rata     : $ {mean}")
    terendah =  df['Budget'].min()
    print(f"Terendah      : $ {terendah} ")
    tertinggi = df['Budget'].max()
    print(f"Tertinggi     : $ {tertinggi} ")
    #============================================
    print("\nGross Revenue Resume")
    print("===============")
    total = df['Gross Revenue'].sum()
    print(f"Total         : $ {total}")
    mean = df['Gross Revenue'].mean()
    print(f"Rata-rata     : $ {mean}")
    terendah =  df['Gross Revenue'].min()
    print(f"Terendah      : $ {terendah} ")
    tertinggi = df['Gross Revenue'].max()
    print(f"Tertinggi     : $ {tertinggi} ")

def pilihan8():
    while True:
        
        pilihan_genre = input("\n>> Input Genre yang dicari : \n")
        pilihan_color = input(">> Color/B&W ?\n")
        df_new = df[(df['Color/B&W'] == pilihan_color) & 
                    df['Genre'].isin([pilihan_genre])]
        print(df_new.head())

        film = df_new['Title'].unique()
        print(f"\nTotal Film Genre Action dan Color adalah : {len(film)} Film\n")

        #=======Budget========
        total_budget = df_new['Budget'].sum()
        print(f"Total Budget            : $ {total_budget}")

        rata_rata = df_new['Budget'].mean()
        print(f"Rata-rata Budget        : $ {rata_rata}")

        min = df_new['Budget'].min()
        min_film = list(df_new[df_new['Budget'] == df_new['Budget'].min()]['Title'])
        print(f"Budget Terendah         : $ {min}, Judul: {min_film}")

        max = df_new['Budget'].max()
        max_film = list(df_new[df_new['Budget'] == df_new['Budget'].max()]['Title'])
        print(f"Budget Tetinggi         : $ {max}, Judul: {max_film}")


        #=======Gross Revenue========
        total_gross = df_new['Gross Revenue'].sum()
        print(f"\nTotal Gross Revenue     : $ {total_gross}")

        rata_rata = df_new['Gross Revenue'].mean()
        print(f"Rata-rata Gross Revenue : $ {rata_rata}")

        min = df_new['Gross Revenue'].min()
        min_film = list(df_new[df_new['Gross Revenue'] == df_new['Gross Revenue'].min()]['Title'])
        print(f"Gross Revenue Terendah  : $ {min}, Judul: {min_film}")

        max = df_new['Gross Revenue'].max()
        max_film = list(df_new[df_new['Gross Revenue'] == df_new['Gross Revenue'].max()]['Title'])
        print(f"Gross Revenue Tetinggi  : $ {max}, Judul: {max_film}")
        print()
        pilihan = input("Ingin lanjut ? (y/n) : ")
        if pilihan == "n":
            break

while True:  
    os.system('cls')
    dashboard()
    pilihan = int(input("\nInput Pilihan : "))
    print()
    if pilihan == 1:
        pilihan1()
    elif pilihan == 2:
        pilihan2()
    elif pilihan == 3:
        pilihan3()
    elif pilihan == 4:
        pilihan4()
    elif pilihan == 5:
        pilihan5()
    elif pilihan == 6:
        pilihan6()
    elif pilihan == 7:
        pilihan7()
    elif pilihan == 8:
        pilihan8()
    elif pilihan == 0:
        break
    else:
        print('Input Salah, Coba lagi.')

    print()
    print("\n\nTekan Spasi untuk kembali")
    while True:  
        try:  
            if keyboard.is_pressed(' '): 
                break
        except:
            pass
