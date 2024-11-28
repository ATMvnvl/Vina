import os
import re
import base64

def convert_images_to_base64(md_file_path):
    if not md_file_path.endswith('.md'):
        raise ValueError("File cần phải có đuôi '.md'")
    
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Tìm tất cả các đường dẫn ảnh trong file Markdown
    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    matches = image_pattern.findall(content)
    
    for image_path in matches:
        # Kiểm tra xem ảnh có tồn tại không
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
            # Tạo chuỗi Base64
            mime_type = "image/" + image_path.split('.')[-1]  # Ví dụ: image/png
            base64_string = f"data:{mime_type};base64,{encoded_string}"
            # Thay thế trong nội dung Markdown
            content = content.replace(image_path, base64_string)
        else:
            print(f"⚠️ Không tìm thấy ảnh: {image_path}")
    
    # Ghi lại nội dung Markdown với ảnh Base64
    output_file = md_file_path.replace('.md', '_base64.md')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"✅ Đã xử lý xong! File mới được lưu tại: {output_file}")

# Thay 'your_md_file.md' bằng đường dẫn file của bạn
convert_images_to_base64(r"D:\Downloads\Vinahost\VPS Service.md")
