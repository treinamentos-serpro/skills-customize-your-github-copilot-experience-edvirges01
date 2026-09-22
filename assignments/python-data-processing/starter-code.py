import csv


def load_records(file_path):
    """Read CSV records into a list of dictionaries."""
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def summarize_records(records):
    """Return a basic summary for the records."""
    if not records:
        return {
            "total_records": 0,
            "average_score": 0,
            "highest_score": 0,
            "lowest_score": 0,
        }

    scores = [int(record["score"]) for record in records if record.get("score")]
    return {
        "total_records": len(records),
        "average_score": sum(scores) / len(scores) if scores else 0,
        "highest_score": max(scores) if scores else 0,
        "lowest_score": min(scores) if scores else 0,
    }


if __name__ == "__main__":
    data = load_records("data.csv")
    print(f"Loaded {len(data)} records.")
    print(summarize_records(data))
