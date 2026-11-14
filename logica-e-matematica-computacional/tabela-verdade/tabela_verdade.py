# Tabelas verdade para proposições simples e compostas
# Linguagem de Programação / Lógica e Matemática Computacional
from itertools import product   # gera todas as combinações de V e F

def implica(p, q):
    """Implicação lógica P -> Q: só é falsa quando P é V e Q é F."""
    return (not p) or q

# ---------- Tabela 1: negação ----------
print("a) Negação  ¬P")
print("P     | ¬P")
for p in (True, False):
    print(f"{'V' if p else 'F'}     | {'V' if not p else 'F'}")

# ---------- Tabela 2: implicação ----------
print("\nb) Implicação  P → Q")
print("P     | Q     | P → Q")
for p, q in product((True, False), repeat=2):
    print(f"{'V' if p else 'F'}     | {'V' if q else 'F'}     | {'V' if implica(p, q) else 'F'}")

falsas = [(p, q) for p, q in product((True, False), repeat=2) if not implica(p, q)]
print("A implicação é FALSA apenas em:", ", ".join(f"P={'V' if p else 'F'} e Q={'V' if q else 'F'}" for p, q in falsas))

# ---------- Tabela 3: proposição composta ----------
print("\nc) Proposição composta  (P ∧ Q) ∨ (¬P)")
print("P     | Q     | P ∧ Q | ¬P    | (P ∧ Q) ∨ (¬P)")
resultados = []
for p, q in product((True, False), repeat=2):
    conj = p and q
    neg = not p
    res = conj or neg
    resultados.append(res)
    print(f"{'V' if p else 'F'}     | {'V' if q else 'F'}     | {'V' if conj else 'F'}     | {'V' if neg else 'F'}     | {'V' if res else 'F'}")

# ---------- Classificação ----------
def classificar(valores):
    """Tautologia: sempre V. Contradição: sempre F. Contingência: os dois casos."""
    if all(valores):
        return "Tautologia"
    if not any(valores):
        return "Contradição"
    return "Contingência"

neg_p = [not p for p in (True, False)]
imp   = [implica(p, q) for p, q in product((True, False), repeat=2)]

print("\n--- Classificação ---")
print("¬P: ", classificar(neg_p))
print("P → Q: ", classificar(imp))
print("(P ∧ Q) ∨ (¬P): ", classificar(resultados))
