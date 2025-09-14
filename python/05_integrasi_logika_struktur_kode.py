# ===============================================
# TUTORIAL 5: INTEGRASI LOGIKA DAN STRUKTUR KODE
# ===============================================

"""
Tutorial ini mengintegrasikan semua konsep yang sudah dipelajari:
1. Alur Logika (Conditions)
2. Perulangan (Loops) 
3. Fungsi (Functions)
4. Object-Oriented Programming (OOP)

Kita akan membuat sebuah aplikasi lengkap: SISTEM MANAJEMEN TOKO ONLINE
yang mendemonstrasikan penggunaan semua konsep tersebut dalam satu project.
"""

print("="*70)
print("TUTORIAL 5: INTEGRASI LOGIKA DAN STRUKTUR KODE")
print("PROJECT: SISTEM MANAJEMEN TOKO ONLINE")
print("="*70)

# ==================
# IMPORT LIBRARIES
# ==================
import datetime
import json
from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Union
import uuid

# ==================
# 1. BASE CLASSES DAN ABSTRACT CLASSES
# ==================

class Identifiable(ABC):
    """Abstract base class untuk object yang memiliki ID"""
    
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]  # Generate unique ID
        self.created_at = datetime.datetime.now()

class Printable(ABC):
    """Abstract base class untuk object yang bisa dicetak"""
    
    @abstractmethod
    def to_dict(self) -> Dict:
        pass
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str, indent=2)

# ==================
# 2. UTILITY FUNCTIONS
# ==================

def format_currency(amount: float) -> str:
    """Utility function untuk format mata uang"""
    return f"Rp{amount:,.0f}"

def validate_email(email: str) -> bool:
    """Function untuk validasi email menggunakan conditions"""
    if not email or "@" not in email:
        return False
    
    parts = email.split("@")
    if len(parts) != 2:
        return False
    
    username, domain = parts
    return len(username) > 0 and "." in domain

def validate_phone(phone: str) -> bool:
    """Function untuk validasi nomor telepon"""
    clean_phone = phone.replace(" ", "").replace("-", "").replace("+", "")
    return clean_phone.isdigit() and len(clean_phone) >= 10

def calculate_discount(subtotal: float, discount_type: str, discount_value: float) -> float:
    """Function untuk menghitung diskon menggunakan conditions"""
    if discount_type == "percentage":
        if discount_value > 100:
            discount_value = 100
        return subtotal * (discount_value / 100)
    elif discount_type == "fixed":
        return min(discount_value, subtotal)
    else:
        return 0.0

# ==================
# 3. PRODUCT CLASSES (OOP + Inheritance)
# ==================

class Product(Identifiable, Printable):
    """Base class untuk semua produk"""
    
    def __init__(self, name: str, price: float, description: str = ""):
        super().__init__()
        self.name = name
        self.price = price
        self.description = description
        self.stock = 0
        self.category = "General"
        self.is_active = True
    
    def set_stock(self, quantity: int) -> str:
        """Method dengan validation menggunakan conditions"""
        if quantity < 0:
            return "Stock tidak bisa negatif!"
        
        self.stock = quantity
        return f"Stock {self.name} diupdate menjadi {quantity}"
    
    def add_stock(self, quantity: int) -> str:
        """Method untuk menambah stock"""
        if quantity <= 0:
            return "Jumlah yang ditambahkan harus positif!"
        
        self.stock += quantity
        return f"Stock {self.name} ditambah {quantity}. Total: {self.stock}"
    
    def reduce_stock(self, quantity: int) -> tuple[bool, str]:
        """Method untuk mengurangi stock dengan return boolean dan message"""
        if quantity <= 0:
            return False, "Jumlah yang dikurangi harus positif!"
        
        if quantity > self.stock:
            return False, f"Stock tidak mencukupi! Tersedia: {self.stock}"
        
        self.stock -= quantity
        return True, f"Stock {self.name} dikurangi {quantity}. Sisa: {self.stock}"
    
    def is_available(self) -> bool:
        """Check availability menggunakan conditions"""
        return self.is_active and self.stock > 0
    
    def get_info(self) -> str:
        """Get product information"""
        status = "Tersedia" if self.is_available() else "Tidak Tersedia"
        return f"{self.name} - {format_currency(self.price)} ({status}, Stock: {self.stock})"
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock": self.stock,
            "category": self.category,
            "is_active": self.is_active,
            "created_at": self.created_at
        }

class Electronics(Product):
    """Child class untuk produk elektronik"""
    
    def __init__(self, name: str, price: float, brand: str, warranty_months: int, description: str = ""):
        super().__init__(name, price, description)
        self.brand = brand
        self.warranty_months = warranty_months
        self.category = "Electronics"
    
    def get_warranty_info(self) -> str:
        return f"Garansi {self.warranty_months} bulan dari {self.brand}"
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            "brand": self.brand,
            "warranty_months": self.warranty_months
        })
        return data

class Clothing(Product):
    """Child class untuk produk pakaian"""
    
    def __init__(self, name: str, price: float, size: str, color: str, material: str, description: str = ""):
        super().__init__(name, price, description)
        self.size = size
        self.color = color
        self.material = material
        self.category = "Clothing"
    
    def get_variant_info(self) -> str:
        return f"Size: {self.size}, Color: {self.color}, Material: {self.material}"
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            "size": self.size,
            "color": self.color,
            "material": self.material
        })
        return data

