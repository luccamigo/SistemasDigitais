from lexer import *
from parser_1 import *
from vasco2 import *


def main():
    global CoordUltimaVar
    winPrincipal = ...
    while True:
        try:
            data = input("Digite uma expressão logica (ou 'exit' para sair): ")
        except EOFError:
            break
        if winPrincipal != ...:
            ClearWindow(winPrincipal)
            winPrincipal.close()

        ClearWindow(win)

        if data.lower() == 'exit':
            win.close()
            break

        # Executar o analisador léxico
        lexer.input(data)
        '''
        for token in lexer:
            print(token)
        '''
        # Executar o analisador sintático
        result = parser.parse(data)
        print("Resultado:", result)
        print(CoordUltimaVar.getY())
        print(result.getX())
        winPrincipal = GraphWin("vasco2", result.getX(), CoordUltimaVar.getY())
        TransferItemFromWinToWin(win, winPrincipal)
        ResetCoordUltimaVar()
        print(CoordUltimaVar.getY())

if __name__ == "__main__":
    main()

#python D:\compiladores\main.py










