
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="ModaStore PRO",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "roupas.csv"

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1445205170230-053b83016050"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_LOJA = (
    "https://images.unsplash.com/"
    "photo-1555529669-e69e7aa0ba9a"
    "?auto=format&fit=crop&w=1200&q=85"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f8f1f5 0%, #f0e1e9 50%, #e8d3df 100%);
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #321b2b, #513246);
    border-right: 2px solid #c58ca9;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #e7b9ce !important;
    letter-spacing: 1px;
}

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #351f2d !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #66495a !important;
    margin-bottom: 30px;
}

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;
    background-size: cover;
    background-position: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.18);
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        90deg,
        rgba(45,22,38,0.96) 0%,
        rgba(45,22,38,0.78) 45%,
        rgba(45,22,38,0.10) 100%
    );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;
    transform: translateY(-50%);
    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #e7a9c5 !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #f6eaf0 !important;
    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;
    margin-top: 24px;
    padding: 10px 22px;
    border-radius: 30px;
    background: #9a5578;
    color: #FFFFFF !important;
    font-size: 14px;
    font-weight: 700;
}

.info-card {
    background: #FFFFFF;
    border-radius: 22px;
    padding: 28px;
    min-height: 170px;
    border: 1px solid rgba(154,85,120,0.25);
    box-shadow: 0 10px 25px rgba(0,0,0,0.07);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;
    color: #351f2d !important;
    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;
    color: #76596a !important;
    margin-top: 5px;
}

.dark-card {
    background: linear-gradient(135deg, #321b2b, #5a344a);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.14);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #f4e7ee !important;
    line-height: 1.7;
}

[data-testid="stForm"] {
    background: rgba(255,255,255,0.88);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid #d7b4c5;
    box-shadow: 0 10px 30px rgba(0,0,0,0.07);
}

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #351f2d !important;
    opacity: 1 !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #281c23 !important;
    -webkit-text-fill-color: #281c23 !important;
    border: 2px solid #bd8fa7 !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border: 2px solid #8e486d !important;
    box-shadow: 0 0 0 3px rgba(142,72,109,0.12) !important;
}

input::placeholder,
textarea::placeholder {
    color: #806b76 !important;
    opacity: 1 !important;
}

[data-baseweb="select"] > div {
    background-color: #3c2a35 !important;
    border: 2px solid #a66d8b !important;
    border-radius: 12px !important;
}

[data-baseweb="select"] > div *,
[data-baseweb="select"] input,
[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #3c2a35 !important;
}

[role="option"] {
    background-color: #3c2a35 !important;
    color: #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #75405d !important;
    color: #FFFFFF !important;
}

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #8d4b6d, #b56f92) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 14px !important;
    min-height: 54px;
    font-family: 'Poppins', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    box-shadow: 0 8px 18px rgba(141,75,109,0.24);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background: linear-gradient(135deg, #713a57, #965978) !important;
    color: #FFFFFF !important;
    transform: translateY(-1px);
}

[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid #d7b4c5;
}

.footer {
    margin-top: 50px;
    text-align: center;
    color: #76596a !important;
    font-size: 14px;
    font-weight: 600;
}

@media (max-width: 768px) {
    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}
</style>
""", unsafe_allow_html=True)


def carregar_dados():

    colunas = [
        "Marca",
        "Produto",
        "Categoria",
        "Tamanho",
        "Cor",
        "Estoque",
        "Preco",
        "Observacoes"
    ]

    if os.path.exists(ARQUIVO):

        try:
            dados = pd.read_csv(ARQUIVO)
            return dados

        except Exception:
            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


df = carregar_dados()


colunas_necessarias = [
    "Marca",
    "Produto",
    "Categoria",
    "Tamanho",
    "Cor",
    "Estoque",
    "Preco",
    "Observacoes"
]


for coluna in colunas_necessarias:

    if coluna not in df.columns:
        df[coluna] = ""


df["Preco"] = pd.to_numeric(
    df["Preco"],
    errors="coerce"
).fillna(0)


df["Estoque"] = pd.to_numeric(
    df["Estoque"],
    errors="coerce"
).fillna(0)


st.sidebar.markdown(
"""
<div class="logo-title">
👗 ModaStore
</div>

<div class="logo-subtitle">
GESTÃO INTELIGENTE DA SUA LOJA
</div>
""",
unsafe_allow_html=True
)


st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Produto",
        "👗 Produtos Cadastrados"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "ModaStore PRO • 2026"
)


if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Sua loja.<br>
Seu estilo.
</div>

<div class="hero-text">
Organize suas roupas e produtos em um único lugar.<br>
Cadastre, consulte e acompanhe seu estoque de forma
simples, rápida e profissional.
</div>

<div class="hero-badge">
👗 GESTÃO DE MODA
</div>

</div>

</div>
""",
unsafe_allow_html=True
)


    st.markdown(
"""
<div class="page-title">
📊 Visão geral da loja
</div>

<div class="page-subtitle">
Acompanhe seus produtos, estoque e valor do catálogo.
</div>
""",
unsafe_allow_html=True
)


    total_produtos = len(df)

    estoque_total = df["Estoque"].sum()

    valor_catalogo = (
        df["Preco"] * df["Estoque"]
    ).sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
