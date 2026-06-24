from datetime import date
import inflect
import sys


class Dob:
    def __init__(self,dob_date):
        self.dob_date=dob_date

    def get_dob(self):
        try:
            dob_date=date.fromisoformat(self.dob_date)
            if date.today()<dob_date:
                raise ValueError
            return dob_date
        except ValueError:
            sys.exit("Invalid Date")


    def get_total_minutes(self):
        today=date.today()

        diff=today - self.get_dob()
        total_minutes=int(diff.total_seconds()/60)
        return total_minutes

    def __str__(self):
        p=inflect.engine()
        return (p.number_to_words(self.get_total_minutes(), andword="") + " minutes").capitalize()


def main():
    dob_date=input("Date of Birth: ")

    dob=Dob(dob_date)
    print(dob)

if __name__=="__main__":
    main()