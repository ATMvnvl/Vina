 |# Web App Helper là một công cụ quản lý các dự án của mình 
## Các tính năng chính
| Các tính năng             | Miêu tả | 
| :------------             | :------ | 
| Permissions  | Cấp quyền cụ thể từng người dùng khi tạo  |
| Roles           | Thêm các vai trò cần thiết cho người dùng |
| Project - Ticket          | Hỗ trợ theo dõi dễ dàng  | 
| Language | Hỗ trợ nhiều ngôn ngữ | 
|Login | Hỗ trợ nhiều loại xác thực OIDC, Google, Facebook| 

## So sánh Leantime với Helper
| Phân loại | Helper | Leantime| 
| :-------- | -------- | ------ |
| Chung | Đều mã nguồn mở, quản lý các dự án, triển khai dễ dàng với công nghệ Docker, hỗ trợ nhiều ngôn ngữ | 
| Nền tảng  | Laravel, TailwindCSS, Filament, PHP 8 | PHP, Vue.js, Bulma CSS |
| Xác thực	| OAuth, OpenID Connect | Không hỗ trợ OAuth mặc định | 
| Quản lý dự án	| Tickets, thời gian thực, bảng Kanban | Bảng Kanban, Scrum, Roadmap, OKR |
| Đối tượng người dùng | Nhóm phát triển phần mềm nhỏ | Doanh nghiệp vừa và nhỏ, startup | 
| Chức năng theo thời gian thực | Pusher tích hợp | Không có mặc định |


## [Documents](https://devaslanphp.github.io/project-management/#/installation?id=installing-the-project)

## [Github](https://github.com/devaslanphp/project-management)

### Fix lỗi không update được 

![alt text](image-3.png)

### Đổi source với lệnh sau: `sudo sed -i 's|http://de.archive.ubuntu.com|http://archive.ubuntu.com|g' /etc/apt/sources.list`

Kết quả: 

![alt text](image-4.png)

### Tiến hành git clone về với lệnh sau: `git clone https://github.com/devaslanphp/project-management && cd project-management`

![alt text](image-6.png)

### Tiến hành cài `docker.io và docker-compose`

![alt text](image-7.png)

### Tiến hành Build image locally lệnh sau: `docker build --network=host -t vina/helper:latest .`  (khá lâu )

![alt text](image-8.png)

### Lệnh để xây dựng vùng chứa docker: `docker-compose up -d` (khá lâu)

![alt text](image-9.png)

### Kiểm tra các docker container đã build: `docker ps -a` 

![alt text](image-10.png)

### Tiến hành login url: `http://103.153.254.29:8000/login`

### Khi login báo như sau: chưa có database về user tiến hành tạo 

![alt text](image-11.png)

### Tiến hành thực hiện lệnh trong một container đang chạy bằng lệnh sau: `docker exec -it helper-server /bin/bash`

![alt text](image-12.png)

### Tiến hành update container và cài đặt vim

![alt text](image-13.png)

### Chạy lệnh `npm audit fix` nếu có lỗi khi dùng lệnh npm install 

![alt text](image-14.png)

### Tạo khóa ứng dụng lệnh sau: ` php artisan key:generate` (có thể bỏ qua)

![alt text](image-15.png)

### Tạo cơ sở dữ liệu: `php artisan migrate`

![alt text](image-16.png)

### Tạo cơ sở dữ liệu để chèn người dùng mặc định thông tin tham chiếu và quyền lệnh sau: `php artisan db:seed`

![alt text](image-17.png)

### Triến khai dự án vào hoạt động: ` npm run build`

![alt text](image-18.png)

### Tiến hành đăng nhập lại url: `http://103.153.254.29:8000/`
+ Login: user:pass: `john.doe@helper.app:Passw@rd`

### Bảng tổng quan về Helper 

![alt text](image-19.png)

### Tiến hành tạo thêm user lệnh sau: `php artisan tinker`

![alt text](image-22.png)

### Tiến hành login với user và pass mới tạo (`secroot1112@gmail.com` và `vinahost`)

### Hệ thống bắt xác thực Email 

![alt text](image-23.png)

![alt text](image-24.png)

### Ta có bỏ qua xác thực mail chỉnh sửa trong file sau: `vim app/Models/User.php`
+ Dòng 9 và 23 comment 
+ Dòng 24 thêm như sau: `class User extends Authenticatable implements FilamentUser`

![alt text](image-25.png)

### Tiến hành đăng nhập lại và ta thành công với bảng Dashboard với user `secroot1112@gmail.com`

![alt text](image-26.png)

### Tạo tài khoản user trên web 

![alt text](image-28.png)

![alt text](image-29.png)

### Qua bảng Dashboard của Admin vào User kiểm tra các user trên hệ thống

![alt text](image-30.png)

### Tạo dự án và thêm các ngươi dùng 

Tạo `Project statuses` rồi nhấn Create

![alt text](image-31.png)

Tạo `Projects`  rồi nhấn Create 

![alt text](image-32.png)

Thêm user vào trong Project --> cuộn xuống dưới User --> Attach --> thêm các user vào dự án --> Attach

![alt text](image-33.png)

![alt text](image-34.png)

Kết quả:

![alt text](image-35.png)

Kiểm tra tài khoản của người dùng 

![alt text](image-37.png)

![alt text](image-36.png)

### Thêm các quyền vai trò cho người dùng 

Thêm vai trò vào mục `Permission --> Roles --> New role --> Nhập Permission name --> Add các quyền cần thiết --> Create`

Kết quả đã tạo thành công với roles tên là `Guest`

![alt text](image-40.png)

![alt text](image-41.png)

Thêm các quyền vào người dùng vào mục `Permission --> Users --> Chọn user cần thêm role -->  Edit --> Tick Permission roles chọn Guest --> Save changes`

Kết quả client với email secroot1112@gmail.com đã thêm thành công vào roles vừa mới tạo là Guest

![alt text](image-39.png)

Kiểm tra quyền trên máy khách về ticket 

Vào Board --> Chọn Project Thử Nghiệm 

![alt text](image-42.png)

![alt text](image-43.png)

### Vào Test để thử các chức năng 
Bảng tổng quan Tickets

![alt text](image-44.png)

Mục `Comments`

![alt text](image-45.png)

Kết quả:

![alt text](image-46.png)

Mục `Activities`

![alt text](image-47.png)

Mục `Time logged`

![alt text](image-48.png)

Mục `Attachments`

![alt text](image-49.png)

Kết quả:

![alt text](image-50.png)

![alt text](image-51.png)