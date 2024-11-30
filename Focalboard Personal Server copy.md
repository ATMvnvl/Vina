## Focalboard là một công cụ quản lý dự án nguồn mở, đa ngôn ngữ, tự lưu trữ, là một giải pháp thay thế cho Trello, Notion và Asana. Nó giúp định nghĩa, tổ chức, theo dõi và quản lý công việc trên các cá nhân và nhóm. 
[Focalboard](https://github.com/mattermost-community/focalboard)
## I. Các tính năng chính
### 1. Quản lý Nhiệm vụ
+ Tạo, chỉnh sửa và theo dõi nhiệm vụ.

+ Phân loại nhiệm vụ theo trạng thái (chưa bắt đầu, đang thực hiện, đã hoàn thành).
### 2. Bảng Kanban
+ Tạo bảng kanban để quản lý quy trình làm việc.
+ Kéo và thả nhiệm vụ giữa các cột.
### 3. Ghi Chú và Tài Liệu
Ghi chú nhanh và lưu trữ thông tin quan trọng.
Chia sẻ tài liệu với các thành viên trong nhóm.
### 4. Tùy Chỉnh Bảng
+ Tùy chỉnh các bảng công việc theo nhu cầu của người dùng.
+ Thêm các trường tùy chỉnh để theo dõi thông tin cụ thể.
### 5. Giao Diện Thân Thiện
+ Giao diện người dùng trực quan, dễ sử dụng.
+ Tích hợp các tính năng kéo và thả.
### 6. Tích Hợp với Công Cụ Khác
+ Tích hợp với Mattermost và các công cụ khác để tăng cường khả năng hợp tác.
### 7. Báo Cáo và Phân Tích
+ Cung cấp báo cáo về tiến độ và hiệu suất công việc.
+ Theo dõi thời gian và nguồn lực sử dụng cho từng nhiệm vụ.
### 8. Chia Sẻ và Cộng Tác
+ Chia sẻ bảng và nhiệm vụ với các thành viên trong nhóm.
+ Hỗ trợ cộng tác thời gian thực

## II. Cài đặt

### 1. Tải gói Focalboard

Tải gói lưu trữ trên github và giải nén di chuyển đến /opt
```
apt update -y
wget https://github.com/mattermost/focalboard/releases/download/v0.15.0/focalboard-server-linux-amd64.tar.gz
tar -xvzf focalboard-server-linux-amd64.tar.gz
sudo mv focalboard /opt
```

### 2. Cài đặt Nginx

```
apt update -y && apt install nginx -y 
```
Tạo trang mới về focalboard `vim /etc/nginx/sites-available/focalboard`
```upstream focalboard {
   server 210.211.122.215:8000;
   keepalive 32;
}

server {
   listen 80 default_server;

   server_name server.thapphuquy.online;

   location ~ /ws/* {
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
       client_max_body_size 50M;
       proxy_set_header Host $http_host;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
       proxy_set_header X-Frame-Options SAMEORIGIN;
       proxy_buffers 256 16k;
       proxy_buffer_size 16k;
       client_body_timeout 60;
       send_timeout 300;
       lingering_timeout 5;
       proxy_connect_timeout 1d;
       proxy_send_timeout 1d;
       proxy_read_timeout 1d;
       proxy_pass http://focalboard;
   }

   location / {
       client_max_body_size 50M;
       proxy_set_header Connection "";
       proxy_set_header Host $http_host;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
       proxy_set_header X-Frame-Options SAMEORIGIN;
       proxy_buffers 256 16k;
       proxy_buffer_size 16k;
       proxy_read_timeout 600s;
       proxy_cache_revalidate on;
       proxy_cache_min_uses 2;
       proxy_cache_use_stale timeout;
       proxy_cache_lock on;
       proxy_http_version 1.1;
       proxy_pass http://focalboard;
   }
}

```

Dòng 2 và dòng 9 đổi thành IP và tên miền

![alt text](image-126.png)

Xóa file mặc định của của nginx để thêm focalboard 

```
sudo rm /etc/nginx/sites-enabled/default
```
Tạo một liên kết tượng trưng từ tệp cấu hình của focalboard trong sites-available sang sites-enabled
```
ln -s /etc/nginx/sites-available/focalboard /etc/nginx/sites-enabled/focalboard
```

Kiểm tra cấu hình và tải lại cấu hình Nginx
```
nginx -t
/etc/init.d/nginx reload
```

### 3. Cài đặt Postgresql 
```
apt install postgresql postgresql-contrib -y 
```

Tạo cơ sở dữ liệu mới
```
sudo --login --user postgres
psql 
CREATE DATABASE boards;
CREATE USER secroot WITH PASSWORD 'tpq2025';
\q
```
Cài đặt dbconfig để sử dụng cơ sở dữ liệu Postgres vừa mới tạo 

```
vim /opt/focalboard/config.json
```

```
{
        "serverRoot": "https://210.211.122.215:8000",
        "port": 8000,
        "dbtype": "postgres",
        "dbconfig": "postgres://secroot:tpq2025@localhost:5432/focalboard?sslmode=disable&connect_timeout=10",
        "postgres_dbconfig": "dbname=focalboard sslmode=disable",
        "useSSL": false,
        "webpath": "./pack",
        "filespath": "./files",
    "telemetry": true,
    "prometheus_address": ":9092",
    "session_expire_time": 2592000,
    "session_refresh_time": 18000,
    "localOnly": false,
    "enableLocalMode": true,
    "localModeSocketLocation": "/var/tmp/focalboard_local.socket"
}

```
Dòng dbtype và dbconfig đổi thành Postgres vừa mới tạo trên 

![alt text](image-133.png)

Cấu hình Focalboard để chạy dịch vụ 

```
vim /lib/systemd/system/focalboard.service

[Unit]
Description=Focalboard server

[Service]
Type=simple
Restart=always
RestartSec=5s
ExecStart=/opt/focalboard/bin/focalboard-server
WorkingDirectory=/opt/focalboard

[Install]
WantedBy=multi-user.target

```
Khởi động dịch vụ 
```
sudo systemctl daemon-reload
sudo systemctl start focalboard.service
sudo systemctl enable focalboard.service
````

Khởi động lại các dịch vụ Nginx và Postgres

![alt text](image-134.png)

### 4. Cấu hình cài đặt chứng chỉ SSL
#### 4.1 Cài đặt Certbot:
```
sudo apt update -y 
sudo apt install certbot python3-certbot-nginx -y 
```

#### 4.2 Tạo chứng chỉ SSL cho tên miền hoặc địa chỉ IP

```
sudo certbot certonly --nginx -d server.thapphuquy.online // SSL lưu tại `/etc/letsencrypt/live/server.thapphuquy.online/`

```

#### 4.3 Cấu hình Nginx để chuyển sang HTTPS
Mở đến file `/etc/nginx/sites-available/focalboard`


### 5. Đăng nhập 
+ Đăng nhập với IP hoặc tên miền đã khai báo: https://server.thapphuquy.online

Đăng ký tài khoản lần đầu 
+ Tên đăng nhập:mật khẩu: `quytp:VinaHost2008`

![alt text](image-137.png)

Bảng tổng quan Focalborad 

![alt text](image-138.png)

#### 5.1 Thêm các user khác
Nhấn vào biểu tượng Focalboard --> Invite users --> Copy link

![alt text](image-171.png)

Kết quả

Vào link đã copy [Register](http://server.thapphuquy.online/register?t=kpkrjzh89x3da7ndhinxx8kd3ur) --> Điền thông tin --> Đã tạo thành công với user `tpq`

![alt text](image-172.png)


#### 5.2 Thêm các bảng vào dự án

Ở đây tôi muốn thêm bảng `Roadmap`  --> nhấn `Use this template` để sử dụng 
 
![alt text](image-139.png)

Kết quả 

![alt text](image-140.png)

### 6. Cấu hình lại 
#### 6.1 Content Calendar 
Nhấn vào Content Calendar  --> New 

![alt text](image-178.png)

Kết quả:

![alt text](image-179.png)

#### 6.2 Meeting Agenda 
Nhấn vào Meeting Agenda --> New

![alt text](image-180.png)

Kết quả:

![alt text](image-181.png)

#### 6.3 Personal Goals 
Nhấn Personal Goals --> New 

![alt text](image-182.png)

Kết quả:

![alt text](image-183.png)

#### 6.4 Personal Tasks 
Nhấn Personal Tasks --> New

![alt text](image-184.png)

Kết quả:

![alt text](image-185.png)

#### 6.5 Project Tasks 
Nhấn Project Tasks  --> New

![alt text](image-186.png)

Kết quả:

![alt text](image-187.png)

#### 6.6 Roadmap 
Vào Roadmap --> New

![alt text](image-188.png)

Kết quả:

![alt text](image-189.png)

### 7. Welcome to Boards!

![alt text](image-190.png)