import PyPDF2
import ollama
import pandas as pd
from typing import Union, List
import os

class ResumeAnalyzer:
    def __init__(self, model: str = "llama3.2:1b"):
        self.model = model
    
    def extract_text_from_pdf(self, pdf_file) -> str:
        """Extract text from PDF file"""
        reader = PyPDF2.PdfReader(pdf_file)
        pdf_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_text += text + "\n"
        return pdf_text
    
    def extract_text_from_csv(self, csv_file: str) -> str:
        """Extract text from CSV file"""
        df = pd.read_csv(csv_file)
        return df.to_string(index=False)
    
    def analyze_resume(self, text: str, job_title: str) -> str:
        """Analyze resume text against job title"""
        message = {
            "role": "user",
            "content": (
                f"Analyze this resume for '{job_title}' job. Give score 0-100 and 2-line explanation only.\n"
                "Format: Score: X/100\nReason: (max 2 lines)\n\n"
                f"Resume:\n{text[:2000]}..."
            ),
        }
        
        payload = {
            "model": self.model,
            "messages": [message],
            "stream": False,
        }
        
        response = ollama.chat(**payload)
        return response["message"]["content"]
    
    def process_file(self, filename: str, job_title: str) -> str:
        """Process a single resume file"""
        if not os.path.exists(filename):
            return f"File {filename} not found."
        
        try:
            if filename.lower().endswith('.pdf'):
                with open(filename, "rb") as f:
                    text = self.extract_text_from_pdf(f)
            elif filename.lower().endswith('.csv'):
                text = self.extract_text_from_csv(filename)
            else:
                return "Unsupported file type. Please use PDF or CSV files."
            
            return self.analyze_resume(text, job_title)
        except Exception as e:
            return f"Error processing {filename}: {str(e)}"
    
    def process_multiple_files(self, files: List[str], job_title: str) -> List[dict]:
        """Process multiple resume files"""
        results = []
        for i, filename in enumerate(files, 1):
            result = self.process_file(filename, job_title)
            results.append({
                'file': filename,
                'analysis': result,
                'index': i
            })
        return results

def main():
    """Command line interface"""
    analyzer = ResumeAnalyzer()
    
    try:
        n = int(input("Enter the number of resumes: "))
        if n <= 0:
            print("Invalid number of files.")
            return
        
        for i in range(n):
            filename = input(f"Enter resume file {i+1} path: ")
            job_title = input(f"Enter job title for resume {i+1}: ")
            
            result = analyzer.process_file(filename, job_title)
            print(f"\nAnalysis for {filename} (Job: {job_title}):")
            print(result)
            print("-" * 50)
            
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()