from page_objects.objetosgerais import ObjetosGerais


class DemoQA(ObjetosGerais):

    def acessar_demoqa(self):
        self.page.goto(
            'http://demoqa.com/elements')
        self.page.wait_for_load_state()

    def acessar_text_box(self):
        self.botao_text_box.click()
        self.page.wait_for_load_state()

    def acessar_web_tables(self):
        self.botao_web_tables.click()
        self.page.wait_for_load_state()

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.botao_text_box = page.get_by_text("Text Box")
        self.botao_web_tables = page.get_by_text("Web Tables")


class TextBox(DemoQA):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.campo_nome = page.locator('#userName')
        self.campo_email = page.locator('#userEmail')
        self.campo_endereco_atual = page.locator('#currentAddress')
        self.campo_endereco_permanente = page.locator('#permanentAddress')

    def preencher_text_box(self,
                           nome='',
                           email='',
                           endereco_atual='',
                           endereco_permanente=''):
        if nome:
            self.campo_nome.fill(nome)
            self.campo_nome.press('Tab')
        if email:
            self.campo_email.fill(email)
            self.campo_email.press('Tab')
        if endereco_atual:
            self.campo_endereco_atual.fill(endereco_atual)
            self.campo_endereco_atual.press('Tab')
        if endereco_permanente:
            self.campo_endereco_permanente.fill(endereco_permanente)
            self.campo_endereco_permanente.press('Tab')


class WebTables(DemoQA):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.campo_nome = page.locator('#firstName')
        self.campo_sobrenome = page.locator('#lastName')
        self.campo_email = page.locator('#userEmail')
        self.campo_idade = page.locator('#age')
        self.campo_salario = page.locator('#salary')
        self.campo_departamento = page.locator('#department')
        self.campo_buscar = page.locator('#searchBox')
        self.botao_editar = page.locator("#edit-record-4 > svg")
        self.botao_delete = page.locator("#delete-record-4 > svg")

    def preencher_web_tables(self,
                             nome='',
                             sobrenome='',
                             email='',
                             idade='',
                             salario='',
                             departamento=''):

        if nome:
            self.campo_nome.fill(nome)
        if sobrenome:
            self.campo_sobrenome.fill(sobrenome)
        if email:
            self.campo_email.fill(email)
        if idade:
            self.campo_idade.fill(idade)
        if salario:
            self.campo_salario.fill(salario)
        if departamento:
            self.campo_departamento.fill(departamento)

    def filtrar_web_tables(self,buscar=''):

        if buscar:
            self.campo_buscar.fill(buscar)
            self.campo_buscar.press('Tab')




