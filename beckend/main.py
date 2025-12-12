import tkinter as tk
from tkinter import messagebox


class MainMenuApp:
    def __init__(self, master):
        self.master = master
        master.title("Hệ Thống Quản Lý Thư Viện - Menu Chính")
        # Thiết lập kích thước cửa sổ và căn giữa các nút
        master.geometry("500x400")

        # --- Thiết lập Frame chứa các nút ---
        self.menu_frame = tk.Frame(master, padx=30, pady=30)
        self.menu_frame.pack(expand=True)

        tk.Label(self.menu_frame, text="CHỌN CHỨC NĂNG QUẢN LÝ", font=("Arial", 16, "bold"), fg="#005a8d").pack(pady=20)

        # Danh sách các chức năng
        self.functions = {
            "Quản lý Danh mục Sách": self.open_book_management,
            "Quản lý Bạn đọc": self.open_reader_management,
            "Quản lý Mượn – Trả – Gia hạn": self.open_loan_management,
            "Quản lý Nhân viên": self.open_staff_management,
            "Báo cáo – Thống kê": self.open_report_management
        }

        # Tạo các nút bấm tương ứng
        for text, command in self.functions.items():
            button = tk.Button(self.menu_frame,
                               text=text,
                               command=lambda cmd=command, title=text: self.dummy_open_window(cmd, title),
                               width=40,
                               height=2,
                               bg="#4CAF50",  # Màu nền xanh lá
                               fg="white",  # Màu chữ trắng
                               font=("Arial", 10, "bold")
                               )
            button.pack(pady=5)

    # --- Các Hàm Giả Định (Dummy Functions) ---

    def dummy_open_window(self, command_func, title):
        """
        Hàm mô phỏng việc mở cửa sổ mới.
        Trong thực tế, hàm này sẽ gọi đến command_func để khởi tạo giao diện mới.
        """
        messagebox.showinfo("Chuyển Hướng",
                            f"Đang chuyển đến giao diện: {title}.\n(Chức năng thực tế sẽ được triển khai sau.)")

        # Gọi hàm tương ứng để chuẩn bị cho việc phát triển sau này
        # command_func()

    # Các hàm để chuyển đến giao diện thực tế (sẽ được thay thế sau)
    def open_book_management(self):
        print("Mở Quản lý Danh mục Sách...")
        # Ví dụ: BookManagementWindow(tk.Toplevel(self.master))
        pass

    def open_reader_management(self):
        print("Mở Quản lý Bạn đọc...")
        pass

    def open_loan_management(self):
        print("Mở Quản lý Mượn – Trả – Gia hạn...")
        pass

    def open_staff_management(self):
        print("Mở Quản lý Nhân viên...")
        pass

    def open_report_management(self):
        print("Mở Báo cáo – Thống kê...")
        pass


# --- Khởi chạy ứng dụng ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuApp(root)
    root.mainloop()