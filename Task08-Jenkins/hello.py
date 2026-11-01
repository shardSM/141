# Script run by Jenkins on every build (no input(), so the build doesn't hang)
for i in range(1, 11):
    print(f"Square of {i} = {i * i}")
print("Build successful!")
