#By Yushima Fujiwara/IyuszTempest

import sys
import time
import os

#untuk membersihkan terminal agar tampilan fokus
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Konstanta warna ANSI
GREEN = "\033[92m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RESET = "\033[0m"

def progress_bar(duration):
    #animasi progress bar berjalan khas media player
    bars = 20
    for i in range(bars + 1):
        percent = (i / bars)
        filled = "➔" * i
        empty = " " * (bars - i)
        # progress bar di baris yang sama
        sys.stdout.write(f"\r{GRAY}[{GREEN}{filled}{empty}{GRAY}] {int(percent*100)}%{RESET}")
        sys.stdout.flush()
        time.sleep(duration / bars)
    print("\n")

def jalanin_lirik():
    # Format: (waktu_tunggu_sebelum_muncul, "teks lirik")
    lirik = [
        (0.0, "--- 🎵 Music Intro 🎵 ---"),
        (1.0, "\"senyum tipis nan menawan\""),
        (2.0, "\"gadis manis kalimantan\""),
        (2.5, "\"ma ulan ulun ta bayang-bayang\""),
        (2.5, "\"muha.. pian\""),
        (3.5, "p p apa..."),
        (2.0, "pian sungguh mempesona..."),
        (3.5, "........"),
    ]

    clear_terminal()
    print(f"{GREEN}=== 🟢 IYUSZ MUSIC ==={RESET}")
    print(f"{GRAY}Now Playing: {WHITE}Gadis Manis Kalimantan (Remix){RESET}\n")
    
    for delay, baris in lirik:
        # Jika ada delay panjang, dia manfaatin buat nampilin progress bar berjalan
        if delay > 1.5:
            progress_bar(delay)
        else:
            time.sleep(delay)
            
        # Efek mengetik per karakter dengan warna putih
        sys.stdout.write(f"{WHITE}")
        for karakter in baris:
            sys.stdout.write(karakter)
            sys.stdout.flush()
            time.sleep(0.05) 
        sys.stdout.write(f"{RESET}\n")
            
    print(f"\n\n{GREEN}--- 🏁 Music Ended 🏁 ---{RESET}")

if __name__ == "__main__":
    # Mengaktifkan dukungan warna ANSI di Windows CMD jika perlu
    if os.name == 'nt':
        os.system('color')
        
    jalanin_lirik()