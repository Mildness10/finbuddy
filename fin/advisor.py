import PyPDF2
from langchain_openai import ChatOpenAI
import os
import glob
from dotenv import load_dotenv
import warnings 
warnings.filterwarnings("ignore")

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        return text

pdf_directory = 'C:/Users/user/Documents/FinBud/finbuddy/static'

pdf_files = glob.glob(os.path.join(pdf_directory, '*.pdf'))

pdf_file_names = [os.path.basename(pdf_file) for pdf_file in pdf_files]

pdf_texts = [extract_text_from_pdf(pdf_path) for pdf_path in pdf_file_names]

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def get_advisor_response(user_input):
    prompt = f"{user_input}"
    response = llm.invoke(f'{prompt}, {pdf_texts}')
    output_text = response.content

    return output_text
