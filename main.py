from classes.contapoupanca import ContaPoupanca
from classes.cc import ContaCorrente

# cp = ContaCorrente(1111, 2222, 5)
# cp.depositar(10)
# cp.sacar(5)
# cp.sacar(10)
# cp.sacar(1)

cc = ContaCorrente(1001, 2002, 5, limite=1000)
cc.depositar(100)
cc.sacar(1050)
