from pdfminer.high_level import extract_text

def get_pdf_text(pdf_path):
    text = extract_text(pdf_path)
    print(text)
    return {"text": text.strip()}

def compare_pdfs(template_pdf, test_pdf):
    template_data = get_pdf_text(template_pdf)
    test_data = get_pdf_text(test_pdf)

    if template_data["text"] == test_data["text"]:
        print("PDF полностью совпадает!")
        return True
    else:
        print("PDF отличается!")
        return False