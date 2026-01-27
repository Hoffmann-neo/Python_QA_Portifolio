from pages.swaglbs import SwagLabs

def test_login(page):
    """
    - Acessar site: saucedemo
    - Efetuar login
        - username='standard_user',
        - password='secret_sauce'
    - Adicionar os produtos ao carrinho de compras
        "Sauce Labs Fleece Jacket",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bolt T-Shirt"
    - Etapas
        - Clicar no nome do produto
        - clicar botao add to cart
        - clicar em voltar
    - depois de adicionar todos produtos no carrinho
    - clicar no carrinho
    - validar grid
    - clicar em checkout
    - preencher informações
        - nome='Fulano',
        - sobrenome='de santas',
        - codigo_postal='92998789'
    - clicar botao continue
    - validar grid de valores
    - clicar em finish
    - validar expect
    - clicar em back home
    """
    login = SwagLabs(page)
    login.acessar_swag_labs()
    login.criar_login(
        username='standard_user',
        password='secret_sauce',
    )
    meus_produtos = [
        "Sauce Labs Fleece Jacket",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bolt T-Shirt"
    ]
    compra = SwagLabs(page)
    compra.comprar_item(
        lista_itens=meus_produtos
    )
    compra.conferir_carrinho_compras()

    compra.validar_grid(
        grid_locator='#cart_contents_container',
        esperado=['qtydescription 1 sauce labs fleece jacket its not every day that you come across a midweight quarterzip '
                  'fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office 4999 remove '
                  '1 testallthethings tshirt red this classic sauce labs tshirt is perfect to wear when cozying up to your '
                  'keyboard to automate a few tests supersoft and comfy ringspun combed cotton 1599 remove 1 sauce labs bolt '
                  'tshirt get your testing superhero on with the sauce labs bolt tshirt from american apparel 100 ringspun '
                  'combed cotton heather gray with red bolt 1599 remove continue shopping checkout qtydescription 1 sauce '
                  'labs fleece jacket its not every day that you come across a midweight quarterzip fleece jacket capable '
                  'of handling everything from a relaxing day outdoors to a busy day at the office 4999 remove 1 testallthethings '
                  'tshirt red this classic sauce labs tshirt is perfect to wear when cozying up to your keyboard to automate a '
                  'few tests supersoft and comfy ringspun combed cotton 1599 remove 1 sauce labs bolt tshirt get your testing '
                  'superhero on with the sauce labs bolt tshirt from american apparel 100 ringspun combed cotton heather gray '
                  'with red bolt 1599 remove qty description 1 sauce labs fleece jacket its not every day that you come across '
                  'a midweight quarterzip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day '
                  'at the office 4999 remove 1 sauce labs fleece jacket its not every day that you come across a midweight quarterzip '
                  'fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office 4999 remove '
                  'sauce labs fleece jacket sauce labs fleece jacket its not every day that you come across a midweight quarterzip fleece '
                  'jacket capable of handling everything from a relaxing day outdoors to a busy day at the office 4999 remove 4999 remove 1'
                  ' testallthethings tshirt red this classic sauce labs tshirt is perfect to wear when cozying up to your keyboard to automate a '
                  'few tests supersoft and comfy ringspun combed cotton 1599 remove 1 testallthethings tshirt red this classic sauce labs tshirt is '
                  'perfect to wear when cozying up to your keyboard to automate a few tests supersoft and comfy ringspun combed cotton 1599 remove '
                  'testallthethings tshirt red testallthethings tshirt red this classic sauce labs tshirt is perfect to wear when cozying up to your '
                  'keyboard to automate a few tests supersoft and comfy ringspun combed cotton 1599 remove 1599 remove 1 sauce labs bolt tshirt get your '
                  'testing superhero on with the sauce labs bolt tshirt from american apparel 100 ringspun combed cotton heather gray with red bolt 1599 '
                  'remove 1 sauce labs bolt tshirt get your testing superhero on with the sauce labs bolt tshirt from american apparel 100 ringspun combed '
                  'cotton heather gray with red bolt 1599 remove sauce labs bolt tshirt sauce labs bolt tshirt get your testing superhero on with the sauce '
                  'labs bolt tshirt from american apparel 100 ringspun combed cotton heather g'
                  'ray with red bolt 1599 remove 1599 remove continue shopping checkout continue shopping checkout']
    )

    compra.checkuot(
        nome='Fulano',
        sobrenome='de santas',
        codigo_postal='92998789'
    )

    compra.validar_grid(
        grid_locator='#checkout_summary_container .summary_info',
        esperado=['payment information saucecard 31337 shipping information free pony express delivery price total item '
                  'total 8197 tax 656 total 8853 cancel finish cancel finish']
    )
    compra.finalizar_carrinho_compras()