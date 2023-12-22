from bs4 import BeautifulSoup

# Read the content of the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <tr> tags that contain an anchor tag with class "text_2"
target_tr_tags = soup.find_all(lambda tag: tag.name == 'tr' and tag.find('a', class_='text_2') is not None)

# Print or process the extracted <tr> tags
for tr_tag in target_tr_tags:
    print(tr_tag)


# from bs4 import BeautifulSoup

# def extract_tr_with_img(html_path):
#     with open(html_path, 'r', encoding='utf-8') as html_file:
#         soup = BeautifulSoup(html_file, 'html.parser')
    
#     # Find all <tr> tags
#     tr_tags = soup.find_all('tr')

#     # Filter <tr> tags that contain an <img> tag
#     tr_with_img_list = [tr_tag for tr_tag in tr_tags if tr_tag.find('img') is not None]
    
#     return tr_with_img_list

# if __name__ == "__main__":
#     html_path = "merged.html"  # Replace with the path to your HTML file

#     tr_with_img_list = extract_tr_with_img(html_path)

#     # Print the extracted <tr> tags
#     for tr_tag in tr_with_img_list:
#         print(tr_tag)
# from bs4 import BeautifulSoup

# # Read HTML content from the file
# file_path = './merged.html'
# with open(file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all <tr> tags
# all_trs = soup.find_all('tr')

# # Extract the content of <tr> tags that contain an <img> tag
# extracted_content = []
# for tr in all_trs:
#     if tr.find('img') is not None:
#         extracted_content.append(str(tr))

# # Print or use the extracted content as needed
# for content in extracted_content:
#     print(content)