#TiKaY - Ứng Dụng Làm Mờ Ảnh Gaussian
##Giới thiệu
TiKaY là một ứng dụng Python đơn giản được xây dựng bằng thư viện tkinter để tạo giao diện người dùng đồ họa và thư viện PIL (Pillow) để xử lý ảnh. Ứng dụng này cho phép người dùng tải lên một hình ảnh, áp dụng bộ lọc làm mờ Gaussian cho hình ảnh và xem hình ảnh gốc và hình ảnh đã làm mờ cùng một lúc.

##Tính Năng:
-Tải Lên Hình Ảnh: Nhấn nút "Tải Lên Hình Ảnh" để chọn một tệp hình ảnh từ máy tính của bạn. Hình ảnh đã tải lên sẽ được hiển thị bên trái của giao diện.

-Thiết Lập Độ Mờ: Nhập giá trị độ mờ vào trường nhập liệu được cung cấp. Giá trị này quyết định độ mạnh của hiệu ứng làm mờ.

-Áp Dụng Mờ: Nhấn nút "LÀM MỜ" để áp dụng bộ lọc làm mờ Gaussian cho hình ảnh đã tải lên dựa trên giá trị độ mờ được chỉ định. Hình ảnh đã làm mờ sẽ được hiển thị bên phải của giao diện.

##Yêu Cầu:
Python 3.x
-Thư viện tkinter (thường được bao gồm trong thư viện tiêu chuẩn của Python)
-Thư viện Pillow (PIL) (pip install Pillow)

##Hướng Dẫn Sử Dụng:
-Sao Chép Repository:
git clone https://github.com/ten-dang-nhap-cua-ban/TiKaY-Gaussian-Blur-App.git

-Di Chuyển Đến Thư Mục Dự Án:
cd TiKaY-Gaussian-Blur-App

-Chạy Ứng Dụng:
python main.py

-Tải Lên Một Hình Ảnh:
Nhấn nút "Tải Lên Hình Ảnh".
Chọn một tệp hình ảnh từ máy tính của bạn.

-Thiết Lập Độ Mờ:
Nhập giá trị nguyên biểu thị cho độ mờ vào trường nhập liệu.

-Áp Dụng Mờ:
Nhấn nút "LÀM MỜ" để áp dụng bộ lọc làm mờ Gaussian cho hình ảnh đã tải lên.

-Xem Kết Quả:
Hình ảnh gốc sẽ được hiển thị bên trái, và hình ảnh đã làm mờ sẽ được hiển thị bên phải.
