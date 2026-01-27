from page_objects.objetosgerais import ObjetosGerais
from playwright.sync_api import expect


class SwagLabs(ObjetosGerais):

    def acessar_swag_labs(self):
        self.page.goto(
            'https://www.saucedemo.com/')
        self.page.wait_for_load_state()

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.campo_username = page.locator('#user-name')
        self.campo_password = page.locator('#password')
        self.item_produto_name = page.locator(".inventory_item_name")
        self.botao_checkout = page.locator('#checkout')
        self.campo_nome = page.locator('#first-name')
        self.campo_sobrenome = page.locator('#last-name')
        self.campo_codigo_postal = page.locator('#postal-code')

    def criar_login(self,
                    username,
                    password):
        if username:
            self.campo_username.fill(username)
            self.campo_password.press('Tab')

        if password:
            self.campo_password.fill(password)
            self.campo_password.press('Tab')

        self.botao_login.click()
        self.page.wait_for_load_state(timeout=5000)

    def comprar_item(self,
                     lista_itens):
        for nome in lista_itens:
            self.item_produto_name.filter(has_text=nome).click()
            self.botao_add_to_cart.click()
            expect(self.page.get_by_text('Remove')).to_be_visible(timeout=5000)
            self.botao_voltar.click()
            self.page.wait_for_timeout(5000)

    def conferir_carrinho_compras(self):
        self.botao_carrinho_compras.click()
        self.page.wait_for_load_state(timeout=5000)

    def checkuot(self, nome='', sobrenome='', codigo_postal=''):
        self.botao_checkout.click()
        self.page.wait_for_timeout(2000)
        if nome:
            self.campo_nome.fill(nome)
        if sobrenome:
            self.campo_sobrenome.fill(sobrenome)
        if codigo_postal:
            self.campo_codigo_postal.fill(codigo_postal)
        self.botao_continue.click()
        self.page.wait_for_timeout(2000)

    def finalizar_carrinho_compras(self):
        self.botao_finish.click()
        expect(self.page.get_by_text(
            'Thank you for your order! Your order has been dispatched, and will arrive just as fast as the pony can get there!'))
        self.botao_back_home.click()