👗
</div>

<div class="card-number">
{total_produtos}
</div>

<div class="card-label">
PRODUTOS CADASTRADOS
</div>

</div>
""",
unsafe_allow_html=True
)


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
📦
</div>

<div class="card-number">
{estoque_total:,.0f}
</div>

<div class="card-label">
PEÇAS EM ESTOQUE
</div>

</div>
""",
unsafe_allow_html=True
)


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_catalogo:,.2f}
</div>

<div class="card-label">
VALOR DO ESTOQUE
</div>

</div>
""",
unsafe_allow_html=True
)


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
✨ Controle profissional
</h2>

<p>
O ModaStore PRO permite manter todos os produtos
da sua loja organizados em um único lugar.
</p>

<p>
Cadastre, consulte, pesquise e acompanhe roupas,
tamanhos, cores, preços e estoque de maneira moderna.
</p>

</div>
""",
unsafe_allow_html=True
)


    with coluna2:

        st.image(
            IMAGEM_LOJA,
            use_container_width=True
        )


elif menu == "➕ Cadastrar Produto":

    st.markdown(
"""
<div class="page-title">
➕ Novo produto
</div>

<div class="page-subtitle">
Adicione uma nova peça ao catálogo da sua loja.
</div>
""",
unsafe_allow_html=True
)


    with st.form(
        "cadastro_produto",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            marca = st.text_input(
                "🏷️ Marca"
            )

            produto = st.text_input(
                "👗 Produto"
            )

            categoria = st.selectbox(
                "📂 Categoria",
                [
                    "Camiseta",
                    "Blusa",
                    "Calça",
                    "Vestido",
                    "Saia",
                    "Shorts",
                    "Jaqueta",
                    "Moletom",
                    "Conjunto",
                    "Outro"
                ]
            )

            tamanho = st.selectbox(
                "📏 Tamanho",
                [
                    "PP",
                    "P",
                    "M",
                    "G",
                    "GG",
                    "XG",
                    "Único"
                ]
            )


        with col2:

            cor = st.selectbox(
                "🎨 Cor",
                [
                    "Preto",
                    "Branco",
                    "Rosa",
                    "Vermelho",
                    "Azul",
                    "Verde",
                    "Bege",
                    "Marrom",
                    "Cinza",
                    "Amarelo",
                    "Outra"
                ]
            )

            estoque = st.number_input(
                "📦 Quantidade em estoque",
                min_value=0,
                value=0,
                step=1
            )

            preco = st.number_input(
                "💰 Preço da peça",
                min_value=0.0,
                value=0.0,
                step=5.0
            )

            observacoes = st.text_area(
                "📝 Observações"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR PRODUTO"
        )


    if cadastrar:

        if (
            marca.strip()
            and produto.strip()
        ):

            novo_produto = pd.DataFrame(
                [{
                    "Marca": marca.strip(),
                    "Produto": produto.strip(),
                    "Categoria": categoria,
                    "Tamanho": tamanho,
                    "Cor": cor,
                    "Estoque": int(estoque),
                    "Preco": float(preco),
                    "Observacoes": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_produto
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "👗 Produto cadastrado com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha Marca e Produto."
            )


elif menu == "👗 Produtos Cadastrados":

    st.markdown(
"""
<div class="page-title">
👗 Meu catálogo
</div>

<div class="page-subtitle">
Consulte e pesquise todos os produtos cadastrados.
</div>
""",
unsafe_allow_html=True
)


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
👗 Nenhum produto cadastrado
</h2>

<p>
Seu catálogo ainda está vazio.
Cadastre sua primeira peça para começar.
</p>

</div>
""",
unsafe_allow_html=True
)


    else:

        busca = st.text_input(
            "🔎 Pesquisar produto",
            placeholder="Digite marca, produto, categoria, tamanho ou cor..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False,
                        regex=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        opcoes_produtos = df.index.tolist()


        produto_excluir = st.selectbox(
            "🗑️ Selecione um produto para excluir",
            options=opcoes_produtos,
            format_func=lambda indice:
                f"{df.loc[indice, 'Marca']} "
                f"{df.loc[indice, 'Produto']} - "
                f"{df.loc[indice, 'Tamanho']}"
        )


        if st.button(
            "🗑️ EXCLUIR PRODUTO"
        ):

            df = df.drop(
                produto_excluir
            )


            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "👗 Produto excluído com sucesso!"
            )


            st.rerun()


st.markdown(
"""
<div class="footer">

👗 ModaStore PRO<br>
Gestão inteligente para lojas de roupa

</div>
""",
unsafe_allow_html=True
)
