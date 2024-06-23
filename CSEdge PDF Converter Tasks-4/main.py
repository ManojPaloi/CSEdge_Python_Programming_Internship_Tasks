import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from pdfminer.high_level import extract_text
from pdf2image import convert_from_path
from docx import Document
import os

class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Converter")
        self.root.geometry("600x400")
        self.root.configure(bg='#34495e')

        # Define style
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12, "bold"), background='#34495e', foreground='#ecf0f1')
        style.configure("TButton", font=("Helvetica", 12, "bold"), background='#1abc9c', foreground='green', padding=10)
        style.map("TButton", background=[('active', '#16a085')], foreground=[('active', 'black')])
        style.configure("TEntry", font=("Helvetica", 12))

        # Widgets
        self.create_widgets()

        # Copyright Label
        self.create_footer()

    def create_widgets(self):
        """Create and place widgets in the window."""
        self.pdf_label = ttk.Label(self.root, text="Select PDF file:")
        self.pdf_label.pack(pady=10)
        
        self.pdf_path_frame = ttk.Frame(self.root)
        self.pdf_path_frame.pack(pady=5)
        
        self.pdf_path_entry = ttk.Entry(self.pdf_path_frame, width=40)
        self.pdf_path_entry.grid(row=0, column=0, padx=5)
        
        self.browse_button = ttk.Button(self.pdf_path_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=1, padx=5)
        
        self.convert_text_button = ttk.Button(self.root, text="Convert to Text", command=self.convert_to_text)
        self.convert_text_button.pack(pady=10)
        
        self.convert_images_button = ttk.Button(self.root, text="Convert to Images", command=self.convert_to_images)
        self.convert_images_button.pack(pady=10)
        
        self.convert_docx_button = ttk.Button(self.root, text="Convert to DOCX", command=self.convert_to_docx)
        self.convert_docx_button.pack(pady=10)

        self.status_label = ttk.Label(self.root, text="", font=("Helvetica", 10, "italic"), background='#34495e', foreground='#ecf0f1')
        self.status_label.pack(pady=20)

    def create_footer(self):
        """Create and place the footer in the window."""
        self.footer_label = ttk.Label(self.root, text="© 2024 Manoj Paloi", font=("Helvetica", 10, "italic"), background='#34495e', foreground='#ecf0f1')
        self.footer_label.pack(side=tk.BOTTOM, pady=10)
    
    def browse_file(self):
        """Open a file dialog to select a PDF file."""
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_path_entry.delete(0, tk.END)
            self.pdf_path_entry.insert(0, file_path)
    
    def update_status(self, message, success=True):
        """Update the status label with a message."""
        self.status_label.config(text=message, foreground='green' if success else 'red')
    
    def convert_to_text(self):
        """Convert the selected PDF file to a text file."""
        pdf_path = self.pdf_path_entry.get()
        if not pdf_path:
            messagebox.showerror("Error", "Please select a PDF file")
            return
        
        try:
            text = extract_text(pdf_path)
            text_path = os.path.splitext(pdf_path)[0] + ".txt"
            with open(text_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)
            messagebox.showinfo("Success", f"Text saved to {text_path}")
            self.update_status(f"Text saved to {text_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.update_status(f"Error: {str(e)}", success=False)
    
    def convert_to_images(self):
        """Convert the selected PDF file to image files."""
        pdf_path = self.pdf_path_entry.get()
        if not pdf_path:
            messagebox.showerror("Error", "Please select a PDF file")
            return
        
        try:
            output_folder = os.path.splitext(pdf_path)[0] + "_images"
            os.makedirs(output_folder, exist_ok=True)
            images = convert_from_path(pdf_path)
            image_paths = []
            for i, img in enumerate(images):
                img_path = f"{output_folder}/page_{i + 1}.png"
                img.save(img_path, "PNG")
                image_paths.append(img_path)
            messagebox.showinfo("Success", f"Images saved to {output_folder}")
            self.update_status(f"Images saved to {output_folder}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.update_status(f"Error: {str(e)}", success=False)
    
    def convert_to_docx(self):
        """Convert the selected PDF file to a DOCX file."""
        pdf_path = self.pdf_path_entry.get()
        if not pdf_path:
            messagebox.showerror("Error", "Please select a PDF file")
            return
        
        try:
            text = extract_text(pdf_path)
            docx_path = os.path.splitext(pdf_path)[0] + ".docx"
            doc = Document()
            doc.add_paragraph(text)
            doc.save(docx_path)
            messagebox.showinfo("Success", f"DOCX saved to {docx_path}")
            self.update_status(f"DOCX saved to {docx_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.update_status(f"Error: {str(e)}", success=False)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()
