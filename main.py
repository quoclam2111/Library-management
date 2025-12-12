"""
Library Management System - Main Entry Point
============================================

Hệ thống quản lý thư viện với Python GUI
Sử dụng:  Tkinter + MySQL + MVC Architecture

Author: NvkhoaDev54
Version: 1.0.0
Year: 2025
"""

import tkinter as tk
from tkinter import messagebox
import sys
import logging
from pathlib import Path

# Setup logging
log_dir = Path(__file__).parent / 'logs'
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging. FileHandler(log_dir / 'app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def check_dependencies():
    """Kiểm tra các thư viện cần thiết"""
    required_packages = {
        'mysql': 'mysql-connector-python',           # ✅ FIX: mysql chứ không phải mysql.connector
        'openpyxl': 'openpyxl',
        'reportlab': 'reportlab',
        'dotenv': 'python-dotenv'
    }

    missing = []
    for package, pip_name in required_packages.items():
        try:
            __import__(package)
            logger. info(f"✓ Package '{package}' found")
        except ImportError:
            logger.warning(f"✗ Package '{package}' not found")
            missing.append(pip_name)

    if missing:
        error_msg = (
            "❌ Thiếu các thư viện sau:\n\n" +
            "\n".join(f"  • {pkg}" for pkg in missing) +
            "\n\nVui lòng cài đặt:\n" +
            f"pip install {' '.join(missing)}"
        )
        messagebox.showerror("Thiếu thư viện", error_msg)
        return False

    logger.info("✅ All dependencies OK")
    return True


def main():
    """Entry point của ứng dụng"""
    try:
        logger.info("="*50)
        logger.info("Starting Library Management System")
        logger.info("="*50)

        # Check dependencies
        if not check_dependencies():
            logger.error("Dependencies check failed")
            sys.exit(1)

        # Import views (after dependency check)
        from views.main_window import MainWindow

        # Create and run application
        logger.info("Creating main window...")
        app = MainWindow()

        logger.info("✅ Application started successfully")

        # Start main loop
        app.mainloop()

    except KeyboardInterrupt:
        logger. info("Application interrupted by user (Ctrl+C)")
        sys.exit(0)

    except ImportError as e:
        logger. critical(f"Import error: {e}", exc_info=True)
        messagebox. showerror(
            "Lỗi Import",
            f"Không thể import module:\n\n{str(e)}\n\n"
            f"Vui lòng kiểm tra:\n"
            f"1. Đã cài đặt đầy đủ dependencies\n"
            f"2. Đang chạy trong virtual environment đúng\n"
            f"3. Cấu trúc thư mục đúng"
        )
        sys.exit(1)

    except Exception as e:
        logger.critical(f"Critical error: {e}", exc_info=True)
        messagebox. showerror(
            "Lỗi nghiêm trọng",
            f"Ứng dụng gặp lỗi không mong muốn:\n\n{str(e)}\n\n"
            f"Vui lòng xem file log để biết thêm chi tiết:\n"
            f"{log_dir / 'app. log'}"
        )
        sys.exit(1)

    finally:
        logger.info("Application shutdown")
        logger.info("="*50)
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


if __name__ == "__main__":
    main()
    root = tk.Tk()
    app = MainMenuApp(root)
    root.mainloop()