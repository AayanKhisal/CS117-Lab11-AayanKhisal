# storage_estimator.py
# Estimates how much storage a collection of files needs.

def main():
    print("Storage Estimator")
    print("-----------------")

    num_files = int(input("Number of files: "))
    avg_size_mb = float(input("Average file size (MB): "))

    total_mb = num_files * avg_size_mb

    print("Total storage needed:", total_mb, "MB")


main()
