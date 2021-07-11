# Print files in a directolry

from pathlib import Path
path = Path()
for file in path.glob('*'):
    print(file)
    