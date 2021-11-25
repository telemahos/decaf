-- A Python FastAPI, finance application for Floretta company --

Λοιπόν, το πρόγραμμα λειτουργεί ως εξής: 
- Για να περάσει νέα Σημείωση γίνεται από το modal που βρίσκεται στο components φάκελο
- μετά την καταχώρηση γίνεται ένα refresh των περιεχομένων, χωρίς να ανανεώνεται η σελίδα ολόκληρη
- Στην ουσία χρησιμοποιώ ένα modal από το vuejs example, και όχι το modal του Bootstrap και αυτό γιατί δεν μπορούσα να ξαναφωρτώσω το περιεχώμενο χωρίς ανανέωση της σελίδας.
- Πρέπει οπωσδήποτε να είναι 'Content-Type': 'application/json' για να περναει από της Ασφάλεια CRSF δηλ:
    const headers = { 
        'Authorization': `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      };    
- Τζαμπα εφαγα όλη μερα γιατί δεν πρόσεξα ότι στο backend repository income στη μέθοδο create δεν είχα συμπεριλάβει το shift_id. Και πεδευόμουν όλη μερα, έχοντας απορία γιατί με κάυε δοκιμή το shift_id εβγαζε null.
- ICONS:
  https://github.com/danklammer/bytesize-icons
- Χρησιμοποιώ το moment.js για να δείνχω ελληνική ημερομηνία
- ModalIncomeList: Στα props, έπρεπε να προσθέσω όλα τα στοιχεία στο singleIncome Object, ώστε να μην χρειάζεται να έχω δυο διαφορετικά props αλλά μόνο ένα. Π.χ. μετέφερα από το shiftStaff -> singleIncome και τα εξής: the_shift.service_id_1 και 2 όπως και the_shift.barman_id_1 και 2
- routers/income.py: Είχα ένα πρόβλημα όταν έδινα έτος και μήνα στο URL url/api/income/2021/09?&page=1&size=31, όπου δεν πρόσεξα ότι πρέπει το αποτέλεσμα απο το SQL request στο τέλος να το περιελάβω στο pagination. Όταν το περιέλαβα το αποτέλεσμα, λύθηκαn όλα τα προβλήματα: 
  return paginate(income.show_by_date(year, month, db)),
Επίσης πρέπει να προσέχω το path parameter να είναι ο αντίστοιχος τύπος πχ. int, str, bool κλπ.
  - Προσοχή σε νέα εγκατάσταση, το fastapi-pagination να είναι το 0.8.3 στο dec_env/lib/python3.7/site-packages