class Book(Product):
    """Child class untuk buku"""
    
    def __init__(self, name: str, price: float, author: str, isbn: str, pages: int, description: str = ""):
        super().__init__(name, price, description)
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.category = "Books"
    
    def get_book_info(self) -> str:
        return f"Penulis: {self.author}, ISBN: {self.isbn}, {self.pages} halaman"
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            "author": self.author,
            "isbn": self.isbn,
            "pages": self.pages
        })
        return data

# ==================
# 4. USER CLASSES (OOP + Encapsulation)
# ==================

class User(Identifiable, Printable):
    """Base class untuk user system"""
    
    def __init__(self, name: str, email: str, phone: str):
        super().__init__()
        self.name = name
        self.__email = ""  # Private attribute
        self.__phone = ""  # Private attribute
        self.is_active = True
        
        # Use setters with validation
        self.set_email(email)
        self.set_phone(phone)
    
    @property
    def email(self) -> str:
        return self.__email
    
    def set_email(self, email: str) -> bool:
        """Setter dengan validasi menggunakan conditions"""
        if validate_email(email):
            self.__email = email
            return True
        return False
    
    @property
    def phone(self) -> str:
        return self.__phone
    
    def set_phone(self, phone: str) -> bool:
        """Setter dengan validasi"""
        if validate_phone(phone):
            self.__phone = phone
            return True
        return False
    
    def get_contact_info(self) -> str:
        return f"Email: {self.email}, Phone: {self.phone}"
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "is_active": self.is_active,
            "created_at": self.created_at
        }

class Customer(User):
    """Customer class dengan additional features"""
    
    def __init__(self, name: str, email: str, phone: str, address: str = ""):
        super().__init__(name, email, phone)
        self.address = address
        self.total_orders = 0
        self.total_spent = 0.0
        self.membership_level = "Bronze"
    
    def update_after_order(self, order_total: float):
        """Update customer data setelah order - menggunakan conditions untuk membership"""
        self.total_orders += 1
        self.total_spent += order_total
        
        # Update membership level menggunakan conditions
        if self.total_spent >= 10000000:  # 10 juta
            self.membership_level = "Platinum"
        elif self.total_spent >= 5000000:  # 5 juta
            self.membership_level = "Gold"
        elif self.total_spent >= 1000000:  # 1 juta
            self.membership_level = "Silver"
        else:
            self.membership_level = "Bronze"
    
    def get_discount_rate(self) -> float:
        """Get discount rate berdasarkan membership - menggunakan conditions"""
        discount_rates = {
            "Bronze": 0.0,
            "Silver": 0.05,
            "Gold": 0.10,
            "Platinum": 0.15
        }
        return discount_rates.get(self.membership_level, 0.0)
    
    def get_customer_summary(self) -> str:
        return f"""
Customer: {self.name}
Membership: {self.membership_level}
Total Orders: {self.total_orders}
Total Spent: {format_currency(self.total_spent)}
Discount Rate: {self.get_discount_rate()*100:.0f}%
        """
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            "address": self.address,
            "total_orders": self.total_orders,
            "total_spent": self.total_spent,
            "membership_level": self.membership_level
        })
        return data

# ==================
# 5. ORDER SYSTEM (OOP + Complex Logic)
# ==================

class OrderItem:
    """Class untuk item dalam order"""
    
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.unit_price = product.price
    
    def get_subtotal(self) -> float:
        return self.unit_price * self.quantity
    
    def to_dict(self) -> Dict:
        return {
            "product_id": self.product.id,
            "product_name": self.product.name,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "subtotal": self.get_subtotal()
        }

