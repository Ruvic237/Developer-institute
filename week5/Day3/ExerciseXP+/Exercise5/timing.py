
from datetime import datetime

datenow = datetime.today()
datejan = datetime(2023, 1, 1)
diff = datejan - datenow
print(f"The 1st of january is in {diff}")


