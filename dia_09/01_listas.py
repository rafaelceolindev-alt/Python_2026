# %%

x = []
for i in range(1,101):
        x.append(i)

x
# %%

y = [i for i in range(1,101)]
y

# %%

def e_par(x):
        return x % 2 == 0

z = [e_par(i) for i in range(1,101)]
z

# %%

w = [i for i in range(1,101) if e_par(i)]
w