class Order(Identifiable, Printable):
    """Class untuk order dengan complex business logic"""
    
    def __init__(self, customer: Customer):
        super().__init__()
        self.customer = customer
        self.items: List[OrderItem] = []
        self.status = "draft"  # draft, confirmed, shipped, delivered, cancelled
        self.discount_amount = 0.0
        self.shipping_cost = 0.0
        self.tax_rate = 0.11  # PPN 11%
    
    def add_item(self, product: Product, quantity: int) -> str:
        """Add item ke order dengan validation - menggunakan conditions"""
        if not product.is_available():
            return f"Produk {product.name} tidak tersedia!"
        
        if quantity <= 0:
            return "Quantity harus lebih dari 0!"
        
        if quantity > product.stock:
            return f"Stock tidak mencukupi! Tersedia: {product.stock}"
        
        # Cek apakah produk sudah ada di order
        existing_item = None
        for item in self.items:
            if item.product.id == product.id:
                existing_item = item
                break
        
        if existing_item:
            # Update quantity jika produk sudah ada
            new_quantity = existing_item.quantity + quantity
            if new_quantity > product.stock:
                return f"Total quantity melebihi stock! Stock tersedia: {product.stock}"
            existing_item.quantity = new_quantity
            return f"Quantity {product.name} diupdate menjadi {new_quantity}"
        else:
            # Tambah item baru
            self.items.append(OrderItem(product, quantity))
            return f"{quantity}x {product.name} ditambahkan ke order"
    
    def remove_item(self, product_id: str) -> str:
        """Remove item dari order - menggunakan loops"""
        for i, item in enumerate(self.items):
            if item.product.id == product_id:
                removed_item = self.items.pop(i)
                return f"{removed_item.product.name} dihapus dari order"
        
        return "Produk tidak ditemukan dalam order"
    
    def update_item_quantity(self, product_id: str, new_quantity: int) -> str:
        """Update quantity item - menggunakan loops dan conditions"""
        if new_quantity <= 0:
            return self.remove_item(product_id)
        
        for item in self.items:
            if item.product.id == product_id:
                if new_quantity > item.product.stock:
                    return f"Stock tidak mencukupi! Tersedia: {item.product.stock}"
                
                old_quantity = item.quantity
                item.quantity = new_quantity
                return f"Quantity {item.product.name} diupdate dari {old_quantity} ke {new_quantity}"
        
        return "Produk tidak ditemukan dalam order"
    
    def calculate_subtotal(self) -> float:
        """Calculate subtotal menggunakan loops"""
        subtotal = 0.0
        for item in self.items:
            subtotal += item.get_subtotal()
        return subtotal
    
    def apply_membership_discount(self):
        """Apply discount berdasarkan membership level"""
        subtotal = self.calculate_subtotal()
        discount_rate = self.customer.get_discount_rate()
        self.discount_amount = subtotal * discount_rate
    
    def calculate_shipping(self) -> float:
        """Calculate shipping cost menggunakan conditions"""
        subtotal = self.calculate_subtotal()
        
        if subtotal >= 500000:  # Free shipping untuk pembelian >= 500rb
            return 0.0
        elif subtotal >= 200000:  # Diskon shipping 50%
            return 15000.0
        else:
            return 30000.0
    
    def calculate_tax(self) -> float:
        """Calculate tax"""
        subtotal = self.calculate_subtotal()
        return (subtotal - self.discount_amount) * self.tax_rate
    
    def calculate_total(self) -> float:
        """Calculate total order"""
        subtotal = self.calculate_subtotal()
        self.shipping_cost = self.calculate_shipping()
        tax = self.calculate_tax()
        
        return subtotal - self.discount_amount + self.shipping_cost + tax
    
    def confirm_order(self) -> tuple[bool, str]:
        """Confirm order dan update stock - menggunakan conditions dan loops"""
        if len(self.items) == 0:
            return False, "Order kosong!"
        
        if self.status != "draft":
            return False, f"Order sudah dalam status {self.status}"
        
        # Validasi stock untuk semua item
        for item in self.items:
            if not item.product.is_available():
                return False, f"Produk {item.product.name} tidak tersedia!"
            
            if item.quantity > item.product.stock:
                return False, f"Stock {item.product.name} tidak mencukupi!"
        
        # Update stock untuk semua item
        for item in self.items:
            success, message = item.product.reduce_stock(item.quantity)
            if not success:
                return False, f"Gagal mengurangi stock {item.product.name}: {message}"
        
        # Apply discount dan update customer
        self.apply_membership_discount()
        total = self.calculate_total()
        self.customer.update_after_order(total)
        
        self.status = "confirmed"
        return True, f"Order berhasil dikonfirmasi! Total: {format_currency(total)}"
    
    def cancel_order(self) -> str:
        """Cancel order dan restore stock - menggunakan conditions"""
        if self.status not in ["draft", "confirmed"]:
            return f"Order dalam status {self.status} tidak bisa dibatalkan"
        
        if self.status == "confirmed":
            # Restore stock jika order sudah confirmed
            for item in self.items:
                item.product.add_stock(item.quantity)
        
        self.status = "cancelled"
        return "Order berhasil dibatalkan"
    
    def get_order_summary(self) -> str:
        """Get order summary - menggunakan loops untuk format"""
        if not self.items:
            return "Order kosong"
        
        summary = f"\n=== ORDER SUMMARY ===\n"
        summary += f"Order ID: {self.id}\n"
        summary += f"Customer: {self.customer.name}\n"
        summary += f"Status: {self.status.upper()}\n\n"
        
        summary += "Items:\n"
        for item in self.items:
            summary += f"  {item.quantity}x {item.product.name} @ {format_currency(item.unit_price)} = {format_currency(item.get_subtotal())}\n"
        
        subtotal = self.calculate_subtotal()
        summary += f"\nSubtotal: {format_currency(subtotal)}\n"
        
        if self.discount_amount > 0:
            summary += f"Discount ({self.customer.membership_level}): -{format_currency(self.discount_amount)}\n"
        
        summary += f"Shipping: {format_currency(self.shipping_cost)}\n"
        summary += f"Tax (11%): {format_currency(self.calculate_tax())}\n"
        summary += f"TOTAL: {format_currency(self.calculate_total())}\n"
        
        return summary
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "customer": self.customer.to_dict(),
            "items": [item.to_dict() for item in self.items],
            "status": self.status,
            "subtotal": self.calculate_subtotal(),
            "discount_amount": self.discount_amount,
            "shipping_cost": self.shipping_cost,
            "tax": self.calculate_tax(),
            "total": self.calculate_total(),
            "created_at": self.created_at
        }

