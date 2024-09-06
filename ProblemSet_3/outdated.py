months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}
class InvalidDate(Exception):
   pass

while True:
   try:
      original_date = input('Date: ').strip()

      if '/' in original_date:
         m, d, y = original_date.split('/')
         if int(m) > 12 or int(d) > 31:
            raise InvalidDate
         m = m.zfill(2)
         d = d.zfill(2)

      else:
         m, d, y = original_date.split()

         if ',' not in original_date:
            raise InvalidDate
         if m not in months:
            raise InvalidDate

         m = months[m]
         d = d.rstrip(',')


      if int(d) > 31:
         raise InvalidDate

      d = d.zfill(2)

      print(f'{y}-{m}-{d}')

      break

   except (InvalidDate, ValueError, IndexError):
      print('Invalid date, please insert a valid one.')
