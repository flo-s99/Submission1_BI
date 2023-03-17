#TKinter importieren und als tk callen
import tkinter as tk

#Counter initialisieren (bei 0)
counter = 0 
# Definieren der funktion counter_label, nimmt als argument das label
def counter_label(label):
  # In der funktion wird die funktion count definiert, nimmt keine argumente, die den globalen Zähler counter um eins erhöht, den Text des Labels auf den neuen Wert updatet und die Funktion count nach einer Sekunde erneut aufruft. 
  # Echtzeit Aktualisierung vom Sek Zähler so möglich
  def count():
    global counter
    # Counter wird um 1 erhöht
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  # Count Funktion callen
  count()
 
# Erstellung eines neuen Objekts - Hauptfenster der Anwendung
root = tk.Tk()
# Definieren des Titels des Fensters das sich öffnet
root.title("Sekundenzähler")
# Label in root platzieren mit arguments, standart Objekt in Tkinter
label = tk.Label(root, fg="green")
# Label tatsächlich in Fenster platzierne
label.pack()
# Ausführung der oben definierten Funktion, also dem counter mit argument=label
counter_label(label)
# Konstruktion eines Buttons, standart Objekt in TKinter mit args, command=root.destroz definiert dass die Anwendung geschlossen wird sobald Button gedrückt
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
# Button tatsächlich im Fenster platzieren
button.pack()
#Mainloop starten um Anwendung zu executen
root.mainloop()