# ==================
# 6. INVENTORY MANAGEMENT (Functions + Loops)
# ==================

class InventoryManager:
    """Class untuk manage inventory dengan berbagai utility functions"""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.low_stock_threshold = 5
    
    def add_product(self, product: Product) -> str:
        """Add produk ke inventory"""
        self.products[product.id] = product
        return f"Produk {product.name} berhasil ditambahkan dengan ID: {product.id}"
    
    def remove_product(self, product_id: str) -> str:
        """Remove produk dari inventory - menggunakan conditions"""
        if product_id in self.products:
            product = self.products.pop(product_id)
            return f"Produk {product.name} berhasil dihapus dari inventory"
        else:
            return "Produk tidak ditemukan"
    
    def search_products(self, keyword: str = "", category: str = "", min_price: float = 0, max_price: float = float('inf')) -> List[Product]:
        """Search produk dengan multiple filters - menggunakan loops dan conditions"""
        results = []
        keyword = keyword.lower()
        
        for product in self.products.values():
            # Filter berdasarkan keyword
            if keyword and keyword not in product.name.lower() and keyword not in product.description.lower():
                continue
            
            # Filter berdasarkan category
            if category and product.category.lower() != category.lower():
                continue
            
            # Filter berdasarkan price range
            if product.price < min_price or product.price > max_price:
                continue
            
            # Filter hanya produk aktif
            if not product.is_active:
                continue
            
            results.append(product)
        
        return results
    
    def get_low_stock_products(self) -> List[Product]:
        """Get produk dengan stock rendah - menggunakan loops dan conditions"""
        low_stock_products = []
        
        for product in self.products.values():
            if product.stock <= self.low_stock_threshold and product.is_active:
                low_stock_products.append(product)
        
        return low_stock_products
    
    def get_category_summary(self) -> Dict[str, Dict]:
        """Get summary per category - menggunakan loops dan dictionaries"""
        category_summary = {}
        
        for product in self.products.values():
            if product.category not in category_summary:
                category_summary[product.category] = {
                    "count": 0,
                    "total_stock": 0,
                    "total_value": 0.0,
                    "active_products": 0
                }
            
            category_data = category_summary[product.category]
            category_data["count"] += 1
            category_data["total_stock"] += product.stock
            category_data["total_value"] += product.stock * product.price
            
            if product.is_active:
                category_data["active_products"] += 1
        
        return category_summary
    
    def generate_inventory_report(self) -> str:
        """Generate comprehensive inventory report - menggunakan functions dan loops"""
        report = "\n" + "="*50 + "\n"
        report += "LAPORAN INVENTORY TOKO ONLINE\n"
        report += "="*50 + "\n"
        
        total_products = len(self.products)
        active_products = sum(1 for p in self.products.values() if p.is_active)
        total_stock = sum(p.stock for p in self.products.values())
        total_value = sum(p.stock * p.price for p in self.products.values())
        
        report += f"Total Produk: {total_products}\n"
        report += f"Produk Aktif: {active_products}\n"
        report += f"Total Stock: {total_stock}\n"
        report += f"Total Nilai Inventory: {format_currency(total_value)}\n\n"
        
        # Low stock alert
        low_stock = self.get_low_stock_products()
        if low_stock:
            report += "⚠️  PERINGATAN STOCK RENDAH:\n"
            for product in low_stock:
                report += f"  - {product.name}: {product.stock} unit\n"
            report += "\n"
        
        # Category summary
        category_summary = self.get_category_summary()
        if category_summary:
            report += "RINGKASAN PER KATEGORI:\n"
            for category, data in category_summary.items():
                report += f"\n{category}:\n"
                report += f"  Produk: {data['active_products']}/{data['count']} (aktif/total)\n"
                report += f"  Stock: {data['total_stock']} unit\n"
                report += f"  Nilai: {format_currency(data['total_value'])}\n"
        
        return report

# ==================
# 7. ORDER MANAGEMENT SYSTEM (Integration)
# ==================

