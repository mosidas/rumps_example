from decimal import Decimal, getcontext
getcontext().prec = 100

# rumpの例題をそのまま計算 → とんでもない値になる
def calc_rump(a, b):
    return 333.75 *  b ** 6 + a ** 2 *( 11 * a ** 2 * b ** 2 - b ** 6 - 121 * b ** 4 - 2) + 5.5 * b ** 8 + a / ( 2 * b )

# rumpの例題を4倍して整数値で計算する(表示するときに4で割る) → 正しい値
def calc_rump_4(a, b):
    return 1335 * (b ** 6) + 4 * (a ** 2) * (11 * (a ** 2) * (b ** 2) - (b ** 6) - 121 * (b ** 4) - 2) + 22 * (b ** 8) + (2 * a) / b

# rumpの例題をDecimal型を使って計算 → 正しい値
def calc_rump_decimal(a, b):
    return Decimal('333.75') *  b ** 6 + a ** 2 *( 11 * a ** 2 * b ** 2 - b ** 6 - 121 * b ** 4 - 2) + Decimal('5.5') * b ** 8 + a / ( 2 * b )

print(calc_rump(77617.0, 33096.0))
print(calc_rump_4(77617, 33096) / 4)
print(calc_rump_decimal(Decimal('77617.0'), Decimal('33096.0')))
