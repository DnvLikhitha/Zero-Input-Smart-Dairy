from fpdf import FPDF
import unicodedata

def remove_non_latin1(text):
    return unicodedata.normalize('NFKD', text).encode('latin1', 'ignore').decode('latin1')
def export_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    text = remove_non_latin1(text)
    for line in text.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)
    # Return PDF as bytes
    return pdf.output(dest='S').encode('latin1')