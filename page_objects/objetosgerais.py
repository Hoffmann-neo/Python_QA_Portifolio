from playwright.sync_api import expect
import re


class ObjetosGerais:

    def __init__(self, page):
        self.page = page
        self.botao_submit = page.locator('#submit')
        self.botao_login = page.locator('#login-button')
        self.botao_add_to_cart = page.locator('#add-to-cart')
        self.botao_voltar = page.locator('#back-to-products')
        self.botao_carrinho_compras = page.locator('#shopping_cart_container')
        self.botao_back_home = page.locator('#back-to-products')
        self.botao_continue = page.locator('#continue')
        self.botao_finish = page.locator('#finish')

    def validar_grid(
            self,
            grid_locator: str,
            esperado,
            timeout: int = 30000,
            normalizar: bool = True,
            parcial: bool = True
    ):
        """
        Valida textos dentro de qualquer container.

        Funciona para:
        - grids
        - listas
        - outputs
        - carrinhos
        - resumos
        - formulários

        esperado pode ser:
        - list  -> ["Texto A", "Texto B"]
        - dict  -> {"campo": "valor"}
        - str   -> "Texto único"
        """

        # -------------------------
        # Normalização
        # -------------------------
        def limpar(texto: str) -> str:

            if not normalizar:
                return texto.strip()

            texto = texto.lower()

            texto = re.sub(r"\s+", " ", texto)

            texto = re.sub(r"[^\w\sáéíóúâêôãõç]", "", texto)

            return texto.strip()

        # -------------------------
        # Localiza container
        # -------------------------
        container = self.page.locator(grid_locator)

        expect(container).to_be_visible(timeout=timeout)

        elementos = container.locator("*")

        expect(elementos.first).to_be_visible(timeout=timeout)

        textos_tela = []

        total = elementos.count()

        for i in range(total):

            texto = elementos.nth(i).inner_text(timeout=timeout).strip()

            if texto:
                textos_tela.append(limpar(texto))

        # Junta tudo também
        texto_completo = " ".join(textos_tela)

        # -------------------------
        # Debug
        # -------------------------
        print("\n📌 Textos encontrados:")
        for t in textos_tela:
            print("-", t)

        # -------------------------
        # Prepara esperado
        # -------------------------
        esperados = []

        if isinstance(esperado, str):
            esperados = [esperado]

        elif isinstance(esperado, list):
            esperados = esperado

        elif isinstance(esperado, dict):
            esperados = list(esperado.values())

        else:
            raise TypeError("esperado deve ser str, list ou dict")

        esperados = [limpar(e) for e in esperados]

        # -------------------------
        # Validação
        # -------------------------
        erros = []

        for valor in esperados:

            if parcial:
                encontrado = valor in texto_completo
            else:
                encontrado = valor in textos_tela

            if not encontrado:
                erros.append(f"❌ Não encontrado: {valor}")

        # -------------------------
        # Resultado
        # -------------------------
        if erros:
            raise AssertionError(
                "\n\n".join(erros)
                + "\n\n📌 Texto da tela:\n"
                + texto_completo
            )

        print("\n✅ Validação concluída com sucesso")


