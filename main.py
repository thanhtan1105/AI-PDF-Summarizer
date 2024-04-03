from function.pdf import Pdf
from function.ai_summary import AISummary

def custom_print(summary):
    return summary.replace("<n>", "\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pdf_provider = Pdf()
    ai_summary_service = AISummary()

    resume_summaries = []  # To store the generated summaries
    list_file_name = pdf_provider.get_pdf_files()
    for directory_file in list_file_name:
        text = pdf_provider.get_summary(directory_file)
        encoded_text = ai_summary_service.encode_text(text)
        generated_summary = ai_summary_service.generate_summary(encoded_text)
        decoded_summary = ai_summary_service.decode_summary(generated_summary)
        resume_summaries.append(decoded_summary)

    # Print the generated summaries for each resume
    for i, summary in enumerate(resume_summaries):
        print(f"Summary for Resume {i + 1}:")
        print(custom_print(summary))
        print()