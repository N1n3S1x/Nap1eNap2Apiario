import tkinter as tk
from tkinter import messagebox
from database.operacoes_genericas_banco import OperacoesBanco
from models.endereco import Endereco
from models.apicultor import Apicultor
from models.apiario import Apiario
from database.conexao_banco import ConexaoBanco


class MainWindow:
    def __init__(self, root):
        """
        Inicializa a janela principal.
        :param root: Instância da janela principal do tkinter.
        """
        self.root = root
        self.root.title("Gerenciador de Endereços e Usuários")
        self.root.geometry("500x400")

        # Configuração de conexão ao banco de dados
        self.conexao = ConexaoBanco("localhost", "root", "admin", "ApisCoop")
        self.conexao.conectar()
        self.operacoes = OperacoesBanco(self.conexao)

        # Aba de navegação
        self.tab_control = tk.Frame(self.root)
        self.tab_control.pack(fill=tk.BOTH, expand=True)

        self.menu_inicial()

    def menu_inicial(self):
        """
        Cria o menu inicial com opções para gerenciamento de Endereços e Usuários.
        """
        # Limpa o conteúdo atual
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Gerenciador de Endereços e Apicultores", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.tab_control, text="Gerenciar Endereços", font=("Arial", 14), command=self.menu_enderecos).pack(pady=10)
        tk.Button(self.tab_control, text="Gerenciar Apicultores", font=("Arial", 14), command=self.menu_apicultores).pack(pady=10)
        tk.Button(self.tab_control, text="Gerenciar Apiario", font=("Arial", 14), command=self.menu_apiario).pack(pady=10)

    def menu_enderecos(self):
        """
        Menu para gerenciar endereços.
        """
        # Limpa o conteúdo atual
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Gerenciar Endereços", font=("Arial", 16)).pack(pady=10)

        # Formulário de cadastro de endereço
        tk.Label(self.tab_control, text="Logradouro:").pack()
        logradouro_entry = tk.Entry(self.tab_control)
        logradouro_entry.pack()

        tk.Label(self.tab_control, text="Bairro:").pack()
        bairro_entry = tk.Entry(self.tab_control)
        bairro_entry.pack()

        tk.Label(self.tab_control, text="Cidade:").pack()
        cidade_entry = tk.Entry(self.tab_control)
        cidade_entry.pack()

        tk.Label(self.tab_control, text="Estado:").pack()
        estado_entry = tk.Entry(self.tab_control)
        estado_entry.pack()

        tk.Label(self.tab_control, text="CEP:").pack()
        cep_entry = tk.Entry(self.tab_control)
        cep_entry.pack()

        tk.Button(self.tab_control, text="Cadastrar Endereço",
                  command=lambda: self.cadastrar_endereco(
                      logradouro_entry.get(),
                      bairro_entry.get(),
                      cidade_entry.get(),
                      estado_entry.get(),
                      cep_entry.get()
                  )).pack(pady=10)

        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=10)

    def menu_apicultores(self):
        """
        Menu para gerenciar usuários.
        """
        # Limpa o conteúdo atual
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Gerenciar Apicultores", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.tab_control, text="Cadastrar Apicultor", font=("Arial", 12),
                  command=self.formulario_apicultor).pack(pady=5)

        tk.Button(self.tab_control, text="Buscar Apicultor", font=("Arial", 12),
                  command=self.buscar_apicultor).pack(pady=5)

        tk.Button(self.tab_control, text="Atualizar Apicultor", font=("Arial", 12),
                  command=self.atualizar_apicultor).pack(pady=5)

        tk.Button(self.tab_control, text="Excluir Apicultor", font=("Arial", 12),
                  command=self.excluir_apicultor).pack(pady=5)

        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=20)

    def menu_apiario(self):
        """
        Menu para gerenciar usuários.
        """
        # Limpa o conteúdo atual
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Gerenciar Apiario", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.tab_control, text="Cadastrar Apiario", font=("Arial", 12),
                    command=self.formulario_apiario).pack(pady=5)

        tk.Button(self.tab_control, text="Buscar Apiario", font=("Arial", 12),
                    command=self.buscar_apiario).pack(pady=5)

        tk.Button(self.tab_control, text="Atualizar Apiario", font=("Arial", 12),
                    command=self.atualizar_apiario).pack(pady=5)

        tk.Button(self.tab_control, text="Excluir Apiario", font=("Arial", 12),
                    command=self.excluir_apiario).pack(pady=5)

        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=20)
      
    def formulario_apiario(self):
        # Formulário de cadastro de apiario

        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Nome do Apiario:").pack()
        nome_apiario_entry = tk.Entry(self.tab_control)
        nome_apiario_entry.pack()

        tk.Label(self.tab_control, text="Localização:").pack()
        localizacao_entry = tk.Entry(self.tab_control)
        localizacao_entry.pack()

        tk.Label(self.tab_control, text="Tamanho:").pack()
        tamanho_entry = tk.Entry(self.tab_control)
        tamanho_entry.pack()
        
        tk.Label(self.tab_control, text="Id Apicultor:").pack()
        id_apicultor_entry = tk.Entry(self.tab_control)
        id_apicultor_entry.pack()

        tk.Button(self.tab_control, text="Cadastrar Apiario",
                  command=lambda: self.cadastrar_apiario(
                      nome_apiario_entry.get(),
                      localizacao_entry.get(),
                      tamanho_entry.get(),
                      id_apicultor_entry.get()
                  )).pack(pady=10)

        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=10)    
         
    def formulario_apicultor(self):
        # Formulário de cadastro de usuário

        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Nome do Apicultor:").pack()
        nome_entry = tk.Entry(self.tab_control)
        nome_entry.pack()

        tk.Label(self.tab_control, text="E-mail:").pack()
        email_entry = tk.Entry(self.tab_control)
        email_entry.pack()

        tk.Label(self.tab_control, text="ID do Endereço:").pack()
        endereco_id_entry = tk.Entry(self.tab_control)
        endereco_id_entry.pack()

        tk.Button(self.tab_control, text="Cadastrar Apicultor",
                  command=lambda: self.cadastrar_apicultor(
                      nome_entry.get(),
                      email_entry.get(),
                      endereco_id_entry.get()
                  )).pack(pady=10)

        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=10)

    def cadastrar_endereco(self, logradouro, bairro, cidade, estado, cep):
        """
        Cadastra um novo endereço no banco de dados.
        """
        if not logradouro or not bairro or not cidade or not estado or not cep:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        endereco = Endereco(logradouro, bairro, cidade, estado, cep)
        self.operacoes.inserir("endereco", ["logradouro", "bairro", "cidade", "estado", "cep"],
                               [logradouro, bairro, cidade, estado, cep])
        messagebox.showinfo("Sucesso", "Endereço cadastrado com sucesso!")

    def buscar_endereco(self):
        """
        Abre um formulário para buscar um endereço pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Buscar Endereço", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do Endereço:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        def realizar_busca():
            try:
                id_endereco = int(id_entry.get())
                endereco = self.operacoes.buscar_por_id("endereco", "id_endereco", id_endereco)
                if endereco:
                    result_text = f"Logradouro: {endereco['logradouro']}\n" \
                                  f"Bairro: {endereco['bairro']}\n" \
                                  f"Cidade: {endereco['cidade']}\n" \
                                  f"Estado: {endereco['estado']}\n" \
                                  f"CEP: {endereco['cep']}"
                    messagebox.showinfo("Resultado da Busca", result_text)
                else:
                    messagebox.showinfo("Resultado da Busca", "Endereço não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar endereço: {e}")

        tk.Button(self.tab_control, text="Buscar", command=realizar_busca).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_enderecos).pack(pady=10)

    def atualizar_endereco(self):
        """
        Abre um formulário para atualizar um endereço.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Atualizar Endereço", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do Endereço:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        tk.Label(self.tab_control, text="Novo Logradouro:").pack()
        logradouro_entry = tk.Entry(self.tab_control)
        logradouro_entry.pack()

        tk.Label(self.tab_control, text="Novo Bairro:").pack()
        bairro_entry = tk.Entry(self.tab_control)
        bairro_entry.pack()

        tk.Label(self.tab_control, text="Nova Cidade:").pack()
        cidade_entry = tk.Entry(self.tab_control)
        cidade_entry.pack()

        tk.Label(self.tab_control, text="Novo Estado:").pack()
        estado_entry = tk.Entry(self.tab_control)
        estado_entry.pack()

        tk.Label(self.tab_control, text="Novo CEP:").pack()
        cep_entry = tk.Entry(self.tab_control)
        cep_entry.pack()

        def realizar_atualizacao():
            try:
                id_endereco = int(id_entry.get())
                dados = {
                    "logradouro": logradouro_entry.get() or None,
                    "bairro": bairro_entry.get() or None,
                    "cidade": cidade_entry.get() or None,
                    "estado": estado_entry.get() or None,
                    "cep": cep_entry.get() or None
                }
                # Remove campos vazios
                dados = {key: value for key, value in dados.items() if value is not None}

                if not dados:
                    messagebox.showwarning("Aviso", "Nenhum dado foi fornecido para atualização.")
                    return

                self.operacoes.atualizar("endereco", "id_endereco", id_endereco, dados)
                messagebox.showinfo("Sucesso", "Endereço atualizado com sucesso!")
                self.menu_enderecos()
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar endereço: {e}")

        tk.Button(self.tab_control, text="Atualizar", command=realizar_atualizacao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_enderecos).pack(pady=10)

    def excluir_endereco(self):
        """
        Abre um formulário para excluir um endereço pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Excluir Endereço", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do Endereço:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        def realizar_exclusao():
            try:
                id_endereco = int(id_entry.get())
                self.operacoes.excluir("endereco", "id_endereco", id_endereco)
                messagebox.showinfo("Sucesso", "Endereço excluído com sucesso!")
                self.menu_enderecos()
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir endereço: {e}")

        tk.Button(self.tab_control, text="Excluir", command=realizar_exclusao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_enderecos).pack(pady=10)

    def cadastrar_apicultor(self, nome, email, endereco_id):
        """
        Cadastra um novo usuário no banco de dados.
        """
        if not nome or not email or not endereco_id:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        try:
            endereco_id = int(endereco_id)
        except ValueError:
            messagebox.showerror("Erro", "O ID do Endereço deve ser um número.")
            return

        apicultor = Apicultor(nome, email, endereco_id)
        self.operacoes.inserir("apicultor", ["nome_apicultor", "email", "endereco"], [nome, email, endereco_id])
        messagebox.showinfo("Sucesso", "Apicultor cadastrado com sucesso!")

    def buscar_apicultor(self):
        """
        Abre um formulário para buscar um usuário pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Buscar Apicultor", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do Apicultor:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        def realizar_busca():
            try:
                id_apicultor = int(id_entry.get())
                apicultor = self.operacoes.buscar_por_id("apicultor", "id_apicultor", id_apicultor)
                if apicultor:
                    result_text = f"Nome: {apicultor['nome_apicultor']}\n" \
                                  f"E-mail: {apicultor['email']}\n" \
                                  f"ID Endereço: {apicultor['endereco']}"
                    messagebox.showinfo("Resultado da Busca", result_text)
                else:
                    messagebox.showinfo("Resultado da Busca", "Apicultor não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar apicultor: {e}")

        tk.Button(self.tab_control, text="Buscar", command=realizar_busca).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apicultores).pack(pady=10)

    def atualizar_apicultor(self):
        """
        Abre um formulário para atualizar um apicultor.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Atualizar Apicultor", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do apicultor:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        tk.Label(self.tab_control, text="Novo Nome:").pack()
        nome_entry = tk.Entry(self.tab_control)
        nome_entry.pack()

        tk.Label(self.tab_control, text="Novo E-mail:").pack()
        email_entry = tk.Entry(self.tab_control)
        email_entry.pack()

        tk.Label(self.tab_control, text="Novo ID do Endereço:").pack()
        endereco_id_entry = tk.Entry(self.tab_control)
        endereco_id_entry.pack()

        def realizar_atualizacao():
            try:
                id_apicultor = int(id_entry.get())
                dados = {
                    "nome_apicultor": nome_entry.get() or None,
                    "email": email_entry.get() or None,
                    "endereco": endereco_id_entry.get() or None,
                }

                # Remove campos vazios
                dados = {key: value for key, value in dados.items() if value is not None}

                if not dados:
                    messagebox.showwarning("Aviso", "Nenhum dado foi fornecido para atualização.")
                    return

                # Converte endereco para inteiro se fornecido
                if "endereco" in dados:
                    try:
                        dados["endereco"] = int(dados["endereco"])
                    except ValueError:
                        messagebox.showerror("Erro", "O ID do Endereço deve ser um número.")
                        return

                self.operacoes.atualizar("apicultor", "id_apicultor", id_apicultor, dados)
                messagebox.showinfo("Sucesso", "Apicultor atualizado com sucesso!")
                self.menu_apicultores()
            except ValueError:
                messagebox.showerror("Erro", "O ID do Apicultor deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar apicultor: {e}")

        tk.Button(self.tab_control, text="Atualizar", command=realizar_atualizacao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apicultores).pack(pady=10)

    def excluir_apicultor(self):
        """
        Abre um formulário para excluir um usuário pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Excluir Apicultor", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do Apicultor:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        def realizar_exclusao():
            try:
                id_apicultor = int(id_entry.get())

                # Confirmação antes de excluir
                confirmar = messagebox.askyesno("Confirmação",
                                                f"Tem certeza de que deseja excluir o apicultor com ID {id_apicultor}?")
                if not confirmar:
                    return

                self.operacoes.excluir("apicultor", "id_apicultor", id_apicultor)
                messagebox.showinfo("Sucesso", "Apicultor excluído com sucesso!")
                self.menu_apicultores()
            except ValueError:
                messagebox.showerror("Erro", "O ID do Apicultor deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir apicultor: {e}")

        tk.Button(self.tab_control, text="Excluir", command=realizar_exclusao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apicultores).pack(pady=10)
        
    
    def cadastrar_apiario(self, nome_apiario, localizacao, tamanho, id_apicultor):
        """
        Cadastra um novo apiario no banco de dados.
        """
        if not nome_apiario or not localizacao or not tamanho or not id_apicultor:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        try:
            tamanho = int(tamanho)
            id_apicultor = int(id_apicultor)
        except ValueError:
            messagebox.showerror("Erro", "Os campos ID do apicultor e tamanho devem ser um número.")
            return

        apiario = Apiario(nome_apiario, localizacao, tamanho, id_apicultor)
        self.operacoes.inserir("apiario", ["nome_apiario", "localizacao", "tamanho","id_apicultor"], [nome_apiario, localizacao, tamanho, id_apicultor])
        messagebox.showinfo("Sucesso", "Apiario cadastrado com sucesso!")

    def buscar_apiario(self):
        """
        Abre um formulário para buscar um usuário pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Buscar Apiario", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do Apiario:").pack()
        id_apiario_entry = tk.Entry(self.tab_control)
        id_apiario_entry.pack()

        def realizar_busca():
            try:
                id_apiario = int(id_apiario_entry.get())
                apiario = self.operacoes.buscar_por_id("apiario", "id_apiario", id_apiario)
                if apiario:
                    result_text = f"Nome Apiario: {apiario['nome_apiario']}\n" \
                                  f"Localizacao: {apiario['localizacao']}\n" \
                                  f"Tamanho: {apiario['tamanho']}\n" \
                                  f"ID Apicultor: {apiario['id_apicultor']}"
                    messagebox.showinfo("Resultado da Busca", result_text)
                else:
                    messagebox.showinfo("Resultado da Busca", "Apiario não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar apiario: {e}")

        tk.Button(self.tab_control, text="Buscar", command=realizar_busca).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apiario).pack(pady=10)

    def atualizar_apiario(self):
        """
        Abre um formulário para atualizar um apicultor.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Atualizar Apiario", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do apiario:").pack()
        id_apiario_entry = tk.Entry(self.tab_control)
        id_apiario_entry.pack()

        tk.Label(self.tab_control, text="Novo Nome Apiario:").pack()
        nome_apiario_entry = tk.Entry(self.tab_control)
        nome_apiario_entry.pack()

        tk.Label(self.tab_control, text="Novo localizacao:").pack()
        localizacao_entry = tk.Entry(self.tab_control)
        localizacao_entry.pack()

        tk.Label(self.tab_control, text="Novo tamanho:").pack()
        tamanho_entry = tk.Entry(self.tab_control)
        tamanho_entry.pack()
        
        tk.Label(self.tab_control, text="Novo ID do Apicultor:").pack()
        id_apicultor_entry = tk.Entry(self.tab_control)
        id_apicultor_entry.pack()

        def realizar_atualizacao():
            try:
                id_apiario = int(id_apiario_entry.get())
                dados = {
                    "nome_apiario": nome_apiario_entry.get() or None,
                    "localizacao": localizacao_entry.get() or None,
                    "tamanho": tamanho_entry.get() or None,
                    "id_apicultor": id_apicultor_entry.get() or None,
                }

                # Remove campos vazios
                dados = {key: value for key, value in dados.items() if value is not None}

                if not dados:
                    messagebox.showwarning("Aviso", "Nenhum dado foi fornecido para atualização.")
                    return

                # Converte localizacao para inteiro se fornecido
                if "tamanho" or "id_apicultor" in dados:
                    try:
                        dados["tamanho"] = int(dados["tamanho"])
                        dados["id_apicultor"] = int(dados["id_apicultor"])
                    except ValueError:
                        messagebox.showerror("Erro", "O tamanho e o id_apicultor devem ser números.")
                        return

                self.operacoes.atualizar("apiario", "id_apiario", id_apiario, dados)
                messagebox.showinfo("Sucesso", "Apiario atualizado com sucesso!")
                self.menu_apicultores()
            except ValueError:
                messagebox.showerror("Erro", "O ID do Apiario deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar apiario: {e}")

        tk.Button(self.tab_control, text="Atualizar", command=realizar_atualizacao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apiario).pack(pady=10)

    def excluir_apiario(self):
        """
        Abre um formulário para excluir um usuário pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Excluir Apiario", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_control, text="ID do Apiario:").pack()
        id_apiario_entry = tk.Entry(self.tab_control)
        id_apiario_entry.pack()

        def realizar_exclusao():
            try:
                id_apiario = int(id_apiario_entry.get())

                # Confirmação antes de excluir
                confirmar = messagebox.askyesno("Confirmação",
                                                f"Tem certeza de que deseja excluir o apiario com ID {id_apiario}?")
                if not confirmar:
                    return

                self.operacoes.excluir("apiario", "id_apiario", id_apiario)
                messagebox.showinfo("Sucesso", "Apiario excluído com sucesso!")
                self.menu_apicultores()
            except ValueError:
                messagebox.showerror("Erro", "O ID do Apiario deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir apiario: {e}")

        tk.Button(self.tab_control, text="Excluir", command=realizar_exclusao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apiario).pack(pady=10)