import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import os
import platform

class SideQuestMasterControl:
    def __init__(self, root):
        self.root = root
        self.root.title("MASTER CONTROL: SIDE QUEST v1.0")
        self.root.geometry("600x500")
        self.root.configure(bg="#1a1a24")  # Koyu siberpunk/RPG teması
        
        # Stil Ayarları
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TProgressbar", thickness=20, troughcolor='#2d2d3d', background='#ff007f')
        
        # Başlık Bölümü
        self.title_label = tk.Label(
            root, 
            text="📜 ACTIVE QUESTS / MASTER CONTROL", 
            font=("Courier New", 18, "bold"), 
            fg="#00ffcc", 
            bg="#1a1a24"
        )
        self.title_label.pack(pady=15)
        
        # Görev Listesi Paneli (Quest Log)
        self.quest_frame = tk.LabelFrame(
            root, 
            text=" QUEST LOG (Sistem Durumu) ", 
            font=("Courier New", 12, "bold"),
            fg="#ffaa00", 
            bg="#1a1a24", 
            bd=2, 
            relief="groove"
        )
        self.quest_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # --- Görev 1: CPU Takibi ---
        self.cpu_label = tk.Label(self.quest_frame, text="[ ] Quest 1: Balance the Core (CPU Load)", font=("Courier New", 11), fg="#ffffff", bg="#1a1a24")
        self.cpu_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        self.cpu_bar = ttk.Progressbar(self.quest_frame, length=300, mode='determinate')
        self.cpu_bar.grid(row=0, column=1, padx=10, pady=5)
        
        # --- Görev 2: RAM Takibi ---
        self.ram_label = tk.Label(self.quest_frame, text="[ ] Quest 2: Allocate Mana (RAM Usage)", font=("Courier New", 11), fg="#ffffff", bg="#1a1a24")
        self.ram_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        
        self.ram_bar = ttk.Progressbar(self.quest_frame, length=300, mode='determinate')
        self.ram_bar.grid(row=1, column=1, padx=10, pady=5)

        # --- Görev 3: Disk Takibi ---
        self.disk_label = tk.Label(self.quest_frame, text="[ ] Quest 3: Clean the Inventory (Disk)", font=("Courier New", 11), fg="#ffffff", bg="#1a1a24")
        self.disk_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        
        self.disk_bar = ttk.Progressbar(self.quest_frame, length=300, mode='determinate')
        self.disk_bar.grid(row=2, column=1, padx=10, pady=5)

        # OS Bilgisi Alanı
        self.os_info = f"Realm: {platform.system()} {platform.release()}"
        self.os_label = tk.Label(root, text=self.os_info, font=("Courier New", 10, "italic"), fg="#8888aa", bg="#1a1a24")
        self.os_label.pack(pady=5)

        # Eylem Butonları (Abilities)
        self.btn_frame = tk.Frame(root, bg="#1a1a24")
        self.btn_frame.pack(pady=20)
        
        self.refresh_btn = tk.Button(
            self.btn_frame, 
            text="🔄 REFRESH QUESTS", 
            font=("Courier New", 11, "bold"),
            bg="#00ffcc", 
            fg="#1a1a24", 
            activebackground="#00ccaa",
            command=self.update_stats
        )
        self.refresh_btn.grid(row=0, column=0, padx=10)
        
        self.abort_btn = tk.Button(
            self.btn_frame, 
            text="💥 ABORT ALL (Exit)", 
            font=("Courier New", 11, "bold"),
            bg="#ff007f", 
            fg="#ffffff", 
            activebackground="#cc0066",
            command=root.quit
        )
        self.abort_btn.grid(row=0, column=1, padx=10)
        
        # İlk verileri yükle ve döngüyü başlat
        self.update_stats()
        self.auto_refresh()

    def update_stats(self):
        # CPU Bilgisi
        cpu_usage = psutil.cpu_percent()
        self.cpu_bar['value'] = cpu_usage
        cpu_status = "⚠️ OVERLOADED" if cpu_usage > 80 else "✅ STABLE"
        self.cpu_label.config(text=f"[{cpu_status}] Quest 1: Core Load ({cpu_usage}%)")
        
        # RAM Bilgisi
        ram = psutil.virtual_memory()
        ram_usage = ram.percent
        self.ram_bar['value'] = ram_usage
        ram_status = "⚠️ LOW MANA" if ram_usage > 85 else "🔮 READY"
        self.grid_status = f"[{ram_status}] Quest 2: Mana Usage ({ram_usage}%)"
        self.ram_label.config(text=self.grid_status)
        
        # Disk Bilgisi
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        self.disk_bar['value'] = disk_usage
        disk_status = "⚠️ FULL" if disk_usage > 90 else "🎒 SLOTS FREE"
        self.disk_label.config(text=f"[{disk_status}] Quest 3: Inventory ({disk_usage}%)")

    def auto_refresh(self):
        """Her 2 saniyede bir quest logu otomatik günceller"""
        self.update_stats()
        self.root.after(2000, self.auto_refresh)

if __name__ == "__main__":
    root = tk.Tk()
    app = SideQuestMasterControl(root)
    root.mainloop()