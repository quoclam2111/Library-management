"""
Dashboard View - Trang chủ chính của hệ thống
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class DashboardView(ttk.Frame):
    """View trang chủ Dashboard"""

    def __init__(self, parent, navigate_callback):
        super().__init__(parent)
        self.navigate_callback = navigate_callback

        self._create_widgets()
        self._load_statistics()

    def _create_widgets(self):
        """Tạo giao diện Dashboard"""

        # Header
        header_frame = ttk.Frame(self)
        header_frame.pack(fill='x', padx=20, pady=(20, 10))

        ttk.Label(
            header_frame,
            text="📊 TRANG CHỦ HỆ THỐNG QUẢN LÝ THƯ VIỆN",
            font=('Arial', 20, 'bold'),
            foreground='#1976D2'
        ).pack(anchor='w')

        ttk.Label(
            header_frame,
            text=f"🕐 {datetime.now().strftime('%A, %d/%m/%Y - %H:%M')}",
            font=('Arial', 10),
            foreground='#666'
        ).pack(anchor='w', pady=(5, 0))

        # Main container
        main_container = ttk.Frame(self)
        main_container.pack(fill='both', expand=True, padx=20, pady=10)

        # Statistics Cards (Top)
        self._create_statistics_section(main_container)

        # Quick Access Menu (Middle)
        self._create_quick_access_section(main_container)

        # Recent Activities (Bottom)
        self._create_recent_activities_section(main_container)

    def _create_statistics_section(self, parent):
        """Tạo phần thống kê tổng quan"""
        stats_frame = ttk.LabelFrame(parent, text="📈 Thống kê tổng quan", padding=15)
        stats_frame.pack(fill='x', pady=(0, 15))

        # Container cho các card
        cards_container = ttk.Frame(stats_frame)
        cards_container.pack(fill='x')

        # Statistics data
        stats = [
            {"icon": "👥", "title": "Bạn đọc", "value": "0", "color": "#4CAF50", "change": "+0%"},
            {"icon": "📚", "title": "Sách", "value": "0", "color": "#2196F3", "change": "+0%"},
            {"icon": "📋", "title": "Đang mượn", "value": "0", "color": "#FF9800", "change": "0"},
            {"icon": "💰", "title": "Phạt chưa thu", "value": "0₫", "color": "#F44336", "change": "0"}
        ]

        for i, stat in enumerate(stats):
            self._create_stat_card(cards_container, stat, i)

    def _create_stat_card(self, parent, data, column):
        """Tạo card thống kê"""
        card = tk.Frame(parent, bg='white', relief='raised', borderwidth=1)
        card.grid(row=0, column=column, padx=10, pady=10, sticky='ew')
        parent.columnconfigure(column, weight=1)

        # Icon
        icon_label = tk.Label(
            card,
            text=data['icon'],
            font=('Arial', 32),
            bg='white'
        )
        icon_label.pack(pady=(15, 5))

        # Value
        value_label = tk.Label(
            card,
            text=data['value'],
            font=('Arial', 24, 'bold'),
            fg=data['color'],
            bg='white'
        )
        value_label.pack()

        # Title
        title_label = tk.Label(
            card,
            text=data['title'],
            font=('Arial', 11),
            fg='#666',
            bg='white'
        )
        title_label.pack(pady=(0, 15))

    def _create_quick_access_section(self, parent):
        """Tạo phần truy cập nhanh"""
        access_frame = ttk.LabelFrame(parent, text="🚀 Truy cập nhanh", padding=15)
        access_frame.pack(fill='both', expand=True, pady=(0, 15))

        # Container cho các nút
        buttons_container = ttk.Frame(access_frame)
        buttons_container.pack(expand=True)

        # Quick access buttons
        buttons = [
            {"text": "👥 Quản lý\nBạn đọc", "color": "#4CAF50", "tab": 1},
            {"text": "📚 Quản lý\nSách", "color": "#2196F3", "tab": 2},
            {"text": "📋 Mượn/Trả\nSách", "color": "#FF9800", "tab": 3},
            {"text": "💰 Quản lý\nPhạt", "color": "#F44336", "tab": 4},
            {"text": "👨‍💼 Quản lý\nNhân viên", "color": "#9C27B0", "tab": 5},
            {"text": "📊 Báo cáo\nThống kê", "color": "#607D8B", "tab": 6}
        ]

        # Tạo grid 2 hàng x 3 cột
        for i, btn in enumerate(buttons):
            row = i // 3
            col = i % 3
            self._create_quick_button(buttons_container, btn, row, col)

    def _create_quick_button(self, parent, data, row, col):
        """Tạo nút truy cập nhanh"""
        btn = tk.Button(
            parent,
            text=data['text'],
            font=('Arial', 12, 'bold'),
            bg=data['color'],
            fg='white',
            activebackground=self._darken_color(data['color']),
            activeforeground='white',
            width=15,
            height=4,
            cursor='hand2',
            command=lambda: self.navigate_callback(data['tab'])
        )
        btn.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        parent.rowconfigure(row, weight=1)
        parent.columnconfigure(col, weight=1)

        # Hover effect
        def on_enter(e):
            btn['bg'] = self._darken_color(data['color'])

        def on_leave(e):
            btn['bg'] = data['color']

        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)

    def _create_recent_activities_section(self, parent):
        """Tạo phần hoạt động gần đây"""
        activity_frame = ttk.LabelFrame(parent, text="🕒 Hoạt động gần đây", padding=15)
        activity_frame.pack(fill='both', expand=True)

        # Treeview for activities
        columns = ('time', 'user', 'action', 'detail')
        tree = ttk.Treeview(activity_frame, columns=columns, show='headings', height=5)

        tree.heading('time', text='Thời gian')
        tree.heading('user', text='Người thực hiện')
        tree.heading('action', text='Hành động')
        tree.heading('detail', text='Chi tiết')

        tree.column('time', width=150)
        tree.column('user', width=150)
        tree.column('action', width=150)
        tree.column('detail', width=300)

        # Scrollbar
        scrollbar = ttk.Scrollbar(activity_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Sample data
        activities = [
            (datetime.now().strftime('%H:%M:%S'), 'Admin', 'Đăng nhập', 'Đăng nhập vào hệ thống'),
        ]

        for activity in activities:
            tree.insert('', 'end', values=activity)

    def _load_statistics(self):
        """Load dữ liệu thống kê từ database"""
        try:
            # TODO: Implement actual database queries
            # from controllers.reader_controller import ReaderController
            # reader_count = ReaderController.count_all()
            pass
        except Exception as e:
            logger.error(f"Error loading statistics: {e}")

    def _darken_color(self, hex_color, factor=0.8):
        """Làm tối màu"""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        darkened = tuple(int(c * factor) for c in rgb)
        return f'#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}'