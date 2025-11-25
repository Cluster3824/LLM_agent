import gradio as gr
from resume_analyzer import ResumeAnalyzer

def analyze_multiple_resumes(files, job_title):
    """Analyze multiple resumes via Gradio interface"""
    if not files:
        return "No files uploaded."
    if not job_title.strip():
        return "Please enter a job title."
    
    analyzer = ResumeAnalyzer()
    results = []
    
    for i, file in enumerate(files, 1):
        try:
            if file.name.lower().endswith('.pdf'):
                text = analyzer.extract_text_from_pdf(file)
            elif file.name.lower().endswith('.csv'):
                text = analyzer.extract_text_from_csv(file.name)
            else:
                results.append(f"Resume {i}: Unsupported file type")
                continue
            
            analysis = analyzer.analyze_resume(text, job_title)
            results.append(f"Resume {i} ({file.name}):\n{analysis}")
        except Exception as e:
            results.append(f"Resume {i}: Error - {str(e)}")
    
    return "\n\n" + "-"*50 + "\n\n".join(results)

def create_interface():
    """Create and return Gradio interface"""
    with gr.Blocks(title="Resume Analyzer") as app:
        gr.Markdown("# Multi-Resume Analyzer")
        gr.Markdown("Upload multiple resumes and get AI-powered analysis for a specific job title.")
        
        job_title = gr.Textbox(label="Job Title", placeholder="Enter job title")
        files = gr.File(label="Upload Resumes", file_count="multiple", file_types=[".pdf", ".csv"])
        
        analyze_btn = gr.Button("Analyze Resumes", variant="primary")
        output = gr.Textbox(label="Analysis Results", lines=10, max_lines=20)
        
        analyze_btn.click(analyze_multiple_resumes, inputs=[files, job_title], outputs=output)
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch()