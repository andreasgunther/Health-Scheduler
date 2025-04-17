from tkinter import *
from tkinter import ttk
from tkinter import messagebox



# Funcoes
def abrir_dashboard():
    # Esconde widgets de root
    login_frame.grid_forget()
    # Mostra widgets de dashboard
    dashboard_frame.grid()

def verificar_login():
    '''usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == 'admin' and senha == '1234':
        messagebox.showinfo("Login", "Login bem-sucedido")
        abrir_dashboard()
    else:
        messagebox.showerror("Erro", "Usuario ou senha incorretos.")'''
    abrir_dashboard()

def atualizar_rolagem_tabela(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def rolagem_mouse(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")




# Janela principal
root = Tk()
root.geometry("1280x720")
# Cor do fundo
root.configure(bg = 'black')
# Janela expansivel
#root.grid_rowconfigure(0, weight=1)
#root.grid_columnconfigure(0, weight=1)
# Titulo
root.title("Sistema de Agendamentos")
# Estilo dos widgets
style = ttk.Style()
style.theme_use('clam')
style.configure('.', background='black')
style.configure('.', font=('Consolas', 12))
style.configure('TLabel', foreground='#FFFFFF')
style.configure("Custom.TButton",
                background='black',
                foreground='white')
style.map("Custom.TButton",
          background=[('active', 'white')],
          foreground=[('active', 'black')])
style.configure("Custom.TEntry",
                foregound='white',
                fieldbackground='white',
                background='black')
style.configure("Custom.Vertical.TScrollbar",
                background="Black",
                troughcolor="Black",
                arrowcolor="Black",
                bordercolor="Black",
                relief="flat",
                width=20)




# Login frame 
login_frame = ttk.Frame(root, padding=(380, 230, 380, 230))
login_frame.grid()

# Login
ttk.Label(login_frame, text="Login").grid(row=0, column=1, pady=30)

# Usuario
ttk.Label(login_frame, text="Usuario", width=10).grid(row=1, column=0)
entrada_usuario = ttk.Entry(login_frame, width=30, font=("Consolas", 12), style='Custom.TEntry')
entrada_usuario.grid(row=1, column=1, pady=5)
# Senha
ttk.Label(login_frame, text="Senha", width=10).grid(row=2, column=0)
entrada_senha = ttk.Entry(login_frame, width=30, font=("Consolas", 12), style='Custom.TEntry')
entrada_senha.grid(row=2, column=1, pady=5)

# Espaçamento
ttk.Label(login_frame).grid(row=3, column=0)

# Entrar
ttk.Button(login_frame, text="Entrar", command=verificar_login, style='Custom.TButton').grid(row=4, column=1, pady=5)
# Sair
ttk.Button(login_frame, text="Sair", command=root.destroy, style='Custom.TButton').grid(row=5, column=1, pady=5)




# Dashboard frame
dashboard_frame = ttk.Frame(root, padding=(20, 10, 20, 10))

# Dashboard
ttk.Label(dashboard_frame, text="Dashboard", font=("Consolas", 18)).grid(row=0, column=0, pady=10, sticky='w')

# Layout (Ordem | Nome | Procedimento | Medico | Data | Horario | Telefone | SUS)
# Pacientes
ttk.Label(dashboard_frame, text=" Id |       Nome       |   Procedimento   |   Medico   |    Data    |   Horario   |   Telefone   |   SUS   ").grid(row=1, column=0, pady=10, sticky='nsew')

# Informacoes
#Configuracoes de Tela e rolagem
canvas = Canvas(dashboard_frame, width=1200, height=500, background='Black', highlightbackground='White')
canvas.grid(row=2, column=0, sticky='nsew')

barra_rolagem = ttk.Scrollbar(dashboard_frame, orient='vertical', command=canvas.yview, style="Custom.Vertical.TScrollbar")
barra_rolagem.grid(row=2, column=1, sticky='ns')

canvas.configure(yscrollcommand=barra_rolagem.set)

tabela_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=tabela_frame, anchor='nw')

tabela_frame.bind("<Configure>", atualizar_rolagem_tabela)
canvas.bind_all("<MouseWheel>", rolagem_mouse)

for i in range(50):
    ttk.Label(tabela_frame, text=f"{i+1}").grid(row=i, column=0, padx=5, pady=5)
    ttk.Label(tabela_frame, text=f"Medicine{i+1}").grid(row=i, column=1, padx=5, pady=5)

#Conteudo

# Espaçamento
ttk.Label(dashboard_frame).grid(row=3, column=0, pady=5)

# Botoes
ttk.Button(dashboard_frame, text="Excluir", style='Custom.TButton').grid(row=4, column=0, padx=(505, 0))
ttk.Button(dashboard_frame, text="Editar", style='Custom.TButton').grid(row=4, column=0, padx=(800, 0))
ttk.Button(dashboard_frame, text="Criar", style='Custom.TButton').grid(row=4, column=0, sticky='e')


root.mainloop()
