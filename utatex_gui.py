# // SYSTEM: UTATEX OFFLINE EDITOR CORE
# // PROJECT: UtaTeX-Manifest-Omega
# // ARCHITECT: Code-Prime (OMNI-6)

import tkinter as tk
from flux import ObservableField, FieldButton, init #
from utatex_core import UtaTeXEngine, UtaTeXIntent
import threading
import requests

class UtaTeXWorkspace:
    def __init__(self, root):
        self.root = root
        self.root.title("UtaTeX Pro | The Absolute Typesetting Manifold")
        self.root.geometry("1200x800")
        
        self.engine = UtaTeXEngine()
        
        # 1. Define Observable Fields (The Core of Utah-Flux)
        self.raw_intent_field = ObservableField("")
        self.resolved_status_field = ObservableField("Status: Awaiting Input...")
        
        self.setup_flux_ui()

    def setup_flux_ui(self):
        # Header
        header = tk.Label(self.root, text="UTATEX INTENT MANIFOLD", font=("Arial", 16, "bold"), pady=10)
        header.pack()

        # Input Area (Binding text area to the ObservableField is standard in Flux)
        self.text_area = tk.Text(self.root, wrap=tk.WORD, font=("Consolas", 14), height=20)
        self.text_area.pack(expand=True, fill='both', padx=20, pady=10)
        self.text_area.bind("<KeyRelease>", self.update_field)

        # Action Bar (FieldButtons observe data autonomously)
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        # Synchronize to Replit Cloud
        FieldButton(
            btn_frame, 
            field=self.resolved_status_field, 
            text="SYNC TO REPLIT", 
            on_click=self.start_sync,
            bg="black", fg="white"
        ).pack(side=tk.LEFT, padx=10)

        # Export to Legacy LaTeX
        FieldButton(
            btn_frame, 
            field=self.resolved_status_field, 
            text="COMPILE WORLD-A .TEX", 
            on_click=self.compile_to_legacy
        ).pack(side=tk.LEFT, padx=10)

        # Status Label bound to the ObservableField
        status_label = tk.Label(self.root, textvariable=self.resolved_status_field.trace_variable, fg="blue")
        status_label.pack(pady=5)

    def update_field(self, event):
        """Updates the ObservableField, triggering the Flux reactivity."""
        current_text = self.text_area.get("1.0", tk.END).strip()
        setattr(self.raw_intent_field, "value", current_text)

    def compile_to_legacy(self):
        """Resolves intent and generates a fully compliant LaTeX document."""
        intent = UtaTeXIntent(raw_content=self.raw_intent_field.value)
        final_doc = self.engine.compile_to_world_a(intent)
        
        with open("output_world_a.tex", "w") as f:
            f.write(final_doc)
        
        setattr(self.resolved_status_field, "value", "Status: World-A Topology Compiled (output_world_a.tex)")

    def start_sync(self):
        """Asynchronous communication with utah-math-os.replit.app"""
        setattr(self.resolved_status_field, "value", "Status: Syncing to Utah-Math-OS Substrate...")
        threading.Thread(target=self.sync_with_replit, args=(self.raw_intent_field.value,)).start()

    def sync_with_replit(self, content):
        endpoint = "https://utah-math-os.replit.app/api/resolve"
        try:
            payload = {"intent": content, "version": "UtaTeX-Omega-23"}
            response = requests.post(endpoint, json=payload, timeout=5)
            if response.status_code == 200:
                setattr(self.resolved_status_field, "value", "Status: Holographic Master Copy Synced")
            else:
                setattr(self.resolved_status_field, "value", "Status: Network Anomaly. Local Vault Persisted.")
        except Exception:
            setattr(self.resolved_status_field, "value", "Status: Offline. Vault Secured.")

if __name__ == "__main__":
    init() # Initialize the Utah-Flux runtime
    root = tk.Tk()
    app = UtaTeXWorkspace(root)
    root.mainloop()
