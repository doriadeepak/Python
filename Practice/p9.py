#String Comparison-
# Yup!! it works, just kinda hard to predict

word = input("Enter the word: ")
if word == "banana":
    print("All right, bananas.")
elif word < "banana":
    print("Your word, " + word + ", comes before banana." )
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("All right, bananas.")
    