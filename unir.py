import streamlit as st
import PyPDF2 

output_pdf = "doc/pdf_fin.pdf"

def unir_pdf(output_path, doc):
    pdf_fin = PyPDF2.PdfMerger()
    for document in doc:
        pdf_fin.append(document)
    pdf_fin.write(output_path)

st.image("media/unir.jpeg")
st.header("PDFUnited")
st.subheader("PDF's a unir")

pdf_sub = st.file_uploader(label = "", accept_multiple_files = True)

unir = st.button(label = "Unir PDF's")

if unir:
    if len(pdf_sub) <= 1:
        st.warning("Adjunta por lo menos dos PDF's")
    else:
        unir_pdf(output_pdf, pdf_sub)
        st.success("Click aqui paa descargar")
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()
        st.download_button(label = "Descargar PDF Unido", data = pdf_data, file_name = "PDF_fin.pdf")