import customtkinter as ctk
from tkinter import ttk, messagebox
from models.salle import Salle
from services.service_salle import ServiceSalle
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des salles")
        self.geometry("700x550")
        self.service_salle = ServiceSalle()
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.cadreInfo, text="Code :").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_code = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Libellé :").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Type :").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_type = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_type.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Capacité :").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)
        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreActions, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.cadreActions, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreActions, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreActions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

    def vider_champs(self):
        self.entry_code.delete(0, "end")
        self.entry_libelle.delete(0, "end")
        self.entry_type.delete(0, "end")
        self.entry_capacite.delete(0, "end")

    def remplir_champs(self, salle):
        self.entry_code.delete(0, "end")
        self.entry_code.insert(0, salle.code)

        self.entry_libelle.delete(0, "end")
        self.entry_libelle.insert(0, salle.libelle)

        self.entry_type.delete(0, "end")
        self.entry_type.insert(0, salle.type)

        self.entry_capacite.delete(0, "end")
        self.entry_capacite.insert(0, str(salle.capacite))

    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            self.entry_capacite.get()
        )

        ok, msg = self.service_salle.ajouter_salle(salle)

        if ok:
            messagebox.showinfo("Succès", msg)
            self.vider_champs()
        else:
            messagebox.showerror("Erreur", msg)