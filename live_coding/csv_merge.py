import csv
import glob
import matplotlib.pyplot as plt

merged_files = []

csv_files = glob.glob("data/*.csv")

# csv_files = [
#     os.path.join("data", file) for file in os.listdir("data")
#     ]

def load_csv(path: str):
    with open(path, newline="") as csv_file:
        reader = csv.reader(
            csv_file
        )
        next(reader)
        for row in reader:
            row = [int(row[0]), float(row[1]), float(row[2]) if row[2] else 0]
            merged_files.append(row)
            
def sort_merge_files():
    for csv_file in csv_files:
        load_csv(csv_file)
    merged_files.sort(
        key=lambda x: x[0]
    )

def running_average(row: list, size: int = 2):
    window = []
    for i, value in enumerate(row):
        average = sum(window) / len(window) if window else 0
        if not value:
            row[i] = average
        window.append(row[i])
        window = window[-size:]
    return row
            
        

def line_plot():
    x = [row[0] for row in merged_files]
    y = [row[1] for row in merged_files]
    plt.figure(figsize=(8, 5))
    plt.plot(x,y)
    plt.savefig("line_plot.png")

def bar_plot():
    x = [row[0] for row in merged_files]
    y = [row[2] for row in merged_files]
    y_filtered = running_average(y, 5)
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].bar(x, y, color="black")
    ax[1].bar(x, y_filtered, color="skyblue")
    
    fig.savefig("bar_plot.png")

sort_merge_files()
line_plot()
bar_plot()
