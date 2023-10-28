

from SelfServiceCashier import Transaction

transaction123 = Transaction()
    
transaction123.add_item("Ayam Goreng", 2, 20000)
transaction123.add_item("Pasta Gigi", 3, 15000)

transaction123.check_order()

transaction123.delete_item("Pasta Gigi")

transaction123.check_order()

transaction123.reset_transaction()

transaction123.add_item("Ayam Goreng", 2, 20_000)

transaction123.add_item("Pasta Gigi", 3, 15_000)

transaction123.add_item("Mainan Mobil", 1, 200_000)

transaction123.add_item("Mie Instant", 5, 3_000)

transaction123.check_order()

transaction123.total_price()