import PyPDF2
import docx
import re

# ----------- PDF RESUME TEXT EXTRACTION -----------
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
    except Exception as e:
        print("Error reading PDF:", e)
    return text


# ----------- DOCX RESUME TEXT EXTRACTION -----------
def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + " "
    except Exception as e:
        print("Error reading DOCX:", e)
    return text


# ----------- CLEAN TEXT FOR NLP -----------
def clean_text(text):
    text = text.lower()                      # convert to lowercase
    text = re.sub(r'[^a-z\s]', ' ', text)    # remove numbers & symbols
    text = re.sub(r'\s+', ' ', text)         # remove extra spaces
    return text.strip()


# ----------- MAIN RESUME PARSER FUNCTION -----------
def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        raw_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        raw_text = extract_text_from_docx(file_path)
    else:
        return ""

    return clean_text(raw_text)
