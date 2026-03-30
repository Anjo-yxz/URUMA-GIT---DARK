import os
from pathlib import Path
from playwright.sync_api import Playwright, sync_playwright

ROOT = Path(__file__).resolve().parents[2]

class UrumaBot:
    def __init__(self):
        self.comandoGit = ""  
        self.user = ""

    def PalavraGit(self):
        self.listPass = [
            'DB_NAME','SECRET_KEY','GITHUB_TOKEN',
            'MONGODB_PASSWORD','MONGODB_URI','EMAIL_PASS'
        ]

        while True:
            print('Você Quer Usar As Variáveis Disponíveis Ou Digitar A Sua? (s/n)'.title())
            comandoVariavel = input('Digita: ').lower()

            if comandoVariavel in ['s', 'sim']:
                print(self.listPass)
                variavelDisponivel = input('Qual Variável Quer Usar: ').upper()

                if variavelDisponivel not in self.listPass:
                    print('Variável inválida.')
                    continue

                self.variavelNome = variavelDisponivel

            elif comandoVariavel in ['n', 'não', 'nao']:
                propiaVariavel = input("[+] Escreva sua própria variável: ").upper().strip()

                if not propiaVariavel:
                    print('Nome inválido.')
                    continue

                self.variavelNome = propiaVariavel

            else:
                print('Opção inválida.')
                continue

            valor = input('[+] Escreva 2/4 letras: ').strip().lower()

            if 1 < len(valor) <= 4:
                self.comandoGit = valor
                os.system('cls')
                return
            else:
                print('Digite 2 a 4 letras. Exemplo: ju, jilu, jol')

    def User(self):
        candidate_paths = [
            ROOT / "UserGit.txt",
            ROOT / "src" / "Token" / "UserGit.txt",
        ]

        for path in candidate_paths:
            if path.exists():
                self.user = path.read_text(encoding="utf-8").strip()
                return

        raise FileNotFoundError(
            f"Arquivo UserGit.txt não encontrado. Verifique: {candidate_paths}"
        )

    @staticmethod
    def add_cookies(context, cookie_value: str):
        cookies = []

        for item in cookie_value.split("; "):
            if "=" in item:
                name, value = item.split("=", 1)
                cookies.append({
                    "name": name,
                    "value": value,
                    "url": "https://github.com",
                })

        if cookies:
            context.add_cookies(cookies)

    def __bot(self, comandoGit: str, playwright: Playwright):
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://github.com")
        self.add_cookies(context, self.user)
        page.reload()

        page.locator('xpath=/html/body/div[1]/div[2]/react-partial[2]/div/header/div/div[2]/div[1]/div[1]/button').click()
        page.locator('xpath=/html/body/div[1]/div[2]/react-partial[2]/div/header/div/div[2]/div[3]/qbsearch-input/div[1]/div/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]/input').fill(f'"{self.variavelNome}={comandoGit}"')
        page.keyboard.press('Enter')
        page.locator('xpath=/html/body/div[1]/div[6]/main/react-app/div/div/div[1]/div/div/div[1]/div[2]/div/div/div/div/ul/li[1]/ul/li[1]/a').click()

        n = 1
        output_file = ROOT / "src" / "Database" / "UrumaGITHUB.txt"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        while True:
            try:
                n += 1
                tt = page.locator(f'xpath=/html/body/div[1]/div[6]/main/react-app/div/div/div[1]/div/div/div[2]/div/div/div/div[4]/div/div/div[{n}]/div[2]').inner_text()

                with open(output_file, "a", encoding="utf-8") as arquivo:
                    arquivo.write('URUMA:\n' + tt + "\n\n\n\n\nURUMA BOT\n")
            except Exception:
                break

        browser.close()

    def execute(self):
        self.PalavraGit()
        self.User()
        with sync_playwright() as p:
            self.__bot(self.comandoGit, p)


if __name__ == "__main__":
    UrumaBot().execute()