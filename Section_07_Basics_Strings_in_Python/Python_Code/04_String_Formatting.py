fn = "Mj"
sn = "Dad"
ss = "Hello {0}. You are my love! Also i love {1}"
vv = ss.format(fn, sn)
print(vv)
# --------------------------------------------------
fn = "Mj"
sn = "Dad"
ss = f"Hello {fn}. You are my love! Also i love {sn}"
print(ss)
# --------------------------------------------------
fn = input("Enter your first Love: ")
sn = input("Enter your second Love: ")
ss = f"Hello {fn}. You are my love! Also i love {sn}"
print(ss)
