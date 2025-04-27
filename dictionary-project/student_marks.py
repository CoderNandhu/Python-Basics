# Problem: Manage a student's subject marks.

# ✅ Create a dictionary marks with keys: "Math", "Science", "History", each with marks out of 100.
marks = {
    "maths": 85,
    "science": 75,
    "history": 62
}

# ✅ Update "Science" marks.
marks.update({"science": 82})
# ✅ Add "English" subject.
marks["english"] = 79
# ✅ Delete "History".
marks.pop("history")
# ✅ Print subject and marks nicely.
print(f"The finals marks obtain in subjects are : {marks}")