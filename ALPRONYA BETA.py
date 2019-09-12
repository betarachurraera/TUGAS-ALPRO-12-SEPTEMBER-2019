def bonus(GPA):
    bonus = 500000
    insentif = GPA*bonus
    return insentif


listGPA = [3,2.7,2.5,4]
for GPA in listGPA:
    if GPA > 3 :
        insentif = bonus(GPA)
        print("--------------------------------")
        print("anda mendapatkan insentif sebesar = Rp.",bonus(GPA))
        print("--------------------------------")
    else:
        print("coba lagi")
    

