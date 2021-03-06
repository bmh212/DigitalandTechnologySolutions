from postcode import centre_point
from crimes_in_radius import crimes_in_radius
from postcode_validate import validatePostcode
from validateDate2 import validateDate

if __name__ == '__main__':
    """
    Takes the postcode input and returns a nested list of strings
    from the csv file of crimes in radius. This is then written to the
    csv file with unneccesary characters stripped
    """
    postcode = input("Please enter a postcode for the Devon and Cornwall area.")
    input_date = input("Please enter the date.")
    
    date_valid, date = validateDate(input_date) #checks date
    
    if validatePostcode(postcode) and date_valid:  # checks for valid postcode
        try:  # catches exemption of postcode not found
            post_data = centre_point(postcode, 'postcodes.csv') # gets centrepoint latlong
            postcode_lat = post_data[0]
            postcode_lon = post_data[1]
            
            cr_list = crimes_in_radius(date, postcode_lat, postcode_lon)
        
            new_file = open('crimes_in_radius.csv', 'w')
            # cleans list before writing to csv file
            for row in cr_list:
                temp_row = ''
                for element in row:  # cleaning quotes and brackets
                    element.lstrip('\'')
                    element.lstrip('[')
                    element.lstrip(']')
                    temp_row = temp_row + element + ',' # recreates csv file
                row = temp_row
                new_file.write("%s\n" % row)
         
            new_file.close()
        
        except ValueError:
            print("We cannot find your postcode.")
    else:
        print("Sorry, the details you provided were invalid!")
