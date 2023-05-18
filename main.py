import PyPDF2

def convert_file(file_path, output_format):
    # Открываем файл
    with open(file_path, 'rb') as file:
        # Создаем объект для чтения PDF
        pdf_reader = PyPDF2.PdfFileReader(file)

        # Создаем объект для записи в новый файл
        with open(f'{file_path[:-4]}.{output_format}', 'wb') as output_file:
            # Создаем объект для записи PDF в другой формат
            if output_format == 'txt':
                pdf_writer = PyPDF2.TxtConverter(pdf_reader, output_file)
            elif output_format == 'docx':
                pdf_writer = PyPDF2.DocxConverter(pdf_reader, output_file)
            elif output_format == 'html':
                pdf_writer = PyPDF2.HtmlConverter(pdf_reader, output_file)
            else:
                print('Неподдерживаемый формат')
                return

            # Конвертируем PDF в другой формат
            pdf_writer.write()

            print(f'Файл успешно конвертирован в формат {output_format}')

# Пример использования
convert_file('example.pdf', 'txt')