class OrderManager:
    """Class untuk manage orders dengan integration ke inventory"""
    
    def __init__(self, inventory_manager: InventoryManager):
        self.orders: Dict[str, Order] = {}
        self.inventory_manager = inventory_manager
    
    def create_order(self, customer: Customer) -> Order:
        """Create new order"""
        order = Order(customer)
        self.orders[order.id] = order
        return order
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Get order by ID - menggunakan conditions"""
        return self.orders.get(order_id, None)
    
    def get_customer_orders(self, customer_id: str) -> List[Order]:
        """Get orders by customer - menggunakan loops"""
        customer_orders = []
        
        for order in self.orders.values():
            if order.customer.id == customer_id:
                customer_orders.append(order)
        
        return customer_orders
    
    def get_orders_by_status(self, status: str) -> List[Order]:
        """Get orders by status - menggunakan loops dan conditions"""
        filtered_orders = []
        
        for order in self.orders.values():
            if order.status.lower() == status.lower():
                filtered_orders.append(order)
        
        return filtered_orders
    
    def process_bulk_orders(self, orders: List[Order]) -> Dict[str, str]:
        """Process multiple orders - menggunakan loops"""
        results = {}
        
        for order in orders:
            if order.status == "draft":
                success, message = order.confirm_order()
                results[order.id] = message
            else:
                results[order.id] = f"Order sudah dalam status {order.status}"
        
        return results
    
    def generate_sales_report(self, start_date: datetime.datetime = None, end_date: datetime.datetime = None) -> str:
        """Generate sales report dengan date filtering"""
        if start_date is None:
            start_date = datetime.datetime.min
        if end_date is None:
            end_date = datetime.datetime.max
        
        report = "\n" + "="*50 + "\n"
        report += "LAPORAN PENJUALAN\n"
        report += "="*50 + "\n"
        
        total_orders = 0
        confirmed_orders = 0
        total_revenue = 0.0
        cancelled_orders = 0
        
        # Statistics calculation menggunakan loops
        for order in self.orders.values():
            if start_date <= order.created_at <= end_date:
                total_orders += 1
                
                if order.status == "confirmed":
                    confirmed_orders += 1
                    total_revenue += order.calculate_total()
                elif order.status == "cancelled":
                    cancelled_orders += 1
        
        report += f"Period: {start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}\n"
        report += f"Total Orders: {total_orders}\n"
        report += f"Confirmed Orders: {confirmed_orders}\n"
        report += f"Cancelled Orders: {cancelled_orders}\n"
        report += f"Total Revenue: {format_currency(total_revenue)}\n"
        
        if confirmed_orders > 0:
            avg_order_value = total_revenue / confirmed_orders
            report += f"Average Order Value: {format_currency(avg_order_value)}\n"
        
        return report

# ==================
# 8. MAIN APPLICATION CLASS (Complete Integration)
# ==================

class TokoOnlineApp:
    """Main application class yang mengintegrasikan semua komponen"""
    
    def __init__(self, store_name: str):
        self.store_name = store_name
        self.inventory_manager = InventoryManager()
        self.order_manager = OrderManager(self.inventory_manager)
        self.customers: Dict[str, Customer] = {}
        self.running = True
    
    def register_customer(self, name: str, email: str, phone: str, address: str = "") -> tuple[bool, str, Optional[Customer]]:
        """Register customer baru dengan validation"""
        # Validasi email dan phone menggunakan functions
        if not validate_email(email):
            return False, "Format email tidak valid!", None
        
        if not validate_phone(phone):
            return False, "Format nomor telepon tidak valid!", None
        
        # Cek apakah email sudah terdaftar menggunakan loops
        for customer in self.customers.values():
            if customer.email == email:
                return False, "Email sudah terdaftar!", None
        
        # Create customer baru
        customer = Customer(name, email, phone, address)
        self.customers[customer.id] = customer
        
        return True, f"Customer {name} berhasil terdaftar dengan ID: {customer.id}", customer
    
    def setup_sample_data(self):
        """Setup sample data untuk demo - menggunakan loops untuk efficiency"""
        print("Setting up sample data...")
        
        # Sample customers
        sample_customers = [
            ("John Doe", "john@example.com", "081234567890", "Jakarta"),
            ("Jane Smith", "jane@example.com", "081234567891", "Bandung"),
            ("Bob Wilson", "bob@example.com", "081234567892", "Surabaya")
        ]
        
        for name, email, phone, address in sample_customers:
            success, message, customer = self.register_customer(name, email, phone, address)
            if success:
                print(f"✓ {message}")
        
        # Sample products - demonstrasi inheritance
        sample_products = [
            Electronics("iPhone 14", 15000000, "Apple", 12, "Latest iPhone with advanced features"),
            Electronics("Samsung Galaxy S23", 12000000, "Samsung", 12, "Premium Android smartphone"),
            Electronics("MacBook Air M2", 18000000, "Apple", 12, "Lightweight laptop with M2 chip"),
            
            Clothing("T-Shirt Premium", 150000, "L", "Blue", "Cotton", "Premium quality t-shirt"),
            Clothing("Jeans", 300000, "32", "Black", "Denim", "Comfortable denim jeans"),
            Clothing("Sneakers", 800000, "42", "White", "Leather", "Premium sneakers"),
            
            Book("Python Programming", 200000, "John Smith", "978-123456789", 350, "Learn Python programming"),
            Book("Data Science Handbook", 250000, "Jane Doe", "978-987654321", 500, "Complete data science guide"),
            Book("Machine Learning", 300000, "AI Expert", "978-555666777", 450, "ML fundamentals and applications")
        ]
        
        for product in sample_products:
            # Set random stock using conditions
            if product.category == "Electronics":
                product.set_stock(10)
            elif product.category == "Clothing":
                product.set_stock(20)
            else:  # Books
                product.set_stock(15)
            
            message = self.inventory_manager.add_product(product)
            print(f"✓ {message}")
        
        print("\nSample data setup completed!\n")
    
    def demo_order_process(self):
        """Demo complete order process"""
        print("="*60)
        print("DEMO: COMPLETE ORDER PROCESS")
        print("="*60)
        
        # Get customer dan products
        customer = list(self.customers.values())[0]  # First customer
        products = list(self.inventory_manager.products.values())
        
        print(f"\nCustomer: {customer.name} ({customer.membership_level})")
        print(f"Discount Rate: {customer.get_discount_rate()*100:.0f}%")
        
        # Create order
        order = self.order_manager.create_order(customer)
        print(f"\nOrder created: {order.id}")
        
        # Add items menggunakan loops dan conditions
        sample_items = [
            (products[0], 1),  # iPhone
            (products[3], 2),  # T-Shirt
            (products[6], 1)   # Python Book
        ]
        
        for product, quantity in sample_items:
            result = order.add_item(product, quantity)
            print(f"✓ {result}")
        
        # Show order summary sebelum confirm
        print("\n" + "="*40)
        print("ORDER SUMMARY SEBELUM KONFIRMASI:")
        print("="*40)
        print(order.get_order_summary())
        
        # Confirm order
        success, message = order.confirm_order()
        if success:
            print(f"\n✓ {message}")
            print("\n" + "="*40)
            print("FINAL ORDER SUMMARY:")
            print("="*40)
            print(order.get_order_summary())
            
            # Show updated customer info
            print("\n" + "="*40)
            print("UPDATED CUSTOMER INFO:")
            print("="*40)
            print(customer.get_customer_summary())
        else:
            print(f"\n✗ {message}")
    
    def demo_inventory_management(self):
        """Demo inventory management features"""
        print("="*60)
        print("DEMO: INVENTORY MANAGEMENT")
        print("="*60)
        
        # Search products
        print("\n1. SEARCH PRODUCTS:")
        print("-" * 20)
        
        search_tests = [
            ("iPhone", "", 0, float('inf')),
            ("", "Electronics", 0, float('inf')),
            ("", "", 100000, 500000)
        ]
        
        for keyword, category, min_price, max_price in search_tests:
            results = self.inventory_manager.search_products(keyword, category, min_price, max_price)
            print(f"\nSearch: keyword='{keyword}', category='{category}', price={min_price}-{max_price}")
            print(f"Found {len(results)} products:")
            for product in results[:3]:  # Show only first 3
                print(f"  - {product.get_info()}")
        
        # Low stock products
        print("\n2. LOW STOCK CHECK:")
        print("-" * 20)
        
        # Artificially reduce stock for demo
        products = list(self.inventory_manager.products.values())
        if len(products) > 0:
            products[0].stock = 2  # Make first product low stock
            
        low_stock = self.inventory_manager.get_low_stock_products()
        if low_stock:
            print("Low stock products found:")
            for product in low_stock:
                print(f"  ⚠️  {product.name}: {product.stock} units")
        else:
            print("No low stock products found.")
        
        # Inventory report
        print("\n3. INVENTORY REPORT:")
        print("-" * 20)
        print(self.inventory_manager.generate_inventory_report())
    
    def demo_customer_management(self):
        """Demo customer management"""
        print("="*60)
        print("DEMO: CUSTOMER MANAGEMENT")
        print("="*60)
        
        # Show all customers dengan loops
        print("\nREGISTERED CUSTOMERS:")
        print("-" * 30)
        for customer in self.customers.values():
            print(f"ID: {customer.id}")
            print(f"Name: {customer.name}")
            print(f"Email: {customer.email}")
            print(f"Phone: {customer.phone}")
            print(f"Membership: {customer.membership_level}")
            print(f"Total Orders: {customer.total_orders}")
            print(f"Total Spent: {format_currency(customer.total_spent)}")
            print("-" * 30)
        
        # Demo validation
        print("\nVALIDATION TESTS:")
        print("-" * 20)
        
        test_emails = ["valid@email.com", "invalid-email", "test@domain.co.id"]
        test_phones = ["081234567890", "123", "+6281234567890"]
        
        print("Email validation:")
        for email in test_emails:
            valid = validate_email(email)
            print(f"  {email}: {'✓' if valid else '✗'}")
        
        print("\nPhone validation:")
        for phone in test_phones:
            valid = validate_phone(phone)
            print(f"  {phone}: {'✓' if valid else '✗'}")
    
    def demo_sales_analytics(self):
        """Demo sales analytics"""
        print("="*60)
        print("DEMO: SALES ANALYTICS")
        print("="*60)
        
        # Show orders by status menggunakan loops dan conditions
        statuses = ["draft", "confirmed", "cancelled"]
        
        for status in statuses:
            orders = self.order_manager.get_orders_by_status(status)
            print(f"\n{status.upper()} ORDERS: {len(orders)}")
            
            for order in orders:
                print(f"  Order {order.id}: {order.customer.name} - {format_currency(order.calculate_total())}")
        
        # Sales report
        print(self.order_manager.generate_sales_report())
    
    def run_complete_demo(self):
        """Run complete demo of the application"""
        print(f"🏪 SELAMAT DATANG DI {self.store_name.upper()} 🏪")
        print("="*70)
        
        # Setup sample data
        self.setup_sample_data()
        
        # Demo sections
        self.demo_inventory_management()
        input("\nTekan Enter untuk melanjutkan ke demo order process...")
        
        self.demo_order_process()
        input("\nTekan Enter untuk melanjutkan ke demo customer management...")
        
        self.demo_customer_management()
        input("\nTekan Enter untuk melanjutkan ke demo sales analytics...")
        
        self.demo_sales_analytics()
        
        print("\n" + "="*70)
        print("DEMO COMPLETED! 🎉")
        print("="*70)
        print("""
FITUR YANG TELAH DIDEMONSTRASIKAN:

1. ALUR LOGIKA (CONDITIONS):
   ✓ Validasi email dan phone
   ✓ Membership level determination
   ✓ Stock availability checks
   ✓ Order status management
   ✓ Price range filtering

2. PERULANGAN (LOOPS):
   ✓ Product search dan filtering
   ✓ Order processing
   ✓ Report generation
   ✓ Bulk operations
   ✓ Data summarization

3. FUNGSI (FUNCTIONS):
   ✓ Utility functions (validation, formatting)
   ✓ Calculation functions (discount, tax, shipping)
   ✓ Business logic functions
   ✓ Report generation functions

4. OOP (OBJECT-ORIENTED PROGRAMMING):
   ✓ Inheritance (Product -> Electronics/Clothing/Book)
   ✓ Encapsulation (private attributes dengan validation)
   ✓ Polymorphism (Product types dengan different behavior)
   ✓ Abstraction (Abstract base classes)
   ✓ Composition (Order contains OrderItems)

INTEGRATION:
✓ Semua konsep bekerja sama dalam satu aplikasi
✓ Real-world business logic implementation
✓ Scalable dan maintainable code structure
        """)

# ==================
# 9. ADVANCED FEATURES DEMO
# ==================

def demo_advanced_features():
    """Demo fitur advanced menggunakan semua konsep"""
    print("\n" + "="*70)
    print("DEMO: ADVANCED FEATURES")
    print("="*70)
    
    # Advanced search dengan multiple conditions dan custom sorting
    def advanced_product_search(inventory: InventoryManager, filters: Dict) -> List[Product]:
        """Advanced search dengan flexible filtering"""
        results = []
        
        for product in inventory.products.values():
            # Apply filters menggunakan conditions
            match = True
            
            if 'name_contains' in filters and filters['name_contains']:
                if filters['name_contains'].lower() not in product.name.lower():
                    match = False
            
            if 'category_in' in filters and filters['category_in']:
                if product.category not in filters['category_in']:
                    match = False
            
            if 'price_range' in filters and filters['price_range']:
                min_price, max_price = filters['price_range']
                if not (min_price <= product.price <= max_price):
                    match = False
            
            if 'min_stock' in filters and filters['min_stock'] is not None:
                if product.stock < filters['min_stock']:
                    match = False
            
            if 'is_available' in filters and filters['is_available'] is not None:
                if product.is_available() != filters['is_available']:
                    match = False
            
            if match:
                results.append(product)
        
        # Custom sorting menggunakan lambda dan conditions
        if 'sort_by' in filters:
            sort_key = filters['sort_by']
            reverse = filters.get('sort_desc', False)
            
            if sort_key == 'price':
                results.sort(key=lambda p: p.price, reverse=reverse)
            elif sort_key == 'name':
                results.sort(key=lambda p: p.name.lower(), reverse=reverse)
            elif sort_key == 'stock':
                results.sort(key=lambda p: p.stock, reverse=reverse)
            elif sort_key == 'category':
                results.sort(key=lambda p: p.category, reverse=reverse)
        
        return results
    
    # Performance monitoring decorator
    def monitor_performance(func):
        """Decorator untuk monitor performance"""
        import time
        
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"⏱️  Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper
    
    # Create app instance
    app = TokoOnlineApp("Advanced Demo Store")
    app.setup_sample_data()
    
    print("\n1. ADVANCED PRODUCT SEARCH:")
    print("-" * 35)
    
    # Test various search filters
    search_filters = [
        {
            'name_contains': 'Phone',
            'price_range': (1000000, 20000000),
            'is_available': True,
            'sort_by': 'price',
            'sort_desc': False
        },
        {
            'category_in': ['Electronics', 'Books'],
            'min_stock': 10,
            'sort_by': 'stock',
            'sort_desc': True
        }
    ]
    
    for i, filters in enumerate(search_filters, 1):
        print(f"\nFilter Set {i}: {filters}")
        results = advanced_product_search(app.inventory_manager, filters)
        print(f"Found {len(results)} products:")
        for product in results[:3]:
            print(f"  - {product.get_info()}")
    
    print("\n2. BULK OPERATIONS:")
    print("-" * 20)
    
    # Bulk stock update menggunakan loops dan conditions
    @monitor_performance
    def bulk_stock_update(inventory: InventoryManager, updates: List[tuple]):
        """Bulk update stock dengan validation"""
        results = []
        
        for product_id, new_stock in updates:
            if product_id in inventory.products:
                product = inventory.products[product_id]
                if new_stock >= 0:
                    old_stock = product.stock
                    product.stock = new_stock
                    results.append(f"✓ {product.name}: {old_stock} → {new_stock}")
                else:
                    results.append(f"✗ {product.name}: Invalid stock value")
            else:
                results.append(f"✗ Product {product_id}: Not found")
        
        return results
    
    # Test bulk operations
    product_ids = list(app.inventory_manager.products.keys())[:3]
    stock_updates = [(pid, 25) for pid in product_ids]
    
    print("Bulk stock update:")
    update_results = bulk_stock_update(app.inventory_manager, stock_updates)
    for result in update_results:
        print(f"  {result}")
    
    print("\n3. ADVANCED ANALYTICS:")
    print("-" * 25)
    
    # Advanced analytics menggunakan loops, conditions, dan functions
    def generate_advanced_analytics(app: TokoOnlineApp):
        """Generate advanced analytics report"""
        analytics = {
            'customer_segments': {},
            'product_performance': {},
            'revenue_trends': {}
        }
        
        # Customer segmentation berdasarkan spending patterns
        for customer in app.customers.values():
            if customer.total_spent >= 5000000:
                segment = 'High Value'
            elif customer.total_spent >= 1000000:
                segment = 'Medium Value'
            elif customer.total_orders > 0:
                segment = 'Low Value'
            else:
                segment = 'New Customer'
            
            if segment not in analytics['customer_segments']:
                analytics['customer_segments'][segment] = {
                    'count': 0,
                    'total_spent': 0,
                    'avg_order_value': 0
                }
            
            analytics['customer_segments'][segment]['count'] += 1
            analytics['customer_segments'][segment]['total_spent'] += customer.total_spent
            
            if customer.total_orders > 0:
                analytics['customer_segments'][segment]['avg_order_value'] += customer.total_spent / customer.total_orders
        
        # Product performance analysis
        for product in app.inventory_manager.products.values():
            category = product.category
            if category not in analytics['product_performance']:
                analytics['product_performance'][category] = {
                    'total_products': 0,
                    'avg_price': 0,
                    'total_stock_value': 0,
                    'low_stock_items': 0
                }
            
            perf = analytics['product_performance'][category]
            perf['total_products'] += 1
            perf['avg_price'] += product.price
            perf['total_stock_value'] += product.stock * product.price
            
            if product.stock <= app.inventory_manager.low_stock_threshold:
                perf['low_stock_items'] += 1
        
        # Calculate averages
        for category in analytics['product_performance']:
            perf = analytics['product_performance'][category]
            if perf['total_products'] > 0:
                perf['avg_price'] /= perf['total_products']
        
        for segment in analytics['customer_segments']:
            seg = analytics['customer_segments'][segment]
            if seg['count'] > 0:
                seg['avg_order_value'] /= seg['count']
        
        return analytics
    
    # Generate dan display analytics
    analytics = generate_advanced_analytics(app)
    
    print("\nCustomer Segments:")
    for segment, data in analytics['customer_segments'].items():
        print(f"  {segment}: {data['count']} customers")
        print(f"    Total Spent: {format_currency(data['total_spent'])}")
        print(f"    Avg Order Value: {format_currency(data['avg_order_value'])}")
        print()
    
    print("Product Performance by Category:")
    for category, data in analytics['product_performance'].items():
        print(f"  {category}:")
        print(f"    Products: {data['total_products']}")
        print(f"    Avg Price: {format_currency(data['avg_price'])}")
        print(f"    Stock Value: {format_currency(data['total_stock_value'])}")
        print(f"    Low Stock Items: {data['low_stock_items']}")
        print()

# ==================
# 10. MAIN EXECUTION
# ==================

def main():
    """Main function to run the complete demonstration"""
    print("🐍 TUTORIAL PYTHON: INTEGRASI LENGKAP SEMUA KONSEP 🐍")
    print("="*70)
    
    # Create main application
    app = TokoOnlineApp("Python Learning Store")
    
    # Run complete demo
    app.run_complete_demo()
    
    # Ask for advanced demo
    response = input("\nApakah Anda ingin melihat demo fitur advanced? (y/n): ").lower()
    if response in ['y', 'yes', 'ya']:
        demo_advanced_features()
    
    print("\n" + "="*70)
    print("TERIMA KASIH TELAH MENGIKUTI TUTORIAL! 🎓")
    print("="*70)
    print("""
SUMMARY PEMBELAJARAN:

✅ ALUR LOGIKA (CONDITIONS):
   - Validasi input dan data
   - Business rules implementation
   - Status management
   - Conditional processing

✅ PERULANGAN (LOOPS):
   - Data processing dan filtering
   - Report generation
   - Bulk operations
   - Iterative calculations

✅ FUNGSI (FUNCTIONS):
   - Code modularity dan reusability
   - Utility functions
   - Business logic separation
   - Decorators untuk cross-cutting concerns

✅ OOP (OBJECT-ORIENTED PROGRAMMING):
   - Real-world modeling dengan classes
   - Inheritance untuk code reuse
   - Encapsulation untuk data security
   - Polymorphism untuk flexibility
   - Abstraction untuk simplicity

🎯 INTEGRASI:
   - Semua konsep bekerja bersama
   - Scalable architecture
   - Maintainable code structure
   - Real-world aplikasi

Selamat! Anda telah menguasai fundamental Python programming! 🚀
    """)

if __name__ == "__main__":
    main()
