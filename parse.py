from docx import Document
import csv

def read_docx_table(file_path):
    document = Document(file_path)

    # print(len(document.tables)) # DEBUG

    # table = document.tables[1]  # Assuming the first table in the document

    finalCSV = []

    tempRowOfCSV = []
    csvRowCounter = -1 # Because the first table is a index

    for table in document.tables:
        
        # print("|||||||||| NEW TABLE |||||||||||||||||||| NEW TABLE |||||||||||||||||||||| NEW TABLE |||||||||||") # DEBUG

        for row in table.rows:
            row_data = []
            for cell in row.cells:
                row_data.append(cell.text)

            # print(row_data) # DEBUG

            if row_data[0] == "Document Information:": # ['Document Information:', 'Supreme Court of Alabama. January 11, 1910 164 Ala. 111 51 So. 424\nExtracted from page: 1\n']
                tempRowOfCSV = []
                # Document Information
                if row_data[1]:
                    tempRowOfCSV.append(row_data[1])

            if row_data[0] == "WestCheck Information:": # ['WestCheck Information:', 'Birmingham Ry., Light & Power Co. v. Moseley, 164 Ala. 111, 51 So. 424 (Ala. Jan. 11, 1910)\n']
                # WestCheck Information
                if row_data[1]:
                    tempRowOfCSV.append(row_data[1])

            # ['Treatment', 'Title', 'Date', 'Type', 'Depth', 'Headnote(s)']
            # Treatment - Overruled by
            if row_data[0] == "Overruled by": # ['Criticized in', ' 1.  Bradley v. Deaton  \n94 So. 767 , 208 Ala. 582 , Ala. , (NO. 6 DIV. 460 )\n', 'Dec. 14, 1922', 'Case', '', 'So.\n']
                # print("@@@@@@@@@@@@@@@@") # DEBUG
                localCopyOfTempRowOfCSV = tempRowOfCSV[:]

                localCopyOfTempRowOfCSV.append(row_data[0])

                # Title
                if row_data[1]:
                    localCopyOfTempRowOfCSV.append(row_data[1])
                # Date
                if row_data[2]:
                    localCopyOfTempRowOfCSV.append(row_data[2])
                
                finalCSV.append(localCopyOfTempRowOfCSV[:])
                
            
            if row_data[0] == "Abrogated by":
                # print("&&&&&&&&&&&&&&&&") # DEBUG
                localCopyOfTempRowOfCSV = tempRowOfCSV[:]

                localCopyOfTempRowOfCSV.append(row_data[0])

                # Title
                if row_data[1]:
                    localCopyOfTempRowOfCSV.append(row_data[1])
                # Date
                if row_data[2]:
                    localCopyOfTempRowOfCSV.append(row_data[2])

                finalCSV.append(localCopyOfTempRowOfCSV[:])

                
            if row_data[0] == "Disavowed by":
                # print("*****************") # DEBUG
                localCopyOfTempRowOfCSV = tempRowOfCSV[:]

                localCopyOfTempRowOfCSV.append(row_data[0])

                # Title
                if row_data[1]:
                    localCopyOfTempRowOfCSV.append(row_data[1])
                # Date
                if row_data[2]:
                    localCopyOfTempRowOfCSV.append(row_data[2])
                
                finalCSV.append(localCopyOfTempRowOfCSV[:])

                
    
    # print("=========================================================================") # DEBUG
    # print(len(finalCSV)) # DEBUG

    with open('test.csv', 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(["DOCUMENT INFORMATION", "PRIMARY CASE INFORMATION", "TREATMENT", "TREATED CASE INFORMATION", "TREATED CASE DATE"])
        write.writerows(finalCSV)

    # for csvRows in finalCSV: # DEBUG
    #     print(csvRows) # DEBUG
    #     print("$$$$$$$$$$$$$$$$$") # DEBUG


# Example usage:
docx_file = '/Users/kdhyani/desktop/west-law/WestCheck Report_12-30-2023_05.00.01.docx'  # https://www.dropbox.com/home/data%20for%20sanskriti/Processed%20files/States/Georgia/Process?preview=WestCheck+Report_12-30-2023_05.00.01.docx
read_docx_table(docx_file)


# for row in table_data:
#     print(row)