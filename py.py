class JogoDaVelha:
    def __init__(self):
        # Inicializa o tabuleiro 3x3 com espaços vazios
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.turno = 'X'

    def exibir_tabuleiro(self):
        print("\n  0 1 2")
        for i, linha in enumerate(self.tabuleiro):
            print(f"{i} {'|'.join(linha)}")
            if i < 2:
                print("  -----")

    def realizar_jogada(self, linha, coluna):
        # Validação de regras de negócio
        if 0 <= linha <= 2 and 0 <= coluna <= 2 and self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = self.turno
            return True
        return False

    def verificar_vitoria(self):
        # 1. Verificar Linhas e Colunas
        for i in range(3):
            if all(self.tabuleiro[i][j] == self.turno for j in range(3)): return True
            if all(self.tabuleiro[j][i] == self.turno for j in range(3)): return True
        
        # 2. Verificar Diagonais
        if all(self.tabuleiro[i][i] == self.turno for i in range(3)): return True
        if all(self.tabuleiro[i][2-i] == self.turno for i in range(3)): return True
        
        return False

    def tabuleiro_cheio(self):
        return all(celula != ' ' for linha in self.tabuleiro for celula in linha)

    def trocar_turno(self):
        self.turno = 'O' if self.turno == 'X' else 'X'

# --- Fluxo de Execução (Main) ---
if __name__ == "__main__":
    jogo = JogoDaVelha()
    print("--- ENGENHARIA DE SOFTWARE: LÓGICA DO JOGO ---")

    while True:
        jogo.exibir_tabuleiro()
        try:
            l = int(input(f"\nJogador {jogo.turno}, escolha a LINHA (0-2): "))
            c = int(input(f"Jogador {jogo.turno}, escolha a COLUNA (0-2): "))
            
            if jogo.realizar_jogada(l, c):
                if jogo.verificar_vitoria():
                    jogo.exibir_tabuleiro()
                    print(f"\n🏆 PARABÉNS! O Jogador {jogo.turno} venceu!")
                    break
                if jogo.tabuleiro_cheio():
                    jogo.exibir_tabuleiro()
                    print("\n🤝 EMPATE! O jogo deu 'Velha'.")
                    break
                jogo.trocar_turno()
            else:
                print("\n⚠️ Jogada inválida! Tente novamente.")
        except ValueError:
            print("\n❌ Erro: Digite apenas números inteiros!")