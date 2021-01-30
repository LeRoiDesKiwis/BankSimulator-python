import bank

manager = bank.BankManager()
manager.register_bank("Crédit Mutuel")
manager.register_bank("Crédit Agricole")

kiwi, _ = manager.register(1, "kiwi")
guiguim, _ = manager.register(2, "guiguim")

manager.pay_with_card(kiwi, guiguim)