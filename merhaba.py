#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Abartılı Merhaba Dünyası
Bu kod gerçekten çalışır. Abartılıdır. Anlamsızdır. Türkçedir.
"""

import time
import random

def abartili_merhaba():
    print("=" * 50)
    print("EVREN: Bekle... düşünüyorum...")
    time.sleep(1)
    print("EVREN: Tamam, hazırım.")
    time.sleep(0.5)
    
    mesajlar = [
        "Merhaba Dünya!",
        "Merhaba... aslında tüm evren!",
        "Merhaba, ben buradayım, sen de oradasın, birlikte varız!",
        "Merhaba Dünya, seni çok seviyorum ama abartıyorum!"
    ]
    
    for i, mesaj in enumerate(mesajlar, 1):
        print(f"\n[{i}/4] {mesaj}")
        time.sleep(0.8)
        print("  -> Abartı seviyesi: " + "⭐" * (i * 2))
        time.sleep(0.3)
    
    print("\n" + "=" * 50)
    print("SONUÇ: Dünya merhaba dedi. Evren titredi. Sen güldün.")
    print("Gizli not: " + "".join([chr(ord(c) ^ 42) for c in "demokrasi"]))  # gizli şifreli şey
    print("=" * 50)

if __name__ == "__main__":
    abartili_merhaba()
    print("\nÇalıştı. Gerçekten. Abartmadım. (Abarttım.)")
