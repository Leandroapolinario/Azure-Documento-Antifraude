import streamlit as st

def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    fileName = uploaded_file.name
    #Enviar para o blob storage
    blob_url = ""
    if blob_url
    st.write("Arquivo {fileName} enviado com sucesso!")
    credit_card_info = "" #Chamar a função de detecção de cartão de crédito
    else:
        st.write("Erro ao enviar o arquivo {fileName}")
        st.write("Por favor, tente novamente.")
        st.write("Se o erro persistir, entre em contato com o suporte.")

def show_image_and_validation(blob_url, credit_card_info)
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da validação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style= 'color: green;'>Cartão de crédito válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do cartão: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
        




        if __name__ == "__main__":
        configure_interface()