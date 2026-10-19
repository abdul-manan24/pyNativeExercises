import repository

records = [(1, "Mayo Clinic", 200),
           (2, "Cleveland Clinic", 400),
           (3, "Johns Hopkins", 1000)]

# repository.insert_many_records("Hospitals", records)
repository.insert_one_record("Hospitals", (4, "UCLA Medical Center", 1500))
records = repository.list_all_records("Hospitals")
print